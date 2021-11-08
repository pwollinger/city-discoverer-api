from fastapi import FastAPI
import pyowm
import os

app = FastAPI()
owm = pyowm.owm.OWM(os.environ['OW_API_KEY'])
mgr = owm.weather_manager()

@app.get("/city/")
def get_city_info(city_name: str):
    city_name = city_name.replace("_", " ")
    try:
        location_data = mgr.weather_at_place(city_name)
        wheather_data = location_data.weather
        return wheather_data.temperature(unit='celsius')
    except pyowm.commons.exceptions.NotFoundError:
        return {"Error": "City not found!"}