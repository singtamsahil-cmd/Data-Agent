from ast import main

from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

def pick_llm(level: str):
    """
    Pick the appropriate LLM (Language Model) based on the specified level.

    Args:
        level (str): The level of the LLM to pick. It can be one of the following:
            - "easy": Picks the basic LLM.
            - "medium": Picks the advanced LLM.
            - "high": Picks the expert LLM.

    Returns:
        str: The name of the picked LLM.
    """

    if level.lower() == "low":
        llm = ChatGroq(model = "openai/gpt-oss-20b",temperature = 0,reasoning_effort="low")
    elif level.lower() == "medium":
        llm = ChatGroq(model = "qwen/qwen3.8-27b",temperature = 0,reasoning_effort= "low")
    elif level.lower() == "high":
        llm = ChatGroq(model = "openai/gpt-oss-120b",temperature = 0,reasoning_effort= "low")
    else:
        raise ValueError("Invalid level specified. Please choose from 'low', 'medium', or 'high'.")

    return llm

if __name__ == "__main__":
    llm_obj = pick_llm("low")
    print(llm_obj.invoke("what is the capital of France?"))
