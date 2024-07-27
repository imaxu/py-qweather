
from pyqweather import QWeatherRequestBase, QWeatherResponseBase

class HistoricalWeatherRequest(QWeatherRequestBase):
  
  _PATH = '/historical/weather'
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.location = self.get_arg('location', kwargs, required=True)
    self.date = self.get_arg('date', kwargs, required=True)
    self.lang = self.get_arg('lang', kwargs)
    self.unit = self.get_arg('unit', kwargs)
    
    
  def __str__(self) -> str:
    return f'location={self.location}'
  

class HistoricalWeatherResponse(QWeatherResponseBase):
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.fxLink = self.get_arg('fxLink', kwargs, None)
    self.weatherDaily= self.get_arg('weatherDaily', kwargs, None)
    self.weatherHourly:list[any] = self.get_arg('weatherHourly', kwargs, [])
    