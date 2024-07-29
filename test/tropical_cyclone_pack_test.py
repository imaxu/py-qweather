# coding: utf-8

import unittest
from datetime import datetime, timedelta
from pyqweather import QWeatherConfig
from pyqweather.factories import QWeatherFactory


from pyqweather.auth import EnvironmentVariableSignAuthCredential


class TestMethods(unittest.TestCase):
  
  _endpoint = 'https://api.qweather.com/v7'
  
  def test_qweather_tropical_cyclone_storm_forecast(self):
    
    conf = QWeatherConfig(self._endpoint, EnvironmentVariableSignAuthCredential())
    factory = QWeatherFactory()
    pack = factory.create_tropical_cyclone_pack(conf)
    
    self.assertTrue(pack is not None)
    

    resp = pack.storm_forecast('NP_2403')
    self.assertEqual('200', resp.get_code())
    
    self.assertTrue(resp.forecast is not None)
    
    
  def test_qweathertime_tropical_cyclone_storm_track(self):
    
    conf = QWeatherConfig(self._endpoint, EnvironmentVariableSignAuthCredential())
    factory = QWeatherFactory()
    pack = factory.create_tropical_cyclone_pack(conf)
    
    self.assertTrue(pack is not None)
    resp = pack.storm_track('NP_2403')
    self.assertEqual('200', resp.get_code())
    
    self.assertTrue(resp.isActive is not None)
    print(f'isActive = {resp.isActive}')
    
    
  def test_qweathertime_tropical_cyclone_storm_list(self):
    
    conf = QWeatherConfig(self._endpoint, EnvironmentVariableSignAuthCredential())
    factory = QWeatherFactory()
    pack = factory.create_tropical_cyclone_pack(conf)
    
    self.assertTrue(pack is not None)
    resp = pack.storm_list('2024')
    self.assertEqual('200', resp.get_code())
    
    self.assertTrue(resp.storm is not None)
    print(resp.storm[0].name)
    

    
    
if __name__ == '__main__':
  
  unittest.main(verbosity=2)