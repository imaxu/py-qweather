# coding: utf-8
from pyqweather import QWeatherPackBase
from pyqweather.packages.tropical_cyclone.storm_forecast import StormForecastRequest, StormForecastResponse
from pyqweather.packages.tropical_cyclone.storm_track import StormTrackRequest, StormTrackResponse
from pyqweather.packages.tropical_cyclone.storm_list import StormListRequest, StormListResponse


class QWeatherTropicalCyclonePack(QWeatherPackBase):
  """热带气旋（台风）API"""
  
  def storm_forecast(self, stormid:str) -> StormForecastResponse:
    """台风预报API提供全球主要海洋流域的台风预测位置、等级、气压、风速等。
    如果查询的台风已经结束，则返回的数据为空，建议先通过台风列表接口获取台风的状态
    
    Args:
        stormid (str): (必选)需要查询的台风ID，StormID可通过台风查询API获取。例如 stormid=NP2018

    Returns:
        HistoricalWeatherResponse: _description_
    """
    
    req = StormForecastRequest(stormid=stormid)
    data = req.with_url(self.get_conf().endpoint).with_credential(self.get_conf().get_credential()).get()
    return StormForecastResponse(**data)
  
  
  def storm_track(self, stormid:str) -> StormTrackResponse:
    """台风实况和路径。
    台风实况和路径API提供全球主要海洋流域的台风实时位置、等级、气压、风速以及活跃台风的轨迹路径。

    Args:
        stormid (str): (必选)需要查询的台风ID，StormID可通过台风查询API获取。例如 stormid=NP2018

    Returns:
        StormTrackResponse: _description_
    """
    
    req = StormTrackRequest(stormid=stormid)
    data = req.with_url(self.get_conf().endpoint).with_credential(self.get_conf().get_credential()).get()
    return StormTrackResponse(**data)
  
  
  def storm_list(self, year:str, basin:str='NP') -> StormListResponse:
    """台风列表API提供全球主要海洋流域最近2年的台风列表。```目前仅支持中国沿海地区，即basin=NP```

    Args:
        year (str): (必选)支持查询本年度和上一年度的台风，例如：year=2020, year=2019
        
        basin (str, optional): (必选)需要查询的台风所在的流域，例如中国处于西北太平洋，即 basin=NP。当前仅支持NP。Defaults to 'NP'.
    """
    
    req = StormListRequest(year=year, basin=basin)
    data = req.with_url(self.get_conf().endpoint).with_credential(self.get_conf().get_credential()).get()
    return StormListResponse(**data)