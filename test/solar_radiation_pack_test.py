# coding: utf-8

import unittest
from datetime import datetime, timedelta
from pyqweather import QWeatherConfig
from pyqweather.factories import QWeatherFactory


from pyqweather.auth import EnvironmentVariableSignAuthCredential


class SolarRadiationPackTest(unittest.TestCase):
  
  _endpoint = 'https://api.qweather.com/v7'
  
  def test_qweather_solar_radiation_hourly(self):
    
    conf = QWeatherConfig(self._endpoint, EnvironmentVariableSignAuthCredential())
    factory = QWeatherFactory()
    pack = factory.create_solar_radiation_pack(conf)
    
    self.assertTrue(pack is not None)
    resp = pack.hourly_72h('116.41,39.92')
    self.assertEqual('200', resp.get_code())
    
    self.assertTrue(resp.radiation is not None)
    print(f'{resp.radiation[0].net} W/m2')
    

    
    
if __name__ == '__main__':
  
  unittest.main(verbosity=2)