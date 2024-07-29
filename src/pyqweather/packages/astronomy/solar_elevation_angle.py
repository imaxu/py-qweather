
from pyqweather import QWeatherRequestBase, QWeatherResponseBase

class AstronomySolarElevationAngleRequest(QWeatherRequestBase):
  
  _PATH = '/astronomy/solar-elevation-angle'
  
  def __init__(self, **kwargs):
    
    super().__init__(**kwargs)
    self.location       = self.get_arg('location', kwargs, required=True)
    self.date           = self.get_arg('date', kwargs, required=True)
    self.time           = self.get_arg('time', kwargs, required=True)
    self.tz             = self.get_arg('tz', kwargs, required=True)
    self.alt            = self.get_arg('alt', kwargs, required=True)
    
  def __str__(self) -> str:
    return f'location={self.location}'
  

class AstronomySolarElevationAngleResponse(QWeatherResponseBase):
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.updateTime               = self.get_arg('updateTime', kwargs, None)
    self.solarElevationAngle      = self.get_arg('solarElevationAngle', kwargs, None)
    self.solarAzimuthAngle        = self.get_arg('solarAzimuthAngle', kwargs, None)
    self.solarHour                = self.get_arg('solarHour', kwargs, None)
    self.hourAngle                = self.get_arg('hourAngle', kwargs, None)
    