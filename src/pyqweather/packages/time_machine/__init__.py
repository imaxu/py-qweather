# coding: utf-8
from pyqweather import QWeatherPackBase
from pyqweather.packages.time_machine.historical_weather import HistoricalWeatherRequest, HistoricalWeatherResponse
from pyqweather.packages.time_machine.historical_air import HistoricalAirRequest, HistoricalAirResponse

class QWeatherTimeMachinePack(QWeatherPackBase):
  """时光机API"""
  
  def historical_weather(self, location:str, date:str, unit:str='m', lang:str='zh-hans'):
    """获取最近10天某日历史再分析数据。"""
    
    req = HistoricalWeatherRequest(location=location, date=date, unit=unit, lang=lang)
    data = req.with_url(self.get_conf().endpoint).with_credential(self.get_conf().get_credential()).get()
    return HistoricalWeatherResponse(**data)
  
  
  def historical_air(self, location:str, date:str, lang:str='zh-hans'):
    """获取最近10天某日的中国空气质量历史再分析数据。"""
    
    req = HistoricalAirRequest(location=location, date=date,  lang=lang)
    data = req.with_url(self.get_conf().endpoint).with_credential(self.get_conf().get_credential()).get()
    return HistoricalAirResponse(**data)