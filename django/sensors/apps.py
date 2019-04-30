from django.apps import AppConfig
import requests


class SensorsConfig(AppConfig):
  name = 'sensors'

  def getSensorData (self, IP):
    response = requests.get('http://'+str(IP))
    return response.status_code

