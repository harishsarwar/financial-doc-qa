from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def build_qa_engine(model="mistral"):
    llm = Ollama(model=model)
    template = """
    You are a financial assistant.
    Context: {context}
    Question: {question}
    Answer clearly and concisely.
    """
    prompt = PromptTemplate(input_variables=["context", "question"], template=template)
    return LLMChain(prompt=prompt, llm=llm)

def answer_question(chain, context, question):
    return chain.run(context=context, question=question)
