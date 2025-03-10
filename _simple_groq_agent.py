import os
from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API Key from .env
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize the model with the API key
agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile", api_key=groq_api_key)
)

# Test the agent
agent.print_response("Write a 2-sentence poem about the love between dogs and samosas.")
