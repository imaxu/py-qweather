
from pyqweather import QWeatherRequestBase, QWeatherResponseBase
from pyqweather.packages import QWeatherSolarRadiationDto


class SolarRadiationHourlyRequest(QWeatherRequestBase):
  """太阳辐射逐小时预报。
  """
  
  _PATH = '/solar-radiation'
  
  def __init__(self,hour_range:str,  **kwargs):
    """构建太阳辐射逐小时预报的请求类

    Args:
        hour_range (str): ONLY  24h  72h
        **kwargs (dict): 
        
          - location: (必选)需要查询地区的以英文逗号分隔的经度,纬度坐标（十进制，最多支持小数点后两位）。例如 location=116.41,39.92
    """
    super().__init__(**kwargs)
    self.location = self.get_arg('location', kwargs, required=True)
    
    self._PATH = f'/solar-radiation/{hour_range}'
    
    
  def __str__(self) -> str:
    return f'location={self.location}'
  

class SolarRadiationHourlyResponse(QWeatherResponseBase):
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.updateTime = self.get_arg('updateTime', kwargs, None)
    self.radiation:list[QWeatherSolarRadiationDto] = self.get_items('radiation', kwargs, QWeatherSolarRadiationDto)
    """除非特别说明，本数据返回的太阳辐射均指地表垂直向下的短波辐射，单位w/m2"""
    