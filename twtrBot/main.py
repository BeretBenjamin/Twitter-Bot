import random
import time
import requests
import tweepy
from bs4 import BeautifulSoup
import keys
from gas_lookup import *


def tweet(message, media_path):
    client = tweepy.Client(keys.bearer_token, keys.api_key, keys.api_secret, keys.access_token,
                           keys.access_token_secret)
    auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret, keys.access_token, keys.access_token_secret)
    api = tweepy.API(auth)

    media = api.media_upload(media_path)
    client.create_tweet(text=message, media_ids=[media.media_id])

    print("Tweeted successfully")


if __name__ == "__main__":
    # tweet("Badea Vlad Stefan din Brasov este homo")
    # monitor_gas_prices()

    word_list = ['Uau!', 'Fenomenal!', 'Remarcabil!', 'Uimitor!',
                 'Formidabil!', 'Miraculos!', 'Excepțional!', 'Remarcant!',
                 'Neașteptat!', 'Fabulos!', 'Uluitor!', "Impresionant!", 'Neobișnuit!',
                 'Minunat!', 'Fantastic!', 'Uluitor!', 'Șocant!', 'Neprevăzut!', 'Neașteptat!']

    # URL of the webpage containing the fuel prices
    url = "https://ro.fuelo.net/prices/date/2024-03-01?lang=en"

    # Get the gasoline and diesel prices of Petrom



    while True:
        user_input = input("Enter 'exit' to stop: ")
        if user_input == 'exit':
            break
        else:
            print("You entered:", user_input)
        gasoline_prices, diesel_prices, gasoline_premium, diesel_premium, lpg_prices = get_petrom_prices(url)
        benzina = ''
        diesel = ''

        for station, price in gasoline_prices.items():
            benzina += f"{station}: {price} RON | "

        for station, price in diesel_prices.items():
            diesel += (f"{station}: {price} RON | ")

        random_nr = random.randint(0, 19)
        random_image = random.randint(1, 5)
        message = word_list[random_nr] + " " + "Acestea sunt ultimele preturi la benzina standard : \n" + benzina
        media_path = f"{random_image}.jpg"
        tweet(message, media_path)
        time.sleep(1800)
