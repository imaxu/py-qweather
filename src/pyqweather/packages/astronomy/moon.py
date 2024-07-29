
from pyqweather import QWeatherRequestBase, QWeatherResponseBase
from pyqweather.packages import QWeatherMoonPhaseDto


class AstronomyMoonRequest(QWeatherRequestBase):
  
  _PATH = '/astronomy/moon'
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.location = self.get_arg('location', kwargs, required=True)
    self.date = self.get_arg('date', kwargs, required=True)
    self.lang = self.get_arg('lang', kwargs)
    
  def __str__(self) -> str:
    return f'location={self.location}'
  

class AstronomyMoonResponse(QWeatherResponseBase):
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.updateTime = self.get_arg('updateTime', kwargs, None)
    self.fxLink = self.get_arg('fxLink', kwargs, None)
    self.moonrise= self.get_arg('sunrise', kwargs, None)
    self.moonset= self.get_arg('sunset', kwargs, None)
    self.moonPhase:list[QWeatherMoonPhaseDto]= self.get_items('moonPhase', kwargs, QWeatherMoonPhaseDto)