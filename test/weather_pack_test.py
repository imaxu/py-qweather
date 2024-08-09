# coding: utf-8

import unittest
from pyqweather import QWeatherConfig
from pyqweather.factories import QWeatherFactory

from pyqweather.auth import EnvironmentVariableSignAuthCredential

class WeatherPackTest(unittest.TestCase):
  
  _domain = 'https://api.qweather.com/v7'
  
  def test_qweather_weather_weather_now(self):
    
    conf = QWeatherConfig(self._domain, EnvironmentVariableSignAuthCredential())
    factory = QWeatherFactory()
    pack = factory.create_weather_pack(conf)
    
    self.assertTrue(pack is not None)
    
    resp = pack.weather_now('101010100')
    self.assertEqual('200', resp.get_code())
    
    self.assertTrue(resp.now is not None)
    
    print(resp)
    print(f'当前气压 = {resp.now.pressure} 百帕')
    
    
    
  def test_qweather_weather_weather_daily(self):
    conf = QWeatherConfig(self._domain, EnvironmentVariableSignAuthCredential())
    factory = QWeatherFactory()
    pack = factory.create_weather_pack(conf)
    
    self.assertTrue(pack is not None)
    resp = pack.weather_30d('101010100')
    self.assertEqual('200', resp.get_code())
    
    self.assertTrue(len(resp.daily) == 30)
    
    daily = resp.daily[0]
    print(f'{daily.fxDate}: {daily.pressure} 百帕')
    
    
  def test_qweather_weather_weather_hourly(self):
    conf = QWeatherConfig(self._domain, EnvironmentVariableSignAuthCredential())
    factory = QWeatherFactory()
    pack = factory.create_weather_pack(conf)
    
    self.assertTrue(pack is not None)
    resp = pack.weather_168h('101010100')
    self.assertEqual('200', resp.get_code())
    
    self.assertTrue(len(resp.hourly) == 168)
    
    hourly = resp.hourly[0]
    print(f'{hourly.fxTime}: {hourly.pressure} 百帕')
    
    
if __name__ == '__main__':
  
  unittest.main(verbosity=2)