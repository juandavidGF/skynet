# from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain

from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model_name="gpt-3.5-turbo", n=2, best_of=2)

template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

llm = ChatOpenAI()

llm_chain = LLMChain(prompt=prompt, llm=llm)

question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"

response = llm_chain.run(question)

print(response)


