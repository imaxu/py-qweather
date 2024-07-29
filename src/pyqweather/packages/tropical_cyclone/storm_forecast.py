
from pyqweather import QWeatherRequestBase, QWeatherResponseBase
from pyqweather.packages import QWeatherTropicalCycloneForecastDto


class StormForecastRequest(QWeatherRequestBase):
  
  _PATH = '/tropical/storm-forecast'
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.stormid = self.get_arg('stormid', kwargs, required=True)
    
    
  def __str__(self) -> str:
    return f'stormid={self.stormid}'
  

class StormForecastResponse(QWeatherResponseBase):
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.updateTime = self.get_arg('updateTime', kwargs, None)
    self.fxLink = self.get_arg('fxLink', kwargs, None)
    self.forecast:list[QWeatherTropicalCycloneForecastDto] = self.get_items('forecast', kwargs, QWeatherTropicalCycloneForecastDto)
    