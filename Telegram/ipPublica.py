import requests
import config
import time


# Configura tu token de bot y el ID del chat

config.bot_token

bot_token = config.bot_token
chat_id = config.chat_id
message = config.message
##ciudad= config.ciudad
api_key= config.api_key
tiempoEspera = config.milesegundosIp

def obtener_ip_publica():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        if response.status_code == 200:
            ip = response.json().get('ip')
            return ip
        else:
            print("Error al obtener la IP pública.")
    except requests.RequestException as e:
        print(f"Error de conexión: {e}")



def enviarTelegram():

    print("5")
    ip_publica
          
    
    message= f"Tu ip pública actualmente es: "+ ip_publica 

    ##print(f"El precio actual de Bitcoin es: ${btc_price}")
    
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': message
        }
    response = requests.post(url, params=params)
    if response.status_code == 200:
        print('Mensaje enviado exitosamente 5A!')
    else:
        print(f'Error al enviar el mensaje: {response.status_code}')


if __name__ == "__main__":
    
    ip_publica = obtener_ip_publica()
    print(type(ip_publica))
    ip_publica_old = ip_publica 

    while True:

        if ip_publica == ip_publica_old:
            print(f"Tu dirección IP pública es: {ip_publica}")
            enviarTelegram()
            
        elif ip_publica != ip_publica_old:
            print("la ip ha cambiado")
            enviarTelegram()

    
        time.sleep(tiempoEspera)## milesegundos
        