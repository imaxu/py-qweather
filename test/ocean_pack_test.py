# coding: utf-8

import unittest
from datetime import datetime, timedelta
from pyqweather import QWeatherConfig
from pyqweather.factories import QWeatherFactory


from pyqweather.auth import EnvironmentVariableSignAuthCredential


class OceanPackTest(unittest.TestCase):
  
  _endpoint = 'https://api.qweather.com/v7'
  
  def test_qweather_ocean_tide(self):
    
    conf = QWeatherConfig(self._endpoint, EnvironmentVariableSignAuthCredential())
    factory = QWeatherFactory()
    pack = factory.create_ocean_pack(conf)
    
    self.assertTrue(pack is not None)
    date = (datetime.now().date() + timedelta(days=3)).strftime('%Y%m%d')
    resp = pack.tide('P2951', date)
    self.assertEqual('200', resp.get_code())
    
    self.assertTrue(resp.tideTable is not None)
    print(resp.tideTable)
    
    
  def test_qweathertime_ocean_currents(self):
    
    conf = QWeatherConfig(self._endpoint, EnvironmentVariableSignAuthCredential())
    factory = QWeatherFactory()
    pack = factory.create_ocean_pack(conf)
    self.assertTrue(pack is not None)
    
    date = (datetime.now().date() + timedelta(days=3)).strftime('%Y%m%d')
    resp = pack.currents('P66981', date)
    self.assertEqual('200', resp.get_code())
    
    self.assertTrue(resp.currentsTable is not None)
    print(resp.currentsTable)
    
    
if __name__ == '__main__':
  
  unittest.main(verbosity=2)