import requests
import time
import config
import telebot

# Configura tu token de bot y el ID del chat

config.bot_token

bot_token = config.bot_token
chat_id = config.chat_id
message = config.message
##ciudad= config.ciudad
api_key= config.api_key
tiempoEspera = config.milesegundosCoins



# Configura la URL de la API de CoinGecko
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana,cardano&vs_currencies=usd"

# Configura el precio objetivo para las alertas
btc_target_price_up = config.btc_price_up # Cambia este valor al precio que desees para Bitcoin
btc_target_price_dow = config.btc_price_down

eth_target_price_up = config.eth_price_up # Cambia este valor al precio que desees para Ethereum
eth_target_price_down = config.eth_price_down


sol_target_price = config.sol_price # Cambia este valor al precio que desees para Solana
ada_target_price = config.ada_price # Cambia este valor al precio que desees para Cardano (ADA)




def get_crypto_prices():
    response = requests.get(url)
    data = response.json()
    return data["bitcoin"]["usd"], data["ethereum"]["usd"], data["solana"]["usd"], data["cardano"]["usd"]


def mensajePercioBTC(btc_precio,estado):

    print("5")
    
    
    if estado==True:

        p_btc = btc_precio
        message= f"Precio BTC UP {p_btc} $ actualmente. :D "

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

    elif estado==False:
        p_btc =str(btc_precio)
        message=f"Precio BTC DOWN {p_btc}$ actualmente. :D "

        url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
        params = {
            'chat_id': chat_id,
            'text': message
            
        }
        response = requests.post(url, params=params)
        if response.status_code == 200:
            print('Mensaje enviado exitosamente 5B!')
        else:
            print(f'Error al enviar el mensaje: {response.status_code}')


def mensajePercioETH(ETH_precio,estado):

    print("ETH")
    
    
    if estado==True:

        ##p_btc = eth_precio
        message= f"Precio ETH UP {ETH_precio} $ actualmente. :D "

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

    elif estado==False:
        

        message=f"Precio ETH DOWN {ETH_precio}$ actualmente. :D "

        url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
        params = {
            'chat_id': chat_id,
            'text': message
            
        }
        response = requests.post(url, params=params)
        if response.status_code == 200:
            print('Mensaje enviado exitosamente 5B!')
        else:
            print(f'Error al enviar el mensaje: {response.status_code}')








""" def mensajePercioBTC_UP(btc_precio):

    print("1")

    p_btc = btc_precio
    message= f"Precio BTC UP {p_btc} $ actualmente. :D "

    ##print(f"El precio actual de Bitcoin es: ${btc_price}")
    
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': message
        }
    response = requests.post(url, params=params)
    if response.status_code == 200:
        print('Mensaje enviado exitosamente!')
    else:
        print(f'Error al enviar el mensaje: {response.status_code}')

def mensajePercioBTC_DOWN(btc_precio):

    print("2")

    p_btc =str(btc_precio)
    message=f"Precio BTC DOWN {p_btc}$ actualmente. :D "

    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': message
        
    }
    response = requests.post(url, params=params)
    if response.status_code == 200:
        print('Mensaje enviado exitosamente!')
    else:
        print(f'Error al enviar el mensaje: {response.status_code}') """


def main():

    while True:

        btc_price, eth_price, sol_price, ada_price = get_crypto_prices()
        print(f"El precio actual de Bitcoin es: ${btc_price}")
        print(f"El precio actual de Ethereum es: ${eth_price}")
        print(f"El precio actual de Solana es: ${sol_price}")
        print(f"El precio actual de Cardano (ADA) es: ${ada_price}")

        print(f"Tarjet: {  btc_target_price_dow} $ y { btc_target_price_up} $" )
        
        if btc_price >= btc_target_price_up:
            print(f"¡Alerta! El precio de Bitcoin ha alcanzado o superado los ${btc_target_price_up}")
            ##mensajePercioBTC_UP(btc_price)
            mensajePercioBTC(btc_price, True)
            # Aquí puedes añadir código para enviar un correo electrónico, mensaje de texto, etc.
        
        if btc_price <= btc_target_price_dow:
            print(f"¡Alerta! El precio de Bitcoin ha perdido los ${btc_target_price_dow}")
            ##mensajePercioBTC_DOWN(btc_price)
            mensajePercioBTC(btc_price, False)
            # Aquí puedes añadir código para enviar un correo electrónico, mensaje de texto, etc.
        
        if eth_price >= eth_target_price_up:
            print(f"¡Alerta! El precio de Ethereum ha alcanzado o superado los ${eth_target_price_up}")
            # Aquí puedes añadir código para enviar un correo electrónico, mensaje de texto, etc.
            mensajePercioETH(eth_price,True)

        if eth_price <= eth_target_price_down:
            print(f"¡Alerta! El precio de Ethereum ha pertidido los ${eth_target_price_down}")
            # Aquí puedes añadir código para enviar un correo electrónico, mensaje de texto, etc.
            mensajePercioETH(eth_price,False)
        
        
        if sol_price >= sol_target_price:
            print(f"¡Alerta! El precio de Solana ha alcanzado o superado los ${sol_target_price}")
            # Aquí puedes añadir código para enviar un correo electrónico, mensaje de texto, etc.

        if ada_price >= ada_target_price:
            print(f"¡Alerta! El precio de Cardano (ADA) ha alcanzado o superado los ${ada_target_price}")
            # Aquí puedes añadir código para enviar un correo electrónico, mensaje de texto, etc.
        
        time.sleep(tiempoEspera)  # Espera 30 minutos antes de verificar nuevamente

if __name__ == "__main__":
    main()
    