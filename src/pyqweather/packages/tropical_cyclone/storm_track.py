
from pyqweather import QWeatherRequestBase, QWeatherResponseBase

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
    self.now = self.get_arg('now', kwargs, None)
    self.refer= self.get_arg('refer', kwargs, None)
    self.track:list[any] = self.get_arg('track', kwargs, [])
    