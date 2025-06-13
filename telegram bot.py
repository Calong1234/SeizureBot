import requests

TOKEN = "7960498642:AAEcTtsuVkY_mq3B0XuI3kcGlu5qwd6GS4c"
chat_id = "1707821396"

def prompt(seizureLevel):
    message = f"⚠️Alert!⚠️: Your likelihood of having a seizure is currently {seizureLevel}. \n\nPlease find a place to lie down and wait for help. \n\nSeizure helpbot: (website goes here)"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url).json()

prompt("99%")