import streamlit as st
#from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain, HuggingFaceHub
import os
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

st.title('🦜🔗 Quickstart App')

def generate_response(question):
    template = """Question: {question}

    Answer:"""
    prompt = PromptTemplate(
            template=template,
        input_variables=['question']
    )
    repo_id = "bigscience/bloom"  
    llm=HuggingFaceHub(repo_id=repo_id, model_kwargs={"temperature":1e-10})
    llm_chain = LLMChain(llm=llm, prompt=prompt)
    answer = llm_chain.run(question).split('\n')[0]
    st.info(answer)



with st.form('my_form'):
    text = st.text_area('Enter your question:', 'who was founded Facebook?')
    submitted = st.form_submit_button('Submit')
    if submitted:
        generate_response(text)


"""
openai_api_key = st.sidebar.text_input('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')



def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)

"""

