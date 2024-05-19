import gradio as gr
import os
import streamlit as st
from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from agents import AINewsLetterAgents
from tasks import AINewsLetterTasks
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# TODO: 
# Add vector data base embedding for better result
# Add streamlit ui for better visualization
load_dotenv()

print(os.environ["GROQ_API_KEY"])
print(os.environ["OPENAI_MODEL_NAME"])
llm = ChatGroq(
        temperature=0, 
        groq_api_key = os.environ["GROQ_API_KEY"], 
        model_name= os.environ["OPENAI_MODEL_NAME"]
    )
    
# Initialize the agents and tasks
agents = AINewsLetterAgents()
tasks = AINewsLetterTasks()

# Initialize the Ollama LLama3 language model
# DolphinLLama3 = ChatOpenAI(
#     model = "dolphin-llama3",
#     base_url = "http://localhost:11434/v1"
# )

# Instantiate the agents
def buildCrew(query):
        news_fetcher = agents.news_fetcher_agent(query)
        news_analyzer = agents.news_analyzer_agent(query)
        fact_compiler = agents.compile_fact_check()
        fetch_news_task = tasks.fetch_news_task(news_fetcher, query)
        analyze_news_task = tasks.analyze_news_task(news_analyzer, [fetch_news_task], query)
        compile_fact_check_task = tasks.compile_fact_check_task(
        fact_compiler, [analyze_news_task])
        return Crew(
        agents=[news_fetcher, 
                news_analyzer,
                fact_compiler
            ],
        tasks=[fetch_news_task, analyze_news_task, compile_fact_check_task],
        process=Process.hierarchical,
        manager_llm=llm,
        llm=llm,
        verbose=10
    )
# Instantiate the tasks

# Form the crew


def crew_kickoff(query):
    # Build the crew with parameters
    crew = buildCrew(query)
    
    # Kick off the crew's work
    results = crew.kickoff()

    # Print the results
    print("Crew Work Results:")
    print(results)
    
iface = gr.Interface(
    fn=crew_kickoff,
    inputs=["text"],
    outputs="text",
    title="Fact Check Crew",
)

iface.launch()