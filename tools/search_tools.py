import json
import os
import requests
from crewai.tools import BaseTool

class SearchTool(BaseTool):
    def __init__(self):
        super().__init__(
            name="Internet Search",
            description="Searches the internet using Serper API for travel-related queries."
        )

    def _run(self, input: str) -> str:
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": input})
        headers = {
            'X-API-KEY': os.getenv('SERPER_API_KEY'),
            'Content-Type': 'application/json'
        }

        response = requests.post(url, headers=headers, data=payload)
        data = response.json()

        if 'organic' not in data or not data['organic']:
            return "Sorry, I couldn't find anything. Please check your SERPER API key or query."

        results = data['organic'][:4]
        output = []
        for result in results:
            try:
                output.append('\n'.join([
                    f"Title: {result['title']}",
                    f"Link: {result['link']}",
                    f"Snippet: {result['snippet']}",
                    "--------------"
                ]))
            except KeyError:
                continue

        return '\n'.join(output)