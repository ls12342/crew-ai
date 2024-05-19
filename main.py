from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from agents import AINewsLetterAgents
from tasks import AINewsLetterTasks

from dotenv import load_dotenv
load_dotenv()

# Initialize the agents and tasks
agents = AINewsLetterAgents()
tasks = AINewsLetterTasks()

# Initialize the Ollama LLama3 language model
LLama3 = ChatOpenAI(
    model = "llama3",
    base_url = "http://localhost:11434/v1"
)

# Instantiate the agents
news_fetcher = agents.news_fetcher_agent()
news_analyzer = agents.news_analyzer_agent()
fact_compiler = agents.compile_fact_check()

# Instantiate the tasks
fetch_news_task = tasks.fetch_news_task(news_fetcher)
# analyze_news_task = tasks.analyze_news_task(news_analyzer, [fetch_news_task])
# compile_newsletter_task = tasks.compile_fact_check_task(
#     fact_compiler, [analyze_news_task])

# Form the crew
crew = Crew(
    agents=[news_fetcher],
    tasks=[fetch_news_task],
    # process=Process.hierarchical,
    # manager_llm=LLama3,
    verbose=2
)

# Kick off the crew's work
results = crew.kickoff()

# Print the results
print("Crew Work Results:")
print(results)