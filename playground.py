import openai
from phi.agent import Agent
import phi.api
from phi.model.openai import OpenAIChat
import phi.playground
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
from phi.model.groq import Groq
import os
import phi
from phi.playground import Playground,serve_playground_app

load_dotenv()

phi.api=os.getenv("PHI_API_KEY")

web_search_agent = Agent(
    name='Web Search Agent',
    role='search the web for the informaton',
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    # description="You are a web search agent that searches the web for information.",
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True
)

## financial agent
financial_agent = Agent(
    name='Financial AI Agent',
    role='get financial data',
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,company_news=True)],
    show_tool_calls=True,
    # description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
    instructions=["Use tables to display the data"],
    markdown=True
)

app=Playground(agents=[web_search_agent,financial_agent]).get_app()

if __name__ == '__main__':
    serve_playground_app("playground:app",reload=True)

