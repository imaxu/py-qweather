# coding: utf-8

import unittest
from pyqweather import QWeatherConfig
from pyqweather.factories import QWeatherFactory

from pyqweather.auth import EnvironmentVariableSignAuthCredential


class AirPackTest(unittest.TestCase):
  
  _domain = 'https://api.qweather.com/v7'
  
  def test_qweather_air_now(self):
    
    conf = QWeatherConfig(self._domain, EnvironmentVariableSignAuthCredential())
    factory = QWeatherFactory()
    pack = factory.create_air_pack(conf)
    
    self.assertTrue(pack is not None)
    
    resp = pack.air_now('101090101')
    self.assertEqual('200', resp.get_code())
    
    self.assertTrue(resp.now is not None)
    print(resp.now.pm2p5)
    
    
  def test_qweather_air_5d(self):
    
    conf = QWeatherConfig(self._domain, EnvironmentVariableSignAuthCredential())
    factory = QWeatherFactory()
    pack = factory.create_air_pack(conf)
    
    self.assertTrue(pack is not None)
    
    resp = pack.air_5d('101090101')
    self.assertEqual('200', resp.get_code())
    
    self.assertTrue(resp.daily is not None)
    print(resp.daily[0].aqi)
    

    
    
if __name__ == '__main__':
  
  unittest.main(verbosity=2)