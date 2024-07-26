# coding: utf-8

import unittest
from pyqweather import QWeatherConfig
from pyqweather.factories import QWeatherFactory

from pyqweather.auth import EnvironmentVariableSimpleAuthCredential

class TestMethods(unittest.TestCase):
  
  
  def test_qweather_weather_weather_now(self):
    
    conf = QWeatherConfig(EnvironmentVariableSimpleAuthCredential())
    factory = QWeatherFactory()
    pack = factory.create_weather_pack(conf)
    
    self.assertTrue(pack is not None)
    
    resp = pack.weather_now('101010100')
    self.assertEqual('200', resp.get_code())
    
    self.assertTrue(resp.now is not None)
    
    
if __name__ == '__main__':
  
  unittest.main(verbosity=2)