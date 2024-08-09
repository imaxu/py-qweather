# coding: utf-8

import unittest
from pyqweather import QWeatherConfig
from pyqweather.factories import QWeatherFactory

from pyqweather.auth import EnvironmentVariableSignAuthCredential

class WeatherWarningPackTest(unittest.TestCase):
  
  _domain = 'https://api.qweather.com/v7'
  
  def test_qweather_weather_warning_now(self):
    
    conf = QWeatherConfig(self._domain, EnvironmentVariableSignAuthCredential())
    factory = QWeatherFactory()
    pack = factory.create_weather_warning_pack(conf)
    
    self.assertTrue(pack is not None)
    
    resp = pack.warning_now('101090101')
    self.assertEqual('200', resp.get_code())
    
    self.assertTrue(resp.warning is not None)
    
    if len(resp.warning) > 0:
      print(f'第一个预警： {resp.warning[0].text}')
    
    
    
  def test_qweather_weather_warning_list(self):
    conf = QWeatherConfig(self._domain, EnvironmentVariableSignAuthCredential())
    factory = QWeatherFactory()
    pack = factory.create_weather_warning_pack(conf)
    
    self.assertTrue(pack is not None)
    resp = pack.warning_list('cn')
    self.assertEqual('200', resp.get_code())
    
    self.assertTrue(resp.warningLocList is not None)
    
    if len(resp.warningLocList) > 0:
      print(f'预警的区域： {resp.warningLocList[0].locationId}')

    
    
if __name__ == '__main__':
  
  unittest.main(verbosity=2)