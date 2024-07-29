
from pyqweather import QWeatherRequestBase, QWeatherResponseBase
from pyqweather.packages import QWeatherAirQualityStationPollutantDto


class AirQualityStationRequest(QWeatherRequestBase):
  
  _PATH = '/station'
  
  def __init__(self, locationId:str,  **kwargs):
    super().__init__(**kwargs)
    self.locationId = locationId
    self.lang = self.get_arg('lang', kwargs)
    
    self._PATH = f'/station/{self.locationId}'
    
    
  def __str__(self) -> str:
    return f'location={self.location}'
  


class AirQualityStationResponse(QWeatherResponseBase):
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.updateTime = self.get_arg('updateTime', kwargs, None)
    self.pollutant:list[QWeatherAirQualityStationPollutantDto] = self.get_items('pollutant', kwargs, QWeatherAirQualityStationPollutantDto)
    