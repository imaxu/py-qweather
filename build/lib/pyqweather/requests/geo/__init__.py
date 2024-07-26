
from pyqweather import QWeatherPackBase
from pyqweather.packages.geo.city_lookup import CityLookupRequest, CityLookupResponse

class QWeatherGeoPack(QWeatherPackBase):
  
  _URL = 'https://geoapi.qweather.com/v2'
    
    
  def city_lookup(self, location:str, adm:str=None, range:str='cn', number:int=20, lang:str='zh-hans'):
    
    req = CityLookupRequest(location=location, adm=adm, range=range, number=number, lang=lang)
    data = req.with_url(self._URL).with_credential(self.get_conf().get_credential()).get()
    return CityLookupResponse(data)