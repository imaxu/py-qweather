
from pyqweather import QWeatherRequestBase, QWeatherResponseBase
from pyqweather.packages import QWeatherLocationDto


class CityTopRequest(QWeatherRequestBase):
  
  _PATH = '/city/top'
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.range = self.get_arg('range', kwargs)
    self.number = self.get_arg('number', kwargs)
    self.lang = self.get_arg('lang', kwargs)
    
    
  def __str__(self) -> str:
    return f'location={self.range}, number={self.number}, lang={self.lang}'
  


class CityTopResponse(QWeatherResponseBase):
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.top_city_list:list[QWeatherLocationDto] = self.get_items('topCityList', kwargs, QWeatherLocationDto)
    