
from pyqweather import QWeatherRequestBase, QWeatherResponseBase

class CurrentsRequest(QWeatherRequestBase):
  """未来10天全球潮流数据，包括潮流流速和流向。
  """
  
  _PATH = '/ocean/currents'
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.location = self.get_arg('location', kwargs, required=True)
    self.date = self.get_arg('date', kwargs, required=True)
    
    
  def __str__(self) -> str:
    return f'location={self.location}'
  

class CurrentsResponse(QWeatherResponseBase):
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.updateTime = self.get_arg('updateTime', kwargs, None)
    self.fxLink = self.get_arg('fxLink', kwargs, None)
    self.refer= self.get_arg('refer', kwargs, None)
    self.currentsTable:list[any] = self.get_arg('currentsTable', kwargs, [])
    