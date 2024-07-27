# coding: utf-8

import unittest
from pyqweather import QWeatherConfig
from pyqweather.factories import QWeatherFactory

from pyqweather.auth import EnvironmentVariableSignAuthCredential

class TestMethods(unittest.TestCase):
  
  _domain = 'https://api.qweather.com/v7'
  
  def test_qweather_grid_weather_now(self):
    
    conf = QWeatherConfig(self._domain, EnvironmentVariableSignAuthCredential())
    factory = QWeatherFactory()
    pack = factory.create_grid_weather_pack(conf)
    
    self.assertTrue(pack is not None)
    
    resp = pack.grid_weather_now('116.41,39.92')
    self.assertEqual('200', resp.get_code())
    
    self.assertTrue(resp.now is not None)
    
    
    
  def test_qweather_grid_weather_daily(self):
    conf = QWeatherConfig(self._domain, EnvironmentVariableSignAuthCredential())
    factory = QWeatherFactory()
    pack = factory.create_grid_weather_pack(conf)
    
    self.assertTrue(pack is not None)
    resp = pack.grid_weather_7d('116.41,39.92')
    self.assertEqual('200', resp.get_code())
    
    self.assertTrue(len(resp.daily) == 7)
    
    
  def test_qweather_grid_weather_hourly(self):
    conf = QWeatherConfig(self._domain, EnvironmentVariableSignAuthCredential())
    factory = QWeatherFactory()
    pack = factory.create_grid_weather_pack(conf)
    
    self.assertTrue(pack is not None)
    resp = pack.grid_weather_72h('116.41,39.92')
    self.assertEqual('200', resp.get_code())
    self.assertTrue(len(resp.hourly) >= 70)
    
    
if __name__ == '__main__':
  
  unittest.main(verbosity=2)