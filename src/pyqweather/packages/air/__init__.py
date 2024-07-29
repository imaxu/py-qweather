#coding: utf-8
from pyqweather import QWeatherPackBase
from pyqweather.packages.air.air_now import AirNowRequest, AirNowResponse
from pyqweather.packages.air.air_daily import AirDailyRequest, AirDailyResponse


class QWeatherAirPack(QWeatherPackBase):
  """空气质量
  """
  
  def air_now(self, location, lang:str='zh-hans'):
    """实时空气质量"""
    
    req = AirNowRequest(location=location,lang=lang)
    data = req.with_url(self.get_conf().endpoint).with_credential(self.get_conf().get_credential()).get()
    return AirNowResponse(**data)
  
  
  def air_5d(self, location:str, lang:str='zh-hans'):
    """空气质量每日预报

    Args:
        location (str): (必选)需要查询地区的LocationID或以英文逗号分隔的经度,纬度坐标（十进制，最多支持小数点后两位），LocationID可通过GeoAPI获取。例如 location=101010100 或 location=116.41,39.92
        lang (str, optional): 多语言设置，请阅读多语言文档，了解我们的多语言是如何工作、如何设置以及数据是否支持多语言。 Defaults to 'zh-hans'.

    Returns:
        _type_: _description_
    """
    
    req = AirDailyRequest(day_range='5d', location=location,lang=lang)
    data = req.with_url(self.get_conf().endpoint).with_credential(self.get_conf().get_credential()).get()
    return AirDailyResponse(**data)