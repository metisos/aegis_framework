# Aegis Multi-Agent Framework

A powerful, extensible platform for building and deploying AI agent systems with seamless local LLM integration.

## Overview

The Aegis Multi-Agent Framework provides a robust foundation for creating sophisticated multi-agent systems while maintaining simplicity and flexibility. Perfect for both researchers and developers looking to build advanced AI agent applications.

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

## Quick Start

### Installation

```bash
pip install aegis-framework
```

### Basic Usage

```python
from aegis_framework import MasterAIAgent, DesignAgent
import os
from datetime import datetime

# Initialize a master agent
agent = MasterAIAgent(model="llama2:13b")

# Get user input for the question
user_question = input("Enter your question: ")

# Generate responses
response = agent.answer_question(user_question)
print("\nResponse:", response)

# Create a specialized design agent
designer = DesignAgent(model="llama2:13b")

# Get user input for design context
context = input("\nEnter design context: ")

# Generate the design
design = designer.generate_new_design(context=context)

# Create README content
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
readme_content = f"""# AI Agent Design - {timestamp}

## Design Context
{context}

## Design Details
- Class Name: {design['class_name']}
- Generated: {timestamp}

## Design Content
"""

# Add the original design content
with open(design['path'], 'r') as f:
    readme_content += f.read()

# Save as README in current directory
readme_path = os.path.join(os.path.dirname(__file__), f'README_{timestamp}.md')
with open(readme_path, 'w') as f:
    f.write(readme_content)

print(f"\nDesign saved to: {readme_path}")

```

## Creating Custom Agents

```python
from aegis_framework import MasterAIAgent
from typing import Dict, Any, Optional

class DataAnalysisAgent(MasterAIAgent):
    def __init__(
        self,
        model: str = "gemma2:9b",
        custom_tasks: Optional[Dict[str, List[str]]] = None
    ):
        super().__init__(model=model)
        
        # Add specialized tasks
        self.agent_task_map.update({
            "data_analysis": [
                "analyze data",
                "statistical analysis",
                "trend analysis",
                "data visualization"
            ]
        })
        
        if custom_tasks:
            self.agent_task_map.update(custom_tasks)
    
    def analyze_data(
        self,
        data: str,
        analysis_type: str = "comprehensive"
    ) -> Dict[str, Any]:
        """Perform data analysis with specified parameters."""
        prompt = f"Analyze this {analysis_type} data: {data}"
        return self.perform_task(prompt)

# Usage
analyst = DataAnalysisAgent()
results = analyst.analyze_data(
    data="your_data_here",
    analysis_type="statistical"
)
```

## System Requirements

- Python 3.7+
- Ollama (for local LLM support)
- 8GB+ RAM (recommended)
- CUDA-compatible GPU (optional)

## Example Scripts

The framework includes several example scripts to help you get started:

1. `basic_usage.py`: Demonstrates core functionality
2. `design_agent_example.py`: Shows advanced design capabilities
3. `custom_agent_example.py`: Illustrates custom agent creation

Run any example with the `--help` flag to see available options:
```bash
python examples/basic_usage.py --help
```

## Version History

Current Version: 0.1.15

Key Updates:
- Enhanced local LLM integration
- Improved design agent capabilities
- Better error handling
- More comprehensive examples

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- **Author**: Metis Analytics
- **Email**: cjohnson@metisos.com
- **GitHub Issues**: [Report a bug](https://github.com/metisos/aegis_framework/issues)

## Acknowledgments

Special thanks to:
- The Ollama team for their excellent LLM runtime
- Our contributors and early adopters
- The open-source AI community

---

Made with ❤️ by Metis Analytics
