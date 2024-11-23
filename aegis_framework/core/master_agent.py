"""
MasterAIAgent: Core agent class for the Aegis Framework.
"""

from flask import Flask, request, render_template, jsonify
from flask_socketio import SocketIO, emit
import sqlite3
import importlib
import os
from datetime import datetime
from fuzzywuzzy import process
import threading
from typing import Optional, Dict, Any, List

from .ollama_model import OllamaLocalModel

class MasterAIAgent:
    """
    Core agent class for managing AI agents and tasks.
    """
    
    def __init__(self, socketio: Optional[SocketIO] = None, model: str = "gemma2:9b"):
        """
        Initialize the MasterAIAgent.
        
        Args:
            socketio: Optional SocketIO instance for real-time updates
            model: Name of the Ollama model to use
        """
        self.llm = OllamaLocalModel(model=model)
        self.socketio = socketio
        self.init_database()
        self.agents = {}
        self.agent_task_map = {
            "test_agent": ["test", "run a test", "testing", "execute test"],
            "coding_agent": ["create an agent", "create", "create agent", "build a new agent", "generate agent"],
            "daily_summary": ["daily summary", "summary", "summarize", "report"],
            "worldnews": ["world news", "news", "latest news", "current events"],
            "shell": ["IP scan", "network scan", "run a pentest", "analyze network", "pentesting"],
            "googlesearch": ["google search", "search", "google", "research", "web search", "find information"],
            "design_agent": ["design agent", "create new agent", "agent architecture", "agent design"],
        }
        self.load_agents()
        self.suggested_prompts = self.generate_suggested_prompts()

    def init_database(self):
        """Initialize the SQLite database for storing insights."""
        self.conn = sqlite3.connect('knowledge_base.db', check_same_thread=False)
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS insights (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            task TEXT,
                            insight TEXT,
                            confidence INTEGER,
                            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                          )''')
        self.conn.commit()

    def save_insight(self, task: str, insight: str, confidence: int = 5):
        """Save an insight to the database."""
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO insights (task, insight, confidence) VALUES (?, ?, ?)",
                       (task, insight, confidence))
        self.conn.commit()

    def load_agents(self):
        """Load available agent modules."""
        agent_dir = os.path.join(os.path.dirname(__file__), 'agents')
        if not os.path.exists(agent_dir):
            return
            
        for filename in os.listdir(agent_dir):
            if filename.endswith('.py') and filename != '__init__.py':
                module_name = filename[:-3]
                try:
                    module = importlib.import_module(f'agents.{module_name}')
                    self.agents[module_name] = module
                    message = f"Loaded agent: {module_name}"
                    print(message)
                    if self.socketio:
                        self.socketio.emit('status_update', {'message': message})
                except Exception as e:
                    error_message = f"Failed to load agent {module_name}: {e}"
                    print(error_message)
                    if self.socketio:
                        self.socketio.emit('status_update', {'message': error_message})

    def generate_suggested_prompts(self) -> List[str]:
        """Generate a list of suggested prompts based on agent capabilities."""
        prompts = []
        for keywords in self.agent_task_map.values():
            prompts.extend(keywords)
        return prompts

    def interpret_intent(self, task: str) -> str:
        """
        Interpret the intent of a task.
        
        Args:
            task: Task description
            
        Returns:
            str: 'conversational' or 'action'
        """
        if any(phrase in task.lower() for phrase in ["can you", "what is", "tell me about", "explain"]):
            return "conversational"
        return "action"

    def perform_task(self, task: str) -> str:
        """
        Perform a given task using appropriate agent or LLM.
        
        Args:
            task: Task description
            
        Returns:
            str: Task result or response
        """
        task = task.lower().strip()
        self._emit_status(f"Received task: '{task}'")

        intent = self.interpret_intent(task)
        if intent == "conversational":
            self._emit_status("Interpreted as a general question.")
            return self.generate_response(task)

        keyword_agent_map = {keyword: agent for agent, keywords in self.agent_task_map.items() for keyword in keywords}
        keywords = list(keyword_agent_map.keys())

        best_match, score = process.extractOne(task, keywords)
        if score >= 70:
            agent_name = keyword_agent_map[best_match]
            agent_module = self.agents.get(agent_name)
            if agent_module and hasattr(agent_module, "run_task"):
                self._emit_status(f"Routing to agent '{agent_name}' (match: '{best_match}', score: {score})")
                try:
                    result = agent_module.run_task(task, self.llm) if agent_name == "googlesearch" else agent_module.run_task(task)
                    self.save_insight(task, result)
                    return result
                except Exception as e:
                    return f"Error executing task with {agent_name} agent: {e}"

        self._emit_status("No strong agent match; defaulting to LLM.")
        return self.generate_response(task)

    def generate_response(self, task_description: str) -> str:
        """
        Generate a response using the LLM.
        
        Args:
            task_description: Task or question description
            
        Returns:
            str: Generated response
        """
        prompt = f"{task_description}\nRespond conversationally or with the best possible answer."
        try:
            response = self.llm.invoke(prompt)
            self.save_insight(task_description, response, confidence=5)
            return response
        except Exception as e:
            return f"Error generating response: {e}"

    def _emit_status(self, message: str):
        """Emit a status update if socketio is available."""
        print(message)
        if self.socketio:
            self.socketio.emit('status_update', {'message': message})
