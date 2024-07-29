# coding: utf-8
from pyqweather import QWeatherPackBase
from pyqweather.packages.minutely.minutely_5m import Minutely5mRequest, Minutely5mResponse


class QWeatherMinutelyPack(QWeatherPackBase):
  """分钟级降水API（临近预报）"""
  
  def minutely_5m(self, location, lang:str='zh-hans'):
    """中国1公里精度的未来2小时每5分钟降雨预报数据。"""
    
    req = Minutely5mRequest(location=location,lang=lang)
    data = req.with_url(self.get_conf().endpoint).with_credential(self.get_conf().get_credential()).get()
    return Minutely5mResponse(**data)
  