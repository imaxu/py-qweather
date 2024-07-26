# coding: utf-8

from pyqweather import QWeatherConfig
from pyqweather.packages.geo import QWeatherGeoPack

class QWeatherFactory:
  
  def __init__(self):
    self._pack_dict = {
      'geo': { 'ns': 'pyqweather.requests.geo', 'module': 'QWeatherGeoPack' }
    }
  
  
  def create_pack(self, packName: str, config: QWeatherConfig):
    
    if packName not in self._pack_dict:
      return None
    
    packInfo = self._pack_dict[packName]
    ns = __import__(packInfo['ns'], fromlist=['None'])
    moduleName = packInfo['module']
    moduleInstance = eval(f'ns.{moduleName}(config)')
    return moduleInstance
  
  
  def create_geo_pack(self, config: QWeatherConfig) -> QWeatherGeoPack:
    return QWeatherGeoPack(config)