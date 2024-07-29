# coding: utf-8
from pyqweather import QWeatherPackBase
from pyqweather.packages.indices.indices_daily import IndicesDailyRequest, IndicesDailyResponse


class QWeatherIndicesPack(QWeatherPackBase):
  """天气指数API包"""
  
  def indices_1d(self, location:str, type, lang:str='zh-hans'):
    """1日天气指数预报

    Args:
        location (str): (必选)需要查询地区的LocationID或以英文逗号分隔的经度,纬度坐标（十进制，最多支持小数点后两位），LocationID可通过GeoAPI获取。例如 location=101010100 或 location=116.41,39.92
        type(str): (必选)生活指数的类型ID，包括洗车指数、穿衣指数、钓鱼指数等。可以一次性获取多个类型的生活指数，多个类型用英文,分割。例如type=3,5。具体生活指数的ID和等级参考天气指数信息。各项生活指数并非适用于所有城市。
        lang (str, optional):多语言设置，请阅读多语言文档，了解我们的多语言是如何工作、如何设置以及数据是否支持多语言。 Defaults to 'zh-hans'.

    Returns:
        _type_: _description_
    """    
    
    req = IndicesDailyRequest(day_range='1d', location=location, type=type, lang=lang)
    data = req.with_url(self.get_conf().endpoint).with_credential(self.get_conf().get_credential()).get()
    return IndicesDailyResponse(**data)
  
  
  def indices_3d(self, location:str, type, lang:str='zh-hans'):
    """3日天气指数预报

    Args:
        location (str): (必选)需要查询地区的LocationID或以英文逗号分隔的经度,纬度坐标（十进制，最多支持小数点后两位），LocationID可通过GeoAPI获取。例如 location=101010100 或 location=116.41,39.92
        type(str): (必选)生活指数的类型ID，包括洗车指数、穿衣指数、钓鱼指数等。可以一次性获取多个类型的生活指数，多个类型用英文,分割。例如type=3,5。具体生活指数的ID和等级参考天气指数信息。各项生活指数并非适用于所有城市。
        lang (str, optional):多语言设置，请阅读多语言文档，了解我们的多语言是如何工作、如何设置以及数据是否支持多语言。 Defaults to 'zh-hans'.

    Returns:
        _type_: _description_
    """    
    
    req = IndicesDailyRequest(day_range='3d', location=location, type=type, lang=lang)
    data = req.with_url(self.get_conf().endpoint).with_credential(self.get_conf().get_credential()).get()
    return IndicesDailyResponse(**data)

    
  