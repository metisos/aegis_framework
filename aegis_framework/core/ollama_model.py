"""
OllamaLocalModel: Interface for local LLM integration through Ollama.
"""

import subprocess
import logging
from typing import Optional

class OllamaLocalModel:
    """
    Interface for local LLM models using Ollama.
    Requires Ollama to be installed locally: https://ollama.ai
    """
    
    def __init__(self, model: str = "llama2:13b"):
        """
        Initialize the Ollama model interface.
        
        Args:
            model: Name of the Ollama model to use (e.g., "llama2:13b", "mistral", "codellama")
        """
        self.model = model
    
    def invoke(self, prompt: str) -> str:
        """
        Generate a response using the Ollama model.
        
        Args:
            prompt: Input text to process
            
        Returns:
            str: Generated response from the model
        
        Raises:
            subprocess.CalledProcessError: If Ollama command fails
        """
        try:
            result = subprocess.run(
                ["ollama", "run", self.model],
                input=prompt,
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            logging.error(f"Ollama error: {e.stderr}")
            raise
