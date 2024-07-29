
from pyqweather import QWeatherRequestBase, QWeatherResponseBase
from pyqweather.packages import QWeatherAirQualityAQIDto, QWeatherAirQualityPollutantDto, QWeatherAirQualityStationDto


class AirQualityNowRequest(QWeatherRequestBase):
  
  _PATH = '/now'
  
  def __init__(self, locationId:str,  **kwargs):
    super().__init__(**kwargs)
    self.locationId = locationId
    # self.pollutant = self.get_arg('pollutant', kwargs, False)
    # self.station = self.get_arg('station', kwargs, True)
    self.lang = self.get_arg('lang', kwargs)
    
    self._PATH = f'/now/{self.locationId}'
    
    
  def __str__(self) -> str:
    return f'location={self.location}'
  


class AirQualityNowResponse(QWeatherResponseBase):
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.updateTime = self.get_arg('updateTime', kwargs, None)
    self.aqi:list[QWeatherAirQualityAQIDto] = self.get_items('aqi', kwargs, QWeatherAirQualityAQIDto)
    self.pollutant:list[QWeatherAirQualityPollutantDto] = self.get_items('pollutant', kwargs, QWeatherAirQualityPollutantDto)
    self.station:list[QWeatherAirQualityStationDto] = self.get_items('station', kwargs, QWeatherAirQualityStationDto)
    
    