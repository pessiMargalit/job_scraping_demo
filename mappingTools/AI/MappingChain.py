from langchain.agents import load_tools, initialize_agent, AgentType
from langchain.llms import OpenAI
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

llm = OpenAI(temperature=0, model_name='gpt-3.5-turbo')
tools = load_tools(["google-serper"], llm=llm)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
url_search_prompt = "Give me the URL to the career page on the official company website," \
                    " of המנסרים ביהלום בעמ located in צפרירים 16 ירושלים. " \
                    "This company name is the official one, it can be a little different (nickname) " \
                    "it can be English letters." \
                    " I want the career page but in case you can't find it," \
                    " then bring me the first result according to the following list:" \
                    " 1. URL to the official website " \
                    " 2. URL for careers on LinkedIn or Facebook when the previous results" \
                    " were not found and the careers are only on LinkedIn or Facebook. " \
                    "3. 'No Website'- when the previous results were not found and there is no website but the company is active 5." \
                    " 'The company is inactive'- when the previous results were not found and the company is inactive."
agent.run(url_search_prompt)
