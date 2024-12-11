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

def QuestionAnswer(questions,chat_log = None):
    FileLog = open("qna_log.txt","r")
    chat_log_template = FileLog.read()
    FileLog.close()

    if chat_log is None:
        chat_log = chat_log_template

    prompt = f'{chat_log}Question : {questions}\nAnswer : '
    response = completion.create(
        model = "text-davinci-002",
        prompt=prompt,
        temperature = 0, 
        max_tokens = 100,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0)
    answers = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f"\nQuestion : {questions} \nAnswer : {answers}"
    FileLog = open("qna_log.txt","w")
    FileLog.write(chat_log_template_update)
    FileLog.close()
    return answers

# while True:
#     kk= input("Enter : ")
#     print(QuestionAnswer(kk))
#     if "End this session" in kk :
#         break
#     else :
#         pass 
