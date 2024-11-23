# Aegis Multi-Agent Framework



## Overview

The Aegis Multi-Agent Framework is a powerful, extensible platform for building and deploying AI agent systems with seamless local LLM integration. Designed for both researchers and developers, it provides a robust foundation for creating sophisticated multi-agent systems while maintaining simplicity and flexibility.

### Key Features

- **Modular Agent Architecture**
  - Plug-and-play agent components
  - Customizable agent behaviors
  - Extensible design patterns

- **Local LLM Integration**
  - Native Ollama support
  - Multiple model compatibility
  - Optimized inference pipeline

- **Advanced Task Management**
  - Real-time task monitoring
  - Parallel task execution
  - Priority-based scheduling

- **Performance Analytics**
  - Built-in metrics tracking
  - Performance optimization tools
  - Detailed execution logs

## Quick Start

### Installation

```bash
# Basic installation
pip install aegis-framework

# With web interface support
pip install aegis-framework[web]
```

### Basic Usage

```python
from aegis_framework import MasterAIAgent, DesignAgent

# Initialize a master agent
agent = MasterAIAgent(
    model="gemma2:9b",
    temperature=0.7,
    max_tokens=2048
)

# Generate responses
response = agent.answer_question("Explain the concept of emergent behavior in multi-agent systems.")
print(response)

# Create a specialized design agent
designer = DesignAgent(model="codellama")
design = designer.generate_new_design(
    context="Create a microservices architecture",
    constraints=["scalability", "fault-tolerance"]
)
print(design)
```

## Creating Custom Agents

```python
from aegis_framework import MasterAIAgent
from typing import Dict, List, Optional

class DataAnalysisAgent(MasterAIAgent):
    def __init__(
        self, 
        model: str = "codellama",
        custom_tasks: Optional[Dict[str, List[str]]] = None
    ):
        super().__init__(model=model)
        
        # Define specialized tasks
        self.agent_task_map.update({
            "data_analysis": [
                "analyze data",
                "statistical analysis",
                "data visualization",
                "hypothesis testing"
            ]
        })
        
        # Add custom tasks if provided
        if custom_tasks:
            self.agent_task_map.update(custom_tasks)
    
    def analyze_data(
        self, 
        data: str,
        analysis_type: str = "comprehensive",
        confidence_level: float = 0.95
    ) -> Dict[str, any]:
        """
        Perform data analysis with specified parameters.
        
        Args:
            data: Input data for analysis
            analysis_type: Type of analysis to perform
            confidence_level: Statistical confidence level
            
        Returns:
            Dictionary containing analysis results
        """
        prompt = self._construct_analysis_prompt(
            data=data,
            analysis_type=analysis_type,
            confidence_level=confidence_level
        )
        return self.generate_structured_response(prompt)

# Usage example
analyst = DataAnalysisAgent(model="codellama:13b")
results = analyst.analyze_data(
    data="your_data_here",
    analysis_type="statistical",
    confidence_level=0.99
)
```

## System Requirements

### Core Requirements
- Python 3.7+
- Ollama (for local LLM support)
- 8GB+ RAM (recommended)
- CUDA-compatible GPU (optional, for enhanced performance)

### Optional Dependencies
- **Web Interface**
  - Flask >= 2.0.0
  - Flask-SocketIO >= 5.0.0
  - Eventlet >= 0.30.0

- **Enhanced Features**
  - fuzzywuzzy >= 0.18.0 (text matching)
  - sqlite3-api >= 3.0.0 (database integration)
  - numpy >= 1.19.0 (numerical operations)
  - pandas >= 1.3.0 (data handling)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact & Support

- **Author**: Metis Analytics
- **Email**: cjohnson@metisos.com
- **GitHub Issues**: [Report a bug](https://github.com/metisos/aegis_framework/issues)


## Acknowledgments

Special thanks to:
- The Ollama team for their excellent LLM runtime
- Our contributors and early adopters
- The open-source AI community

---

<div align="center">
Made with ❤️ by Metis Analytics
</div>
