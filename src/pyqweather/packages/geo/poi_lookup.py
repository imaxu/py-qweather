
from pyqweather import QWeatherRequestBase, QWeatherResponseBase
from pyqweather.packages import QWeatherLocationDto


class PoiLookupRequest(QWeatherRequestBase):
  
  _PATH = '/poi/lookup'
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.location = self.get_arg('location', kwargs, required=True)
    self.type = self.get_arg('type', kwargs, required=True)
    self.city = self.get_arg('city', kwargs)
    self.number = self.get_arg('number', kwargs)
    self.lang = self.get_arg('lang', kwargs)
    
    
  def __str__(self) -> str:
    return f'location={self.location}'
  


class PoiLookupResponse(QWeatherResponseBase):
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.poi:list[QWeatherLocationDto] = self.get_items('poi', kwargs, QWeatherLocationDto)
    