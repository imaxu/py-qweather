
from pyqweather import QWeatherRequestBase, QWeatherResponseBase
from pyqweather.packages import QWeatherWarningDto


class WarningNowRequest(QWeatherRequestBase):
  
  _PATH = '/warning/now'
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.location = self.get_arg('location', kwargs, required=True)
    self.lang = self.get_arg('lang', kwargs)
    
    
  def __str__(self) -> str:
    return f'location={self.location}'
  


class WarningNowResponse(QWeatherResponseBase):
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.updateTime = self.get_arg('updateTime', kwargs, None)
    self.fxLink = self.get_arg('fxLink', kwargs, None)
    self.warning:list[QWeatherWarningDto] = self.get_items('warning', kwargs, QWeatherWarningDto)
    