# Project: Financial Agent

This project is a Python-based platform designed to integrate multiple agents for different tasks, such as web searching, financial data analysis, and more. It leverages tools like OpenAI, Groq, and DuckDuckGo to perform diverse operations efficiently.

## Requirements

- **Programming Language:** Python 3.8+
- **Libraries:** Listed in `requirements.txt`
- **Environment Variables:** Must be set in a `.env` file for API access keys.

### Tools and Libraries Used:
1. **phidata**: For managing agents and APIs.
2. **python-dotenv**: For loading environment variables.
3. **yfinance**: To fetch financial data.
4. **duckduckgo-search**: For web searching capabilities.
5. **fastapi**: To build the web application.
6. **uvicorn**: ASGI server to run the application.
7. **groq**: Advanced model integration.
8. **openai**: OpenAI API for various AI tasks.

## Getting Started

### Step 1: Clone the Repository
```bash
# Clone the repository
git clone https://github.com/SAYANdasAi/Financial-Agent
cd Financial-Agent
```

### Step 2: Create a Virtual Environment
It is recommended to use a virtual environment to isolate dependencies.

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### Step 3: Install Requirements

```bash
# Install required libraries
pip install -r requirements.txt
```

### Step 4: Set Up the `.env` File
Create a `.env` file in the root directory with the following keys:

```
PHI_API_KEY="your_phi_api_key"
GROQ_API_KEY="your_groq_api_key"
OPENAI_API_KEY="your_openai_api_key"
```

Replace the placeholder values with your actual API keys.

### Step 5: Run the Application

```bash
# Run the app
python playground.py
```

The application will start, and you can interact with the agents via the provided interface.

## Key Features

- **Web Search Agent:**
  - Uses DuckDuckGo to fetch information from the web.
  - Always includes sources in its results.

- **Financial AI Agent:**
  - Retrieves stock prices, analyst recommendations, and company news.
  - Displays data in table format for better visualization.

- **Modular and Scalable:**
  - Additional agents can be added as required.

## Future Plans
- Integrate more advanced tools for agent tasks.
- Add more visualizations and a refined UI.
- Expand the agent capabilities for broader applications.

---

**Enjoy using the Financial Agent!**
