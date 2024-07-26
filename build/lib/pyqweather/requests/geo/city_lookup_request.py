
from pyqweather import QWeatherRequestBase, QWeatherResponseBase

class CityLookupRequest(QWeatherRequestBase):
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.location = self.get_arg('location', kwargs)
    self.adm = self.get_arg('adm', kwargs)
    self.range = self.get_arg('range', kwargs)
    self.number = self.get_arg('number', kwargs)
    self.lang = self.get_arg('lang', kwargs)
    
    
  def __str__(self) -> str:
    return f'location={self.location}'
  


class CityLookupResponse(QWeatherResponseBase):
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.location:list[any] = self.get_arg('location', kwargs, [])
    