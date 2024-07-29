
from pyqweather import QWeatherRequestBase, QWeatherResponseBase
from pyqweather.packages import QWeatherIndicesDailyDto


class IndicesDailyRequest(QWeatherRequestBase):
  
  _PATH = '/indices'
  
  def __init__(self, day_range: str, **kwargs):
    super().__init__(**kwargs)
    self._PATH = f'/indices/{day_range}'
    self.location = self.get_arg('location', kwargs, required=True)
    self.lang = self.get_arg('lang', kwargs)
    self.type = self.get_arg('type', kwargs, required=True)
    
    
  def __str__(self) -> str:
    return f'location={self.location}'
  

class IndicesDailyResponse(QWeatherResponseBase):
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.updateTime = self.get_arg('updateTime', kwargs, None)
    self.fxLink = self.get_arg('fxLink', kwargs, None)
    self.daily:list[QWeatherIndicesDailyDto] = self.get_items('daily', kwargs, QWeatherIndicesDailyDto)
    