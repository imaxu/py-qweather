
from pyqweather import QWeatherRequestBase, QWeatherResponseBase
from pyqweather.packages import QWeatherWeatherDailyDataDto


class WeatherDailyRequest(QWeatherRequestBase):
  
  _PATH = '/weather'
  
  def __init__(self, day_range: str, **kwargs):
    super().__init__(**kwargs)
    self._PATH = f'/weather/{day_range}'
    self.location = self.get_arg('location', kwargs, required=True)
    self.lang = self.get_arg('lang', kwargs)
    self.unit = self.get_arg('unit', kwargs)
    
    
  def __str__(self) -> str:
    return f'location={self.location}'
  

class WeatherDailyResponse(QWeatherResponseBase):
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.updateTime = self.get_arg('updateTime', kwargs, None)
    self.fxLink = self.get_arg('fxLink', kwargs, None)
    self.daily:list[QWeatherWeatherDailyDataDto] = self.get_items('daily', kwargs, QWeatherWeatherDailyDataDto)
    