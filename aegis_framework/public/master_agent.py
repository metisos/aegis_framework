"""
Public interface for MasterAIAgent.
"""

from typing import Optional, Dict, Any, List
from ..core.master_agent import MasterAIAgent as CoreMasterAIAgent

class MasterAIAgent(CoreMasterAIAgent):
    """
    Public interface for creating AI agents with optional LLM capabilities.
    """
    
    def __init__(self, model: str = "gemma2:9b"):
        """
        Initialize a MasterAIAgent.
        
        Args:
            model: Name of the Ollama model to use (e.g., "gemma2:9b", "llama2:13b")
        """
        super().__init__(socketio=None, model=model)
    
    def perform_task(self, task: str) -> str:
        """
        Perform a given task using appropriate agent or LLM.
        
        Args:
            task: Task description
            
        Returns:
            str: Task result or response
        """
        return super().perform_task(task)
    
    def answer_question(self, question: str) -> str:
        """
        Process a question and return an answer.
        
        Args:
            question: The question to answer
            
        Returns:
            str: The agent's response
        """
        return self.generate_response(question)
    
    def get_suggested_prompts(self) -> List[str]:
        """
        Get a list of suggested prompts based on available capabilities.
        
        Returns:
            List[str]: List of suggested prompts
        """
        return self.suggested_prompts
