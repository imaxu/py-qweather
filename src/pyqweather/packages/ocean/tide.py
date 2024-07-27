
from pyqweather import QWeatherRequestBase, QWeatherResponseBase

class TideRequest(QWeatherRequestBase):
  """未来10天全球潮汐数据，包括满潮、干潮高度和时间，逐小时潮汐数据。"""
  
  _PATH = '/ocean/tide'
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.location = self.get_arg('location', kwargs, required=True)
    self.date = self.get_arg('date', kwargs, required=True)
    
    
  def __str__(self) -> str:
    return f'location={self.location}'
  

class TideResponse(QWeatherResponseBase):
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.updateTime = self.get_arg('updateTime', kwargs, None)
    self.fxLink = self.get_arg('fxLink', kwargs, None)
    self.refer= self.get_arg('refer', kwargs, None)
    self.tideTable:list[any] = self.get_arg('tideTable', kwargs, [])
    