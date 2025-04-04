from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

def get_weather():
    api_url = f"http://api.weatherapi.com/v1/current.json?key={os.getenv('api_key')}&q=Renton&aqi=no"

configure()
get_weather()