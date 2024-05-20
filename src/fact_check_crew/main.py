import os
from dotenv import load_dotenv
import streamlit as st
from crew import FactCheckCrew
load_dotenv()

# TODO - Implement RAG


def runCrew(api, model, fact):
    inputs = {
        'fact': fact,
    }
    return FactCheckCrew(api, model).crew().kickoff(inputs=inputs)
