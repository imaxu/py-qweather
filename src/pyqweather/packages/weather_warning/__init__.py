# coding: utf-8
from pyqweather import QWeatherPackBase
from pyqweather.packages.weather_warning.warning_now import WarningNowRequest, WarningNowResponse
from pyqweather.packages.weather_warning.warning_list import WarningListRequest, WarningListResponse

class QWeatherWeatherWarningPack(QWeatherPackBase):
  """天气灾害预警API包"""
  
  def warning_now(self, location, lang:str='zh-hans'):
    """天气灾害预警

    Args:
        location (_type_): (必选)需要查询地区的LocationID或以英文逗号分隔的经度,纬度坐标（十进制，最多支持小数点后两位），LocationID可通过GeoAPI获取。例如 location=101010100 或 location=116.41,39.92
        lang (str, optional):多语言设置，请阅读多语言文档，了解我们的多语言是如何工作、如何设置以及数据是否支持多语言。 Defaults to 'zh-hans'.

    Returns:
        _type_: _description_
    """    
    
    req = WarningNowRequest(location=location,lang=lang)
    data = req.with_url(self.get_conf().endpoint).with_credential(self.get_conf().get_credential()).get()
    return WarningNowResponse(**data)
  
  
  def warning_list(self, range: str):
    """获取指定国家或地区当前正在发生天气灾害预警的城市列表

    Args:
        range (str): 选择指定的国家或地区，使用ISO 3166格式。
        例如range=cn或range=hk。目前该功能仅支持中国（包括港澳台）地区的城市列表，其他国家和地区请使用请使用[天气灾害预警]单独获取。
    """   
    req = WarningListRequest(range=range)
    data = req.with_url(self.get_conf().endpoint).with_credential(self.get_conf().get_credential()).get()
    return WarningListResponse(**data) 
    
  