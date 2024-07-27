# coding: utf-8

import unittest
from pyqweather import QWeatherConfig
from pyqweather.factories import QWeatherFactory

from pyqweather.auth import EnvironmentVariableSimpleAuthCredential, EnvironmentVariableSignAuthCredential

class TestMethods(unittest.TestCase):
  
  _domain = 'https://api.qweather.com/v7'
  
  def test_qweather_weather_weather_now(self):
    
    conf = QWeatherConfig(self._domain, EnvironmentVariableSignAuthCredential())
    factory = QWeatherFactory()
    pack = factory.create_weather_pack(conf)
    
    self.assertTrue(pack is not None)
    
    resp = pack.weather_now('101010100')
    self.assertEqual('200', resp.get_code())
    
    self.assertTrue(resp.now is not None)
    
    
if __name__ == '__main__':
  
  unittest.main(verbosity=2)