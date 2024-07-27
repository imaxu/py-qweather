
from pyqweather import QWeatherRequestBase, QWeatherResponseBase

class AirNowRequest(QWeatherRequestBase):
  
  _PATH = '/air/now'
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.location = self.get_arg('location', kwargs, required=True)
    self.lang = self.get_arg('lang', kwargs)
    
    
  def __str__(self) -> str:
    return f'location={self.location}'
  

class AirNowResponse(QWeatherResponseBase):
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.updateTime = self.get_arg('updateTime', kwargs, None)
    self.fxLink = self.get_arg('fxLink', kwargs, None)
    self.now = self.get_arg('now', kwargs, None)
    self.station:list[any] = self.get_arg('station', kwargs, [])
    self.refer = self.get_arg('refer', kwargs, None)
    