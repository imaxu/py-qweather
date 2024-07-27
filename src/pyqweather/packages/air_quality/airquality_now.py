
from pyqweather import QWeatherRequestBase, QWeatherResponseBase

class AirQualityNowRequest(QWeatherRequestBase):
  
  _PATH = '/now'
  
  def __init__(self, locationId:str,  **kwargs):
    super().__init__(**kwargs)
    self.locationId = locationId
    # self.pollutant = self.get_arg('pollutant', kwargs, False)
    # self.station = self.get_arg('station', kwargs, True)
    self.lang = self.get_arg('lang', kwargs)
    
    self._PATH = f'/now/{self.locationId}'
    
    
  def __str__(self) -> str:
    return f'location={self.location}'
  


class AirQualityNowResponse(QWeatherResponseBase):
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.updateTime = self.get_arg('updateTime', kwargs, None)
    self.aqi:list[any] = self.get_arg('aqi', kwargs, [])
    