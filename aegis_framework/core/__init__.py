"""Core components of the Aegis Framework."""

from .master_agent import MasterAIAgent
from .ollama_model import OllamaLocalModel

__all__ = ["MasterAIAgent", "OllamaLocalModel"]
