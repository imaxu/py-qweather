
from pyqweather import QWeatherRequestBase, QWeatherResponseBase

class HistoricalAirRequest(QWeatherRequestBase):
  
  _PATH = '/historical/air'
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.location = self.get_arg('location', kwargs, required=True)
    self.date = self.get_arg('date', kwargs, required=True)
    self.lang = self.get_arg('lang', kwargs)
    
    
  def __str__(self) -> str:
    return f'location={self.location}'
  

class HistoricalAirResponse(QWeatherResponseBase):
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.fxLink = self.get_arg('fxLink', kwargs, None)
    self.refer= self.get_arg('refer', kwargs, None)
    self.airHourly:list[any] = self.get_arg('airHourly', kwargs, [])
    