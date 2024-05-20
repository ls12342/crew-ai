from fact_check_crew.main import runCrew
import streamlit as st


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
    col1, col2 = st.columns([1, 5])
    with col1:
        submitted = st.form_submit_button("Check Fact")
    with col2:
        submittedCancel = st.form_submit_button("Cancel")

    if submittedCancel:
        st.rerun()
    if submitted:
        st.text_area('')
        result = runCrew(api, model, fact)
        st.text_area(result)
