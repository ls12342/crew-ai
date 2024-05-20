import json
import os

import requests
from langchain.tools import tool


class SearchTools():

    @tool("Search the internet")
    def search_internet(query):
        """Useful to fetch news"""
        print("Searching the internet...")
        top_result_to_return = 5
        url = "https://google.serper.dev/search"
        payload = json.dumps(
            {"q": f"${query} stock price", "num": top_result_to_return, "tbm": "nws"})
        headers = {
            'X-API-KEY': os.environ['SERPER_API_KEY'],
            'content-type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print("Response:", response.json())
        # check if there is an organic key
        if 'organic' not in response.json():
            return "Sorry, I couldn't find anything about that, there could be an error with you serper api key."
        else:
            # return response.json()['organic']
            results = response.json()['organic']
            print("Results:", results)
            string = []
            if response.json().get('answerBox'):
                answer = response.json().get('answerBox')
                string.append('\n'.join([
                    f"Title: {answer['title']}",
                    f"Answer: {answer['answer']}",
                    f"Source: {answer['source']}",
                    "\n-----------------"
                ]))
            print("Results:", results[:top_result_to_return])
            for result in results[:top_result_to_return]:
                try:
                    # Attempt to extract the date
                    print(result)
                    date = result.get('date', 'Date not available')
                    string.append('\n'.join([
                        f"Title: {result['title']}",
                        f"Link: {result['link']}",
                        f"Link: {result['link']}",
                        f"Date: {date}",  # Include the date in the output
                        f"Snippet: {result['snippet']}",
                        "\n-----------------"
                    ]))
                except KeyError:
                    next

            return '\n'.join(string)
