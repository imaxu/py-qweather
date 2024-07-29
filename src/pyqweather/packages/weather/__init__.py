# coding: utf-8
from pyqweather import QWeatherPackBase
from pyqweather.packages.weather.weather_now import WeatherNowRequest, WeatherNowResponse
from pyqweather.packages.weather.weather_daily import WeatherDailyRequest, WeatherDailyResponse
from pyqweather.packages.weather.weather_hourly import WeatherHourlyRequest, WeatherHourlyResponse



class QWeatherWeatherPack(QWeatherPackBase):
  
 
  def weather_now(self, location, lang:str='zh-hans', unit:str='m'):
    """实时天气"""
    req = WeatherNowRequest(location=location,lang=lang, unit=unit)
    data = req.with_url(self.get_conf().endpoint).with_credential(self.get_conf().get_credential()).get()
    return WeatherNowResponse(**data)
  
  
  def weather_3d(self, location, lang:str='zh-hans', unit:str='m'):
    """3日天气"""
    req = WeatherDailyRequest(day_range='3d', location=location,lang=lang, unit=unit)
    data = req.with_url(self.get_conf().endpoint).with_credential(self.get_conf().get_credential()).get()
    return WeatherDailyResponse(**data)
  
  
  def weather_7d(self, location, lang:str='zh-hans', unit:str='m'):
    """7日天气"""
    req = WeatherDailyRequest(day_range='7d', location=location,lang=lang, unit=unit)
    data = req.with_url(self.get_conf().endpoint).with_credential(self.get_conf().get_credential()).get()
    return WeatherDailyResponse(**data)
  
  
  def weather_10d(self, location, lang:str='zh-hans', unit:str='m'):
    """10日天气"""
    req = WeatherDailyRequest(day_range='10d', location=location,lang=lang, unit=unit)
    data = req.with_url(self.get_conf().endpoint).with_credential(self.get_conf().get_credential()).get()
    return WeatherDailyResponse(**data)
  
  
  def weather_10d(self, location, lang:str='zh-hans', unit:str='m'):
    """15日天气"""
    req = WeatherDailyRequest(day_range='15d', location=location,lang=lang, unit=unit)
    data = req.with_url(self.get_conf().endpoint).with_credential(self.get_conf().get_credential()).get()
    return WeatherDailyResponse(**data)
  
  
  def weather_30d(self, location, lang:str='zh-hans', unit:str='m'):
    """30日天气"""
    req = WeatherDailyRequest(day_range='30d', location=location,lang=lang, unit=unit)
    data = req.with_url(self.get_conf().endpoint).with_credential(self.get_conf().get_credential()).get()
    return WeatherDailyResponse(**data)
  
  
  def weather_24h(self, location, lang:str='zh-hans', unit:str='m'):
    req = WeatherHourlyRequest(hour_range='24h', location=location,lang=lang, unit=unit)
    data = req.with_url(self.get_conf().endpoint).with_credential(self.get_conf().get_credential()).get()
    return WeatherHourlyResponse(**data)
  
  
  def weather_72h(self, location, lang:str='zh-hans', unit:str='m'):
    req = WeatherHourlyRequest(hour_range='72h', location=location,lang=lang, unit=unit)
    data = req.with_url(self.get_conf().endpoint).with_credential(self.get_conf().get_credential()).get()
    return WeatherHourlyResponse(**data)
  
  
  def weather_168h(self, location, lang:str='zh-hans', unit:str='m'):
    req = WeatherHourlyRequest(hour_range='168h', location=location,lang=lang, unit=unit)
    data = req.with_url(self.get_conf().endpoint).with_credential(self.get_conf().get_credential()).get()
    return WeatherHourlyResponse(**data)