from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

## web search agent
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
    # role='get financial data',
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,company_news=True)],
    show_tool_calls=True,
    # description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
    instructions=["Use tables to display the data"],
    markdown=True
)

multi_ai_agent = Agent(
    team=[web_search_agent, financial_agent],
    instructions=["Always include sources","Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent.print_response("Summarize analyst recommendations and share the latest news for NVDA",stream=True)