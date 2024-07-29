# coding: utf-8
from pyqweather import QWeatherPackBase
from pyqweather.packages.astronomy.sun import AstronomySunRequest, AstronomySunResponse
from pyqweather.packages.astronomy.moon import AstronomyMoonRequest, AstronomyMoonResponse
from pyqweather.packages.astronomy.solar_elevation_angle import AstronomySolarElevationAngleRequest, AstronomySolarElevationAngleResponse



class QWeatherAstronomyPack(QWeatherPackBase):
  """天文API包"""
  
  def sun(self, location:str, date:str) -> AstronomySunResponse:
    """获取未来60天全球任意地点日出日落时间。
    
    Args:
        location (str): (必选)需要查询地区的LocationID或以英文逗号分隔的经度,纬度坐标（十进制，最多支持小数点后两位），LocationID可通过GeoAPI获取。例如 location=101010100 或 location=116.41,39.92
        date (str): (必选)选择日期，最多可选择未来60天（包含今天）的数据。日期格式为yyyyMMdd，例如 date=20200531

    Returns:
        AstronomySunResponse: _description_
    """
    
    req = AstronomySunRequest(location=location,date=date)
    data = req.with_url(self.get_conf().endpoint).with_credential(self.get_conf().get_credential()).get()
    return AstronomySunResponse(**data)
  
  
  def moon(self, location:str, date:str , lang:str='zh-hans') -> AstronomyMoonResponse:
    """月升月落和月相

    Args:
        location (_type_): (必选)需要查询地区的LocationID或以英文逗号分隔的经度,纬度坐标（十进制，最多支持小数点后两位），LocationID可通过GeoAPI获取。例如 location=101010100 或 location=116.41,39.92
        date (str): (必选)选择日期，最多可选择未来60天（包含今天）的数据。日期格式为yyyyMMdd，例如 date=20200531
        lang (str, optional): 多语言设置. Defaults to 'zh-hans'.


    Returns:
        AstronomyMoonResponse: _description_
    """
    
    req = AstronomyMoonRequest(location=location, date=date,  lang=lang)
    data = req.with_url(self.get_conf().endpoint).with_credential(self.get_conf().get_credential()).get()
    return AstronomyMoonResponse(**data)
  
  
  def solar_elevation_angle(self, location:str, date:str, time:str, alt:str, tz:str='0800') -> AstronomySolarElevationAngleResponse:
    """任意时间点的全球太阳高度及方位角。

    Args:
        location (str): (必选)需要查询地区的以英文逗号分隔的经度,纬度坐标（十进制，最多支持小数点后两位）。例如 location=116.41,39.92
        date (str): (必选)查询日期，格式为yyyyMMdd，例如 date=20170809
        time (str): (必选)查询时间，格式为HHmm，24时制，例如 time=1230
        alt (str): (必选)海拔高度，单位为米，例如alt=43
        tz (str, optional): 查询地区所在时区，例如tz=0800或tz=-0530 ，默认0800

    Returns:
        AstronomySolarElevationAngleRequest: _description_
    """
    req = AstronomySolarElevationAngleRequest(location=location, date=date, time=time,  alt=alt, tz=tz)
    data = req.with_url(self.get_conf().endpoint).with_credential(self.get_conf().get_credential()).get()
    return AstronomySolarElevationAngleResponse(**data)
  
  
  