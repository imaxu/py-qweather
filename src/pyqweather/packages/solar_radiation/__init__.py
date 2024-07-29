# coding: utf-8
from pyqweather import QWeatherPackBase
from pyqweather.packages.solar_radiation.solar_radiation_hourly import SolarRadiationHourlyRequest, SolarRadiationHourlyResponse


class QWeatherSolarRadiationPack(QWeatherPackBase):
  """_summary_

  Args:
      QWeatherPackBase (_type_): _description_
  """
  
  def hourly_24h(self, location:str)  -> SolarRadiationHourlyResponse:
    """太阳辐射24小时预报

    Args:
        location (str): (必选)需要查询地区的以英文逗号分隔的经度,纬度坐标（十进制，最多支持小数点后两位）。例如 location=116.41,39.92

    Returns:
        SolarRadiationHourlyResponse: _description_
    """
    req = SolarRadiationHourlyRequest('24h', location=location)
    data = req.with_url(self.get_conf().endpoint).with_credential(self.get_conf().get_credential()).get()
    return SolarRadiationHourlyResponse(**data)
  
  
  def hourly_72h(self, location:str)  -> SolarRadiationHourlyResponse:
    """太阳辐射72小时预报

    Args:
        location (str): (必选)需要查询地区的以英文逗号分隔的经度,纬度坐标（十进制，最多支持小数点后两位）。例如 location=116.41,39.92

    Returns:
        SolarRadiationHourlyResponse: _description_
    """
    req = SolarRadiationHourlyRequest('72h', location=location)
    data = req.with_url(self.get_conf().endpoint).with_credential(self.get_conf().get_credential()).get()
    return SolarRadiationHourlyResponse(**data)