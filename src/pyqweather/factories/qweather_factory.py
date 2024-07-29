# coding: utf-8

from pyqweather import QWeatherConfig
from pyqweather.packages.geo import QWeatherGeoPack
from pyqweather.packages.weather import QWeatherWeatherPack
from pyqweather.packages.minutely import QWeatherMinutelyPack
from pyqweather.packages.grid_weather import QWeatherGridWeatherPack
from pyqweather.packages.weather_warning import QWeatherWeatherWarningPack
from pyqweather.packages.indices import QWeatherIndicesPack
from pyqweather.packages.air_quality import QWeatherAirQualityPack
from pyqweather.packages.air import QWeatherAirPack
from pyqweather.packages.time_machine import QWeatherTimeMachinePack
from pyqweather.packages.tropical_cyclone import QWeatherTropicalCyclonePack
from pyqweather.packages.ocean import QWeatherOceanPack
from pyqweather.packages.solar_radiation import QWeatherSolarRadiationPack
from pyqweather.packages.astronomy import QWeatherAstronomyPack


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
    """创建 Geo API包"""
    
    return QWeatherGeoPack(config)
  
  
  def create_weather_pack(self, config: QWeatherConfig) -> QWeatherWeatherPack:
    """创建城市天气预报API包"""
    
    return QWeatherWeatherPack(config)
  
  
  def create_minutely_pack(self, config: QWeatherConfig) -> QWeatherMinutelyPack:
    """创建分钟级降水API（临近预报）包
    """
    
    return QWeatherMinutelyPack(config)
  
  
  def create_grid_weather_pack(self, config: QWeatherConfig) -> QWeatherGridWeatherPack:
    """以经纬度为基准的全球高精度、公里级、格点化天气预报产品，包括任意经纬度的实时天气和天气预报。"""
    
    return QWeatherGridWeatherPack(config)
  
  
  def create_weather_warning_pack(self, config: QWeatherConfig) -> QWeatherWeatherWarningPack:
    """创建预警API包"""
    
    return QWeatherWeatherWarningPack(config)
  
  
  def create_indices_pack(self, config: QWeatherConfig) -> QWeatherIndicesPack:
    """创建中国和全球城市天气生活指数预报数据API包"""
    
    return QWeatherIndicesPack(config)
  
  
  def create_airquality_pack(self, config: QWeatherConfig) -> QWeatherAirQualityPack:
    """创建空气质量(beta)API包"""
    
    return QWeatherAirQualityPack(config)
  
  def create_air_pack(self, config: QWeatherConfig) -> QWeatherAirPack:
    """创建空气质量 API包"""
    
    return QWeatherAirPack(config)
  
  
  def create_time_machine_pack(self, config: QWeatherConfig) -> QWeatherTimeMachinePack:
    """创建时光机 API包"""
    
    return QWeatherTimeMachinePack(config)
  
  
  def create_tropical_cyclone_pack(self, config: QWeatherConfig) -> QWeatherTropicalCyclonePack:
    """创建热带气旋（台风） API包
    
    ```热带气旋（台风）API提供全球主要海洋流域的台风信息，包括台风实时位置、等级、气压、风速，还可查询台风路径和台风预报信息。```
    """
    
    return QWeatherTropicalCyclonePack(config)
  
  
  def create_ocean_pack(self, config: QWeatherConfig) -> QWeatherOceanPack:
    """创建海洋数据 API包
    
    ```海洋数据API提供全球主要港口和城市的潮汐和潮流数据。```
    """
    
    return QWeatherOceanPack(config)
  
  
  def create_solar_radiation_pack(self, config: QWeatherConfig) -> QWeatherSolarRadiationPack:
    """创建太阳辐射 API包
    
    ```太阳辐射API支持获取全球任意坐标的辐射数据，包括净太阳辐射，太阳散射辐射和太阳直接辐射。```
    """
    
    return QWeatherSolarRadiationPack(config)
  
  
  def create_astronomy_pack(self, config: QWeatherConfig) -> QWeatherAstronomyPack:
    """创建天文API包

    Args:
        config (QWeatherConfig): _description_

    Returns:
        QWeatherAstronomyPack: _description_
    """
    return QWeatherAstronomyPack(config)