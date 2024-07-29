
from pyqweather import QWeatherRequestBase, QWeatherResponseBase
from pyqweather.packages import QWeatherAirRealDataDto, QWeatherAirStationDataDto


class AirNowRequest(QWeatherRequestBase):
  
  _PATH = '/air/now'
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.location = self.get_arg('location', kwargs, required=True)
    self.lang = self.get_arg('lang', kwargs)
    
    
  def __str__(self) -> str:
    return f'location={self.location}'
  

class AirNowResponse(QWeatherResponseBase):
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.updateTime = self.get_arg('updateTime', kwargs, None)
    self.fxLink = self.get_arg('fxLink', kwargs, None)
    self.now:QWeatherAirRealDataDto = self.get_obj('now', kwargs, QWeatherAirRealDataDto)
    self.station:list[QWeatherAirStationDataDto] = self.get_items('station', kwargs, QWeatherAirStationDataDto)
    