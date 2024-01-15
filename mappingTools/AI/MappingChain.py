# import os
# import openai
# from langchain import PromptTemplate
#
# os.environ["OPENAI_API_KEY"] = "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"
# os.environ['SERPER_API_KEY'] = "11257ca7c83f827ea4aba9da47523ae98a8226a3"
# from langchain.agents import AgentType, initialize_agent, load_tools
# from langchain_community.llms import OpenAI
#
# llm = OpenAI(temperature=0)
# tools = load_tools(["google-serper"], llm=llm)
# # prompt_template_url = PromptTemplate(input_variables=["company_name", "company_address"], template="""
# # search in google and give me the URL to the company's CAREERS page or website \
# # of {company_name} that located in {company_address} in Jerusalem. \
# # if the company has Israeli careers website give its URL \
# # This company name is the official one, it can be a little different (nickname) it can be English letters. \
# # In addition to this it can be at a different address. \
# # I want the career page but in case you can't find it \
# # Return the general website URL.\
# # important! Check if the URL exist and active  \
# # """)
# prompt_template_url = PromptTemplate(input_variables=["company_name", "company_address"], template="""
#   search for "" in "www.google.com" give me and load the first website address that you found
# """)
#
# query = prompt_template_url.format(company_name="https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite", company_address="חזון")
# self_ask_with_search = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True,
#                                         handle_parsing_errors=True, max_iterations=10)
# try:
#     self_ask_with_search.run(query)
# except openai.BadRequestError:
#     print("No answer")
# except Exception as e:
#     print(e)
#
# # llm = OpenAI(temperature=0)
# #
# # # The tools we'll give the Agent access to. Note that the 'llm-math' tool uses an LLM, so we need to pass that in.
# # tools = load_tools(["google-serper"], llm=llm)
# #
# # # Finally, let's initialize an agent with the tools, the language model, and the type of agent we want to use.
# # agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
# #
# # # Let's test it out!
# # agent.run("give me an active and existing url website of company 'ג'יי די סי אינטרנשיונל' ")
from langchain_community.utilities.tavily_search import TavilySearchAPIWrapper
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType, load_tools
from langchain import PromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI
import os

os.environ["TAVILY_API_KEY"] = "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"
os.environ["OPENAI_API_KEY"] = "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"
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

company_name = "יד שרה"
company_address = "שדרות הרצל 124"
prompt_template_url = PromptTemplate(input_variables=["company_name", "company_address"],
                                     template="""What the website link of  {company_name} company that located in {company_address} Israel?
     ### This company name is the official one, it can be a little different (nickname) it can be English letters. ###
     ### if you dont find eny website url that matches the official company name try to  find the  other name of the company and then search again for the url as before ### """)
query = prompt_template_url.format(company_name="א א ברזני", company_address = "ירושלים")
# run the agent
agent_chain.run(query)