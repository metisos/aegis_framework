"""
Example demonstrating the use of the DesignAgent to generate new agent designs.
"""

from aegis_framework import OllamaLocalModel
from aegis_framework.core.design_agent import DesignAgent

def main():
    # Initialize the design agent with custom models (optional)
    design_model = OllamaLocalModel(model="llama2:13b")
    review_model = OllamaLocalModel(model="llama2:13b")
    
    agent = DesignAgent(
        design_model=design_model,
        review_model=review_model,
        design_interval=3600  # Generate designs every hour
    )
    
    # Generate a single new design
    print("Generating a new agent design...")
    result = agent.generate_new_design()
    print(result)
    
    # Start periodic design generation
    print("\nStarting periodic design generation...")
    agent.start_periodic_design()
    
    try:
        # Let it run for a while (5 minutes in this example)
        import time
        time.sleep(300)
    except KeyboardInterrupt:
        print("\nStopping periodic design generation...")
    finally:
        # Stop periodic generation
        agent.stop_periodic_design()

if __name__ == "__main__":
    main()
