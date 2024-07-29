#coding: utf-8
from pyqweather import QWeatherPackBase
from pyqweather.packages.air_quality.airquality_now import AirQualityNowRequest, AirQualityNowResponse
from pyqweather.packages.air_quality.airquality_station import AirQualityStationRequest, AirQualityStationResponse

class QWeatherAirQualityPack(QWeatherPackBase):
  """全球空气质量"""
  
  
  def airquality_now(self, locationId:str, lang:str='zh-hans'):
    """实时空气质量"""
    
    req = AirQualityNowRequest(locationId=locationId,  lang=lang)
    data = req.with_url(self.get_conf().endpoint).with_credential(self.get_conf().get_credential()).get()
    return AirQualityNowResponse(**data)

  def airquality_station(self, locationId:str, lang:str='zh-hans'):
    """监测站数据"""
    
    req = AirQualityStationRequest(locationId=locationId, lang=lang)
    data = req.with_url(self.get_conf().endpoint).with_credential(self.get_conf().get_credential()).get()
    return AirQualityStationResponse(**data)