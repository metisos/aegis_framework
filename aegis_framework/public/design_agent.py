"""
Public interface for DesignAgent.
"""

from typing import Optional, Dict, Any
from ..core.design_agent import DesignAgent as CoreDesignAgent, run_task

class DesignAgent(CoreDesignAgent):
    """
    Public interface for generating and managing AI agent designs.
    """
    
    def __init__(self):
        """
        Initialize the DesignAgent.
        """
        super().__init__()
    
    def generate_new_design(self) -> str:
        """
        Generate a new agent design.
        
        Returns:
            str: Path to the generated design file or error message
        """
        return super().generate_new_design()
    
    def start_periodic_design(self) -> str:
        """
        Start periodic design generation.
        
        Returns:
            str: Status message
        """
        return super().start_periodic_design()
    
    def stop_periodic_design(self) -> str:
        """
        Stop periodic design generation.
        
        Returns:
            str: Status message
        """
        return super().stop_periodic_design()

# Expose the run_task function at module level
def run_design_task(task_description: str) -> str:
    """
    Run a design-related task.
    
    Args:
        task_description: Description of the task to perform
        
    Returns:
        str: Result of the task execution
    """
    return run_task(task_description)
