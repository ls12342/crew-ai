import os
import argparse
from dotenv import load_dotenv
import streamlit as st
from crew import FactCheckCrew
load_dotenv()

# TODO - Implement RAG


def runCrew(api, model, company_name):
    inputs = {
        'company_name': company_name,
    }
    return FactCheckCrew(api, model).crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--api", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--company_name", required=True)
    args = parser.parse_args()

    runCrew(args.api, args.model, args.company_name)
