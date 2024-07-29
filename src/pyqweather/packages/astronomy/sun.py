
from pyqweather import QWeatherRequestBase, QWeatherResponseBase

class AstronomySunRequest(QWeatherRequestBase):
  
  _PATH = '/astronomy/sun'
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.location = self.get_arg('location', kwargs, required=True)
    self.date = self.get_arg('date', kwargs, required=True)
    
    
  def __str__(self) -> str:
    return f'location={self.location}'
  

class AstronomySunResponse(QWeatherResponseBase):
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.updateTime = self.get_arg('updateTime', kwargs, None)
    self.fxLink = self.get_arg('fxLink', kwargs, None)
    self.sunrise= self.get_arg('sunrise', kwargs, None)
    self.sunset= self.get_arg('sunset', kwargs, None)
    