#!/usr/bin/env python3
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os

authenticator = IAMAuthenticator('your-api-key-here')  # Replace with your API key
assistant = AssistantV2(
    version='2023-06-07',
    authenticator=authenticator
)

assistant.set_service_url('YOUR_SERVICE_URL')  # Replace with your service URL

session_id = assistant.create_session(
    assistant_id='YOUR_ASSISTANT_ID'  # Replace with your assistant ID
).get_result()['session_id']

user_prompt = ""
count = 0

print("$" * 48)
print("[Terminal Watson] -- (V2.2) -- {Engine ID: IBM Watson}")
print("Updated 06/07/2023 | <Programmed by GTAI.io> ")
print("*" * 48)
print("[NOTE]: To QUIT the program, enter  '-1'")
print("*" * 48)
print(" ")
print("Welcome to GTAI's [Terminal Watson]...")
print(" ")

while user_prompt != "-1":
    count = count + 1
    print("◌ Prompt " + str(count) + " ◌")
    print("[Terminal Watson]: Enter your PROMPT below...")
    user_prompt = input("      [User]: » ")
    if user_prompt != "-1":
        response = assistant.message(
            assistant_id='YOUR_ASSISTANT_ID',  # Replace with your assistant ID
            session_id=session_id,
            input={
                'message_type': 'text',
                'text': user_prompt
            }
        ).get_result()
        print("[Tm Watson]: " + response['output']['generic'][0]['text'] + "\n" + "-"*48)

if user_prompt == "-1":
    print("[Tm Watson]:" + "\n" + "NO DATA or a NEGATIVE value was entered by the user. TerminalWatson [GTAI.io, V2.1] will now quit.")
