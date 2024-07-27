# coding: utf-8

import unittest
from pyqweather import QWeatherConfig
from pyqweather.factories import QWeatherFactory

from pyqweather.auth import EnvironmentVariableSimpleAuthCredential


class TestMethods(unittest.TestCase):
  
  _domain = 'https://api.qweather.com/airquality/v1'
  
  def test_qweather_airquality_now(self):
    
    conf = QWeatherConfig(self._domain, EnvironmentVariableSimpleAuthCredential())
    factory = QWeatherFactory()
    pack = factory.create_airquality_pack(conf)
    
    self.assertTrue(pack is not None)
    
    resp = pack.airquality_now('101090101')
    self.assertEqual('200', resp.get_code())
    
    self.assertTrue(resp.aqi is not None)
    print(resp.aqi)
    
    
  def test_qweather_airquality_station(self):
    
    conf = QWeatherConfig(self._domain, EnvironmentVariableSimpleAuthCredential())
    factory = QWeatherFactory()
    pack = factory.create_airquality_pack(conf)
    
    self.assertTrue(pack is not None)
    
    resp = pack.airquality_station('P53763')
    self.assertEqual('200', resp.get_code())
    
    self.assertTrue(resp.pollutant is not None)
    print(resp.pollutant)
    

    
    
if __name__ == '__main__':
  
  unittest.main(verbosity=2)