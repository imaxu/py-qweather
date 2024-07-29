
from pyqweather import QWeatherRequestBase, QWeatherResponseBase
from pyqweather.packages import QWeatherTropicalCycloneDataDto


class StormTrackRequest(QWeatherRequestBase):
  
  _PATH = '/tropical/storm-track'
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.stormid = self.get_arg('stormid', kwargs, required=True)
    
    
  def __str__(self) -> str:
    return f'stormid={self.stormid}'
  

class StormTrackResponse(QWeatherResponseBase):
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.updateTime = self.get_arg('updateTime', kwargs, None)
    self.fxLink = self.get_arg('fxLink', kwargs, None)
    self.isActive = self.get_arg('isActive', kwargs, None)
    """是否为活跃台风。1 活跃台风，0 停编。"""
    self.now:QWeatherTropicalCycloneDataDto = self.get_obj('now', kwargs, QWeatherTropicalCycloneDataDto)
    self.track:list[QWeatherTropicalCycloneDataDto] = self.get_items('track', kwargs, QWeatherTropicalCycloneDataDto)
    