# coding: utf-8
from pyqweather import QWeatherPackBase
from pyqweather.packages.ocean.tide import TideRequest, TideResponse
from pyqweather.packages.ocean.currents import CurrentsRequest, CurrentsResponse


class QWeatherOceanPack(QWeatherPackBase):
  
  
  def tide(self, location:str, date:str):
    """未来10天全球潮汐数据，包括满潮、干潮高度和时间，逐小时潮汐数据。

    Args:
        location (str): (必选)需要查询的潮汐站点，请填写潮汐站点的LocationID，LocationID可通过POI搜索服务获取。例如 location=P2951
        date (str): (必选)选择日期，最多可选择未来10天（包含今天）的数据。日期格式为yyyyMMdd，例如 date=20200531

    Returns:
        TideResponse: _description_
    """
    req = TideRequest(location=location, date=date)
    data = req.with_url(self.get_conf().endpoint).with_credential(self.get_conf().get_credential()).get()
    return TideResponse(**data)
  
  
  def currents(self, location:str, date:str):
    """未来10天全球潮流数据，包括潮流流速和流向。

    Args:
        location (str): (必选)需要查询的潮汐站点，请填写潮汐站点的LocationID，LocationID可通过POI搜索服务获取。例如 location=P2951
        date (str): (必选)选择日期，最多可选择未来10天（包含今天）的数据。日期格式为yyyyMMdd，例如 date=20200531

    Returns:
        CurrentsResponse: _description_
    """
    req = CurrentsRequest(location=location, date=date)
    data = req.with_url(self.get_conf().endpoint).with_credential(self.get_conf().get_credential()).get()
    return CurrentsResponse(**data)