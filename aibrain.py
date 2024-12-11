# OpenAi
#API key
fileopen = open("api.txt","r")
API = fileopen.read()
fileopen.close()

#Improting 
import openai
from dotenv import load_dotenv

#Coding

openai.api_key = API
load_dotenv()
completion = openai.Completion()

def ReplyBrain(questions,chat_log = None):
    FileLog = open("chat_log.txt","r")
    chat_log_template = FileLog.read()
    FileLog.close()

    if chat_log is None:
        chat_log = chat_log_template

    prompt = f'{chat_log}You : {questions}\nOmnitrix : '
    response = completion.create(
        model = "text-davinci-002",
        prompt=prompt,
        temperature = 0.5, 
        max_tokens = 60,
        top_p = 0.3,
        frequency_penalty = 0.5,
        presence_penalty = 0)
    answers = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f"\nYou : {questions} \nOmnitrix : {answers}"
    FileLog = open("chat_log.txt","w")
    FileLog.write(chat_log_template_update)
    FileLog.close()
    return answers

# while True:
#     kk= input("Enter : ")
#     print(ReplyBrain(kk))
#     if "End this session" in kk :
#         break
#     else :
#         pass 