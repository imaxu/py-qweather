# coding: utf-8
from pyqweather import QWeatherPackBase
from pyqweather.packages.grid_weather.grid_weather_now import GridWeatherNowRequest, GridWeatherNowResponse
from pyqweather.packages.grid_weather.grid_weather_daily import GridWeatherDailyRequest, GridWeatherDailyResponse
from pyqweather.packages.grid_weather.grid_weather_hourly import GridWeatherHourlyRequest, GridWeatherHourlyResponse


class QWeatherGridWeatherPack(QWeatherPackBase):
  """格点天气API包"""
  
  def grid_weather_now(self, location, lang:str='zh-hans', unit:str='m'):
    """格点实况天气"""
    
    req = GridWeatherNowRequest(location=location,lang=lang, unit=unit)
    data = req.with_url(self.get_conf().endpoint).with_credential(self.get_conf().get_credential()).get()
    return GridWeatherNowResponse(**data)
  
  
  def grid_weather_24h(self, location, lang:str='zh-hans', unit:str='m'):
    """逐小时预报（未来24小时）"""
    
    req = GridWeatherHourlyRequest(hour_range='24h', location=location,lang=lang, unit=unit)
    data = req.with_url(self.get_conf().endpoint).with_credential(self.get_conf().get_credential()).get()
    return GridWeatherHourlyResponse(**data)
  
  
  def grid_weather_72h(self, location, lang:str='zh-hans', unit:str='m'):
    """逐小时预报（未来72小时）"""
    
    req = GridWeatherHourlyRequest(hour_range='72h', location=location,lang=lang, unit=unit)
    data = req.with_url(self.get_conf().endpoint).with_credential(self.get_conf().get_credential()).get()
    return GridWeatherHourlyResponse(**data)
  
  
  def grid_weather_3d(self, location, lang:str='zh-hans', unit:str='m'):
    """格点3天预报"""
    
    req = GridWeatherDailyRequest(day_range='3d', location=location,lang=lang, unit=unit)
    data = req.with_url(self.get_conf().endpoint).with_credential(self.get_conf().get_credential()).get()
    return GridWeatherDailyResponse(**data)
  
  
  def grid_weather_7d(self, location, lang:str='zh-hans', unit:str='m'):
    """格点7天预报"""
    
    req = GridWeatherDailyRequest(day_range='7d', location=location,lang=lang, unit=unit)
    data = req.with_url(self.get_conf().endpoint).with_credential(self.get_conf().get_credential()).get()
    return GridWeatherDailyResponse(**data)
  
  