import gradio as gr
import os
import streamlit as st
from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from agents import AINewsLetterAgents
from tasks import AINewsLetterTasks
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

# TODO:
# Add vector data base embedding for better result
# https: // www.youtube.com/watch?v = iJjSjmZnNlI


def buildCrew(query, llm):
    agents = AINewsLetterAgents()
    tasks = AINewsLetterTasks()
    news_fetcher = agents.news_fetcher_agent(query)
    news_analyzer = agents.news_analyzer_agent(query)
    fact_compiler = agents.compile_fact_check()
    fetch_news_task = tasks.fetch_news_task(news_fetcher, query)
    analyze_news_task = tasks.analyze_news_task(
        news_analyzer, [fetch_news_task], query)
    compile_fact_check_task = tasks.compile_fact_check_task(
        fact_compiler, [analyze_news_task], query)
    return Crew(
        agents=[
            news_fetcher,
            news_analyzer,
            fact_compiler
        ],
        tasks=[fetch_news_task, analyze_news_task, compile_fact_check_task],
        process=Process.hierarchical,
        manager_llm=llm,
        llm=llm,
        verbose=10
    )


def crew_kickoff(api, model, query):
    print('API:', api)
    print('Model:', model)
    print('Query:', query)
    if api == "ollama":
        llm = ChatOpenAI(
            model=model,
            base_url="http://localhost:11434/v1"
        )
    if api == "groq":
        print(os.environ["GROQ_API_KEY"])
        llm = ChatGroq(
            temperature=0,
            model_name=model
        )

    # Build the crew with parameters
    crew = buildCrew(query, llm)
    results = crew.kickoff()
    print("Crew Work Results:")
    print(results)
    return results


iface = gr.Interface(
    fn=crew_kickoff,
    inputs=[
        gr.Radio(["ollama", "groq"], label="API"),
        gr.Dropdown(
            ['wizardlm2', 'gemma', 'gemma-7b-it', 'mixtral-8x7b-32768'],
            value=['wizardlm2', 'gemma', 'gemma-7b-it', 'mixtral-8x7b-32768'],
            multiselect=False,
            label="Model",
        ),
        gr.Textbox(label="Fact")
    ],
    outputs="text",
    title="Fact Check Crew",
)

iface.launch()
