import os
from dotenv import load_dotenv
import streamlit as st


# TODO - Implement RAG
from crew import FactCheckCrew
load_dotenv()


def runCrew(api, model, fact):
    inputs = {
        'fact': fact,
    }
    return FactCheckCrew(api, model).crew().kickoff(inputs=inputs)


with st.form("fact_form"):
    st.write("Check the fact")
    model = st.sidebar.selectbox(
        'Choose a model',
        ['mixtral-8x7b-32768', 'llama3-8b-8192', 'gemma-7b-it']
    )
    api = st.sidebar.selectbox(
        'Choose an API',
        ['GROQ', 'Ollama']
    )
    st.title('CrewAI Fact Checker')
    fact = st.text_input(
        'Fact',
    )
    # Every form must have a submit button.
    submitted = st.form_submit_button("Check Fact")
    if submitted:
        st.text_area('')
        result = runCrew(api, model, fact)
        st.text_area(result)
