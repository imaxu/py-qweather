# coding: utf-8
from pyqweather import QWeatherPackBase
from pyqweather.packages.weather.weather_now import WeatherNowRequest, WeatherNowResponse

class QWeatherWeatherPack(QWeatherPackBase):
  
  _URL = 'https://api.qweather.com/v7'
  
  def weather_now(self, location, lang:str='zh-hans', unit:str='m'):
    """实时天气"""
    req = WeatherNowRequest(location=location,lang=lang, unit=unit)
    data = req.with_url(self.get_conf().domain).with_credential(self.get_conf().get_credential()).get()
    return WeatherNowResponse(**data)