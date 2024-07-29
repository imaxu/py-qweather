
from pyqweather import QWeatherRequestBase, QWeatherResponseBase
from pyqweather.packages import QWeatherWarningCityDto


class WarningListRequest(QWeatherRequestBase):
  """获取指定国家或地区当前正在发生天气灾害预警的城市列表"""
  
  _PATH = '/warning/list'
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.range = self.get_arg('range', kwargs, required=True)
    
    
  def __str__(self) -> str:
    return f'location={self.location}'
  


class WarningListResponse(QWeatherResponseBase):
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.updateTime = self.get_arg('updateTime', kwargs, None)
    self.warningLocList:list[QWeatherWarningCityDto] = self.get_items('warningLocList', kwargs, QWeatherWarningCityDto)
    