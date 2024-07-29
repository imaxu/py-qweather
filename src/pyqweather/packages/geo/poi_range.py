
from pyqweather import QWeatherRequestBase, QWeatherResponseBase
from pyqweather.packages import QWeatherLocationDto


class PoiRangeRequest(QWeatherRequestBase):
  
  _PATH = '/poi/range'
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.location = self.get_arg('location', kwargs, required=True)
    self.type = self.get_arg('type', kwargs, required=True)
    self.radius = self.get_arg('radius', kwargs)
    self.number = self.get_arg('number', kwargs)
    self.lang = self.get_arg('lang', kwargs)
    
    
  def __str__(self) -> str:
    return f'location={self.location}'
  


class PoiRangeResponse(QWeatherResponseBase):
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.poi:list[QWeatherLocationDto] = self.get_items('poi', kwargs, QWeatherLocationDto)
    