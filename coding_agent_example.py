from aegis_framework import MasterAIAgent, OllamaLocalModel

def create_coding_agent():
    """Create an AI agent specialized for coding tasks"""
    # Initialize with llama3.2 which is good for coding
    llm = OllamaLocalModel(model="llama3.2")
    return MasterAIAgent(name="Code Assistant", llm=llm)

def demonstrate_coding_tasks():
    """Show various coding-related tasks the agent can help with"""
    print("=== AI Coding Assistant Demo ===\n")
    
    # Create our coding-specialized agent
    agent = create_coding_agent()
    
    # Example coding tasks
    coding_tasks = [
        "Write a Python function that implements binary search algorithm with detailed comments.",
        "Explain the difference between merge sort and quick sort, and provide an example implementation of merge sort.",
        "Create a simple REST API endpoint using Flask that accepts POST requests with JSON data.",
        "Write a unit test for a function that validates email addresses using regex.",
    ]
    
    # Process each task
    for i, task in enumerate(coding_tasks, 1):
        print(f"\n=== Task {i} ===")
        print(f"Request: {task}")
        print("\nResponse:")
        response = agent.answer_question(task)
        print(response)
        print("\n" + "="*50)

def interactive_mode():
    """Interactive mode where user can ask coding questions"""
    print("\n=== Interactive Coding Assistant Mode ===")
    print("Type 'exit' to quit\n")
    
    agent = create_coding_agent()
    
    while True:
        question = input("\nEnter your coding question: ")
        if question.lower() == 'exit':
            break
            
        print("\nThinking...")
        response = agent.answer_question(question)
        print(f"\nResponse:\n{response}")

def main():
    # Comment out the demonstration if you just want interactive mode
    # demonstrate_coding_tasks()
    
    # Run interactive mode
    interactive_mode()

if __name__ == "__main__":
    main()
