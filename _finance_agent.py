import os
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
def get_company_symbol(company: str) -> str:
      symbols = {
        "Phidata": "MSFT",
        "Infosys": "INFY",
        "Tesla": "TSLA",
        "Apple": "AAPL",
        "Microsoft": "MSFT",
        "Amazon": "AMZN",
        "Google": "GOOGL",
       }
      return symbols.get(company,"Unknown")
# Get API Key from .env
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize the model with the API key
agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile", api_key=groq_api_key),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True), get_company_symbol],
    show_tool_calls=True,
    markdown=True,
    instructions=["use tables to display data.", "If you need to find the symbol for a company, use the get_company_symbol tool."]
)

# Test the agent
agent.print_response("Summarize and compare analyst recommendations and fundamentals for TSLA and NVDA.")
