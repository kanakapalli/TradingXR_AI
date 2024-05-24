import json
import os
import requests
from tool.tool import *
from tool.functions import *
import openai

openai.api_key = "sk-proj-"



def run_conversation(content):
    messages = [{"role": "user", "content": content}]

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )
    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls

    if tool_calls:
        messages.append(response_message)

        available_functions = {
            "get_news_sentiment": get_news_sentiment,
        }
        for tool_call in tool_calls:
            print(f"Function: {tool_call.function.name}")
            print(f"Params: {tool_call.function.arguments}")
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)
            print(function_args.get("limit", 1))
            function_response = function_to_call(
                api_key='D9FSHNEMC8Z5AWVR',
                tickers=function_args.get("tickers"),
                topics=function_args.get("topics"),
                time_from=function_args.get("time_from"),
                time_to=function_args.get("time_to"),
                sort=function_args.get("sort", 'LATEST'),
                limit=function_args.get("limit", 1)
            )
            print(f"API: {function_response}")
            messages.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": function_response,
                }
            )

        second_response = openai.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=messages,
            stream=True
        )
        return second_response

    return response_message

if __name__ == "__main__":
    question = ("tell me the hightst price of meta stock"
                ".")
    response = run_conversation(question)
    for chunk in response:
        print(chunk.choices[0].delta.content or "", end='', flush=True)
