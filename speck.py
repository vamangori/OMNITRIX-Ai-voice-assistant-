# Speck functions - TWO
# Windoes Based - pip install pyttsx3
# Chrome Based - pip install selenium==4.1.3

#Windows Based
#--> Advantages = Fast , Offline 
#--> Disadvantages = Overcut , Less Voices

import pyttsx3
def Speak(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voices",voices[0].id)
    engine.setProperty("rate",170)
    print("")
    print(f"You : {Text}.")
    print("")
    engine.say(Text)
    engine.runAndWait()

# Chrome Based 
#--> Advantages = More Voices , More Clear , Overspeking 
#--> Disadvantages = Word Limit , Slow

# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from time import sleep

# chrome_options = Options()
# chrome_options.add_argument('--log-level=3')
# chrome_options.headless = True
# Path = "DataBase\\chromedriver.exe"
# driver =  webdriver.Chrome(Path,options=chrome_options)
# driver.maximize_window()

# website = r"https://ttsmp3.com/text-to-speech/British%20English/"
# driver.get(website)
# ButtonSelection = Select(driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/form/select'))
# ButtonSelection.select_by_visible_text('British English / Brian')

# def Speak(Text):
#     lengoftext = len(str(Text))
#     if lengoftext ==0:
#         pass
#     else:
#         print("")
#         print(F"AI : {Text}.")
#         print("")
#         Data = str(Text)
#         xpathofsec = '/html/body/div[4]/div[2]/form/textarea'
#         driver.find_element(By.XPATH,value=xpathofsec).send_keys(Data)
#         driver.find_element(By.XPATH,value='//*[@id="vorlesenbutton"]').click()
#         driver.find_element(By.XPATH,value='/html/body/div[4]/div[2]/form/textarea').clear

#         if lengoftext>=30:
#             sleep(4)
#         elif lengoftext>=40:
#             sleep(6)
#         elif lengoftext>=55:
#             sleep(8)
#         elif lengoftext>=70:
#             sleep(10)
#         elif lengoftext>=100:
#             sleep(13)
#         elif lengoftext>=120:
#             sleep(15)
#         else:
#             sleep(2)


# Speak("hello master , How can i help you? ")