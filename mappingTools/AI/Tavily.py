from langchain_community.utilities.tavily_search import TavilySearchAPIWrapper
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain import PromptTemplate
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

# Tavily
llm = ChatOpenAI(model_name="gpt-4-1106-preview", temperature=0)
search = TavilySearchAPIWrapper()
tavily_tool = TavilySearchResults(api_wrapper=search)

agent_chain = initialize_agent(
    [tavily_tool],
    llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)


def find_url(company_name, company_address):
    prompt_template_url = PromptTemplate(input_variables=["company_name", "company_address"],
                                         template="""
    What the website link of {company_name} company that located in {company_address} Israel?
    ### If there is an Israeli and/or Hebrew website - give the link to it. ###
    ### If you find the official website search inside the career page and give it as the result. ###
    ### This company name is the official one, it can be a little different (nickname) and it can be English letters. ###
    ### The URL should be the link to the official company website, do not give links to aggregators such as checkID and etc. ###
    ### in the final answer return just the url without any text, If you did not find a URL - return an empty string ###
    """)
    query = prompt_template_url.format(company_name=company_name, company_address=company_address)
    # run the agent
    result = agent_chain.run(query)
    return result


res = find_url("א ברקן ושות בעמ", "עם ועולמו, 3, ירושלים")
print(res)
