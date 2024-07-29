
from pyqweather import QWeatherRequestBase, QWeatherResponseBase
from pyqweather.packages import QWeatherTropicalCycloneStormDto


class StormListRequest(QWeatherRequestBase):
  
  _PATH = '/tropical/storm-list'
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.basin = self.get_arg('basin', kwargs, required=True)
    self.year = self.get_arg('year', kwargs, required=True)
    
    
  def __str__(self) -> str:
    return f'stormid={self.stormid}'
  

class StormListResponse(QWeatherResponseBase):
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.updateTime = self.get_arg('updateTime', kwargs, None)
    self.fxLink = self.get_arg('fxLink', kwargs, None)
    self.storm:list[QWeatherTropicalCycloneStormDto] = self.get_items('storm', kwargs, QWeatherTropicalCycloneStormDto)
    