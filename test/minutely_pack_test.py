# coding: utf-8

import unittest
from pyqweather import QWeatherConfig
from pyqweather.factories import QWeatherFactory

from pyqweather.auth import EnvironmentVariableSignAuthCredential

class TestMethods(unittest.TestCase):
  
  
  _domain = 'https://api.qweather.com/v7'
  
  def test_qweather_weather_minutely_5m(self):
    
    conf = QWeatherConfig(self._domain, EnvironmentVariableSignAuthCredential())
    factory = QWeatherFactory()
    pack = factory.create_minutely_pack(conf)
    
    self.assertTrue(pack is not None)
    
    resp = pack.minutely_5m('116.41,39.92')
    self.assertEqual('200', resp.get_code())
    
    self.assertTrue(len(resp.minutely) ==24)
    
    
if __name__ == '__main__':
  
  unittest.main(verbosity= 2)