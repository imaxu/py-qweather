
from pyqweather import QWeatherRequestBase, QWeatherResponseBase
from pyqweather.packages import QWeatherAirDailyDto
from dataclasses import dataclass


class AirDailyRequest(QWeatherRequestBase):
  
  _PATH = '/air'
  
  def __init__(self, day_range:str, **kwargs):
    super().__init__(**kwargs)
    self.location = self.get_arg('location', kwargs, required=True)
    self.lang = self.get_arg('lang', kwargs)
    self._PATH = f'/air/{day_range}'
    
    
  def __str__(self) -> str:
    return f'location={self.location}'
  
@dataclass
class AirDailyResponse(QWeatherResponseBase):
  
  updateTime: str
  fxLink: str
  daily:list[QWeatherAirDailyDto]
  
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.updateTime = self.get_arg('updateTime', kwargs, None)
    self.fxLink = self.get_arg('fxLink', kwargs, None)
    self.daily:list[QWeatherAirDailyDto] = self.get_items('daily', kwargs, QWeatherAirDailyDto)
    