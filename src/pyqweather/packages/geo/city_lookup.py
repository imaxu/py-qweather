
from pyqweather import QWeatherRequestBase, QWeatherResponseBase
from pyqweather.packages import QWeatherLocationDto,  QWeatherReferDto


class CityLookupRequest(QWeatherRequestBase):
  
  _PATH = '/city/lookup'
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.location = self.get_arg('location', kwargs, required=True)
    self.adm = self.get_arg('adm', kwargs)
    self.range = self.get_arg('range', kwargs)
    self.number = self.get_arg('number', kwargs)
    self.lang = self.get_arg('lang', kwargs)
    
    
  def __str__(self) -> str:
    return f'location={self.location}'
  


class CityLookupResponse(QWeatherResponseBase):
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.location:list[QWeatherLocationDto] = self.get_items('location', kwargs, QWeatherLocationDto)
    self.refer:QWeatherReferDto = self.get_obj('refer', kwargs, QWeatherReferDto)
    