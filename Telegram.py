# telegram_functions.py
import requests

token = '' #Digite sua API
chat_id = '' #Digite o Id do seu chat

def send_message(msg):
    try:
        data = {"chat_id": chat_id, "text": msg}
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        requests.post(url, data)
    except Exception as e:
        print("Erro no sendMessage:", e)