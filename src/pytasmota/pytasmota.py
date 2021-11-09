import requests
import json

class Tasmota:

    def __init__(self, host, id):
        self.host = host
        self.id = id

    def on(self):
        return requests.get(f"http://{self.host}/cm?cmnd=Power{self.id}%20On")

    def off(self):
        return requests.get(f"http://{self.host}/cm?cmnd=Power{self.id}%20Off")

    @property
    def is_on(self):
        response = requests.get(f"http://{self.host}/cm?cmnd=Power{self.id}")
        return(json.loads(response.text)[f"POWER{self.id}"] == "ON")

    @property
    def is_off(self):
        return not self.is_on
