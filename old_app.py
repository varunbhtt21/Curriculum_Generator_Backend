# https://github.com/amrrs/chatgpt-api-python/blob/main/ChatGPT_API_in_Python.ipynb
# https://medium.com/geekculture/a-simple-guide-to-chatgpt-api-with-python-c147985ae28

import openai
import os
from dotenv import load_dotenv
from prompts import lessonPlan, weekPlan, dayPlan, systemPrompt,sp,xy,gf,ulp

load_dotenv()

# Load your OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")
import requests


messages = [
        {"role": "system", "content": ulp},
    ]

def savingToFile(fileName,fileContent):
    # Open file in write mode
    with open(fileName, "w") as file:
        file.write(fileContent)


def callChatGPTAPI(userMessage, systemPrompt, fileName):
    messages[0]["content"] = systemPrompt
    while True:
        if userMessage:
            messages.append(
                {"role": "user", "content": userMessage},
            )
            chat = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=messages
            )
            gptOutputResponse = chat.choices[0].message.content
            messages.append({"role": "assistant", "content": gptOutputResponse})

            savingToFile(fileName,gptOutputResponse)
            userMessage = input("Enter your message : ")

            userMessage += "\n Before giving the final output, ask any clarification question in pointers that you might need to improve the quality of the output."



def generatingLessonPlan():
    # Getting the Lesson Plan and Setting the Dynamic Parameter
    lessonPlan.format(numberOfHours=320, teachingStack="node" )

    userMessage = '''
            Course Subject : Database
            Course Duration : 10 weeks
            Course Type : skill based
            Specific Course Goals : Certification
            Target Audience : Frontend Developer
            Current Skill Level : Graduates
            Prior Knowledge : HTML/CSS/Advance JS/React

            Before giving the final output, ask any clarification question in pointers that you might need to improve the quality of the output.


    '''
    
    callChatGPTAPI(userMessage, ulp, "lessonPlan1.md")


def generatingWeekPlan():
    # Getting the Lesson Plan and Setting the Dynamic Parameter
    weekPlan.format(sessionHours=2.5)

    userMessage = input("User : ") # User Input
    callChatGPTAPI(userMessage, weekPlan, "weekPlan2.md")

def generateDayPlan():

    while True:
        userInput = input("Enter your message : ")
        messages.append(
                {"role": "user", "content": userInput},
        
            )
        chat = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=messages, temperature=0.3
            )

        gptOutput = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": gptOutput})

        savingToFile("fileName10.md",gptOutput)
    

if __name__ == '__main__':
    # generatingWeekPlan()
    generatingLessonPlan()
    # generateDayPlan()
