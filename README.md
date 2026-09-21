# Data Agent

A lightweight data workflow agent that routes user requests between ETL and SQL analysis pipelines. It uses LangGraph and Groq-backed LLMs to decide whether a task should be handled by the ETL analyst or SQL analyst, then executes the appropriate flow.

## Features

- API/data extraction workflow with ETL analysis
- SQL query generation and execution support
- Structured routing between task types
- CSV export into the `data/extract` folder
- Graph visualization for the agent workflow

## Project structure

- `agents/` — routing and specialist agents
- `data/` — input and extracted datasets
- `models/` — schema definitions
- `utils/` — database, ETL, and LLM helpers
- `main.py` — example entry point
- `feed_db.py` — database loading helper

## Requirements

- Python 3.14+
- A Groq API key configured through environment variables
- PostgreSQL database access if using SQL execution paths

## Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   If you use `uv`, you can also install from `pyproject.toml`:
   ```bash
   uv sync
   ```

3. Configure environment variables in a `.env` file:
   ```env
   GROQ_API_KEY=your_key_here
   ```

4. Run the example:
   ```bash
   python main.py
   ```

## Example usage

The included script sends a prompt to the agent to extract data from a public API endpoint and save it in the extract folder.

```python
from agents.data_agent import data_agent
from langchain_core.messages import HumanMessage

response = data_agent.invoke(
    {
        "messages": [
            HumanMessage(content="I want to extract the data from the API endpoint 'https://pokeapi.co/api/v2/pokemon' and save it to data/extract folder in the csv folder")
        ],
        "route_response": ""
    }
)

print(response)
```

## Notes

- The project expects a valid Groq key for LLM calls.
- Data and graph outputs are generated in local folders under `data/`.
- `.env` and local environment files are ignored via `.gitignore`.
