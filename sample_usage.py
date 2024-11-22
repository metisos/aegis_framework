from aegis_framework import MasterAIAgent, OllamaLocalModel

def test_without_llm():
    """Test the framework without an LLM model"""
    print("\n=== Testing without LLM ===")
    agent = MasterAIAgent(name="Basic Agent")
    
    # Test basic question answering
    question = "What is the meaning of life?"
    response = agent.answer_question(question)
    print(f"Question: {question}")
    print(f"Response: {response}\n")

def test_with_llm():
    """Test the framework with an Ollama LLM model"""
    print("\n=== Testing with Llama2 LLM ===")
    
    # Initialize the Ollama model with llama2
    llm = OllamaLocalModel(model="llama3.2")
    agent = MasterAIAgent(name="Llama2 Agent", llm=llm)
    
    # Test question answering with LLM
    questions = [
        "What are the three laws of robotics?",
        "Write a haiku about artificial intelligence.",
    ]
    
    for question in questions:
        print(f"\nQuestion: {question}")
        response = agent.answer_question(question)
        print(f"Response: {response}")

def main():
    print("=== Aegis Framework Sample Usage ===")
    
    # Test without LLM
    test_without_llm()
    
    # Test with Llama2
    test_with_llm()

if __name__ == "__main__":
    main()
