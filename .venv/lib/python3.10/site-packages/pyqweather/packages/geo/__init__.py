#coding: utf-8
from pyqweather import QWeatherPackBase
from pyqweather.packages.geo.city_lookup import CityLookupRequest, CityLookupResponse
from pyqweather.packages.geo.city_top import CityTopRequest, CityTopResponse
from pyqweather.packages.geo.poi_lookup import PoiLookupRequest, PoiLookupResponse
from pyqweather.packages.geo.poi_range import PoiRangeRequest, PoiRangeResponse
import inspect

class QWeatherGeoPack(QWeatherPackBase):
  
  _URL = 'https://geoapi.qweather.com/v2'
    
    
  def city_lookup(self, location:str, adm:str=None, range:str='cn', number:int=10, lang:str='zh-hans'):
    """城市搜索"""
    req = CityLookupRequest(location=location, adm=adm, range=range, number=number, lang=lang)
    data = req.with_url(self._URL).with_credential(self.get_conf().get_credential()).get()
    return CityLookupResponse(**data)
  
  
  def city_top(self, range:str='cn', number:int=10, lang:str='zh-hans'):
    """热门城市列表"""
    req = CityTopRequest(range=range, number=number, lang=lang)
    data = req.with_url(self._URL).with_credential(self.get_conf().get_credential()).get()
    return CityTopResponse(**data)
  
  
  def poi_lookup(self, location:str, type:str, city:str=None, number:int=10, lang:str='zh-hans'):
    """POI搜索"""
    frame = inspect.currentframe()
    args = inspect.getargvalues(frame)
    del frame 
    del args.locals['self']
    
    req = PoiLookupRequest(**args.locals)
    data = req.with_url(self._URL).with_credential(self.get_conf().get_credential()).get()
    return PoiLookupResponse(**data)  
  
  
  def poi_range(self, location:str, type:str, radius:str=None, number:int=10, lang:str='zh-hans'):
    """POI范围搜索"""
    frame = inspect.currentframe()
    args = inspect.getargvalues(frame)
    del frame 
    del args.locals['self']  
      
    req = PoiRangeRequest(**args.locals)
    data = req.with_url(self._URL).with_credential(self.get_conf().get_credential()).get()
    return PoiRangeResponse(**data)  