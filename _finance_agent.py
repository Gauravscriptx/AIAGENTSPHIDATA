import os
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API Key from .env
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize the model with the API key
agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile", api_key=groq_api_key),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    show_tool_calls=True,
    markdown=True,
    instructions=["use tables to display data."]
)

# Test the agent
agent.print_response("Summarize and compare analyst recommendations and fundamentals for TSLA and NVDA.")
