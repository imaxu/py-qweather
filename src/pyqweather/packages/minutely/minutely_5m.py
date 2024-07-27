
from pyqweather import QWeatherRequestBase, QWeatherResponseBase

class Minutely5mRequest(QWeatherRequestBase):
  
  _PATH = '/minutely/5m'
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.location = self.get_arg('location', kwargs, required=True)
    self.lang = self.get_arg('lang', kwargs)
    
    
  def __str__(self) -> str:
    return f'location={self.location}'
  

class Minutely5mResponse(QWeatherResponseBase):
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.updateTime = self.get_arg('updateTime', kwargs, None)
    self.fxLink = self.get_arg('fxLink', kwargs, None)
    self.minutely:list[any] = self.get_arg('minutely', kwargs, [])
    self.summary = self.get_arg('summary', kwargs, None)
    