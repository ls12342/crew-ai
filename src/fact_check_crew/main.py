import os
import argparse
import streamlit as st
from dotenv import load_dotenv
from crew import FactCheckCrew
load_dotenv()

# TODO - Implement RAG


def runCrew(api, model, fact):
    inputs = {
        'fact': fact,
    }
    return FactCheckCrew(api, model).crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--api", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--fact", required=True)
    args = parser.parse_args()

    runCrew(args.api, args.model, args.fact)
