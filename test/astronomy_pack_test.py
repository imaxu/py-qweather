# coding: utf-8

import unittest
from datetime import datetime, timedelta
from pyqweather import QWeatherConfig
from pyqweather.factories import QWeatherFactory

from pyqweather.auth import EnvironmentVariableSignAuthCredential


class AstronomyPackTest(unittest.TestCase):
  
  _domain = 'https://api.qweather.com/v7'
  
  def test_qweather_astronomy_sun(self):
    
    conf = QWeatherConfig(self._domain, EnvironmentVariableSignAuthCredential())
    factory = QWeatherFactory()
    pack = factory.create_astronomy_pack(conf)
    
    self.assertTrue(pack is not None)
    
    date = (datetime.now().date() + timedelta(days=3)).strftime('%Y%m%d')
    resp = pack.sun('101090101', date)
    self.assertEqual('200', resp.get_code())
    
    self.assertTrue(resp.sunrise is not None)
    print(resp.sunrise)
    
    
  def test_qweather_astronomy_moon(self):
    
    conf = QWeatherConfig(self._domain, EnvironmentVariableSignAuthCredential())
    factory = QWeatherFactory()
    pack = factory.create_astronomy_pack(conf)
    
    self.assertTrue(pack is not None)
    
    date = (datetime.now().date() + timedelta(days=3)).strftime('%Y%m%d')
    resp = pack.moon('101090101', date)
    self.assertEqual('200', resp.get_code())
    
    self.assertTrue(resp.moonPhase is not None)
    print(resp.moonPhase[0].name)
    
    
  def test_qweather_astronomy_solar_elevation_angle(self):
    
    conf = QWeatherConfig(self._domain, EnvironmentVariableSignAuthCredential())
    factory = QWeatherFactory()
    pack = factory.create_astronomy_pack(conf)
    
    self.assertTrue(pack is not None)
    
    date = (datetime.now().date() + timedelta(days=3)).strftime('%Y%m%d')
    resp = pack.solar_elevation_angle('120.34,36.08', date, time='1230', alt='43')
    self.assertEqual('200', resp.get_code())
    
    self.assertTrue(resp.solarHour is not None)
    print(resp.solarHour)
    

    
    
if __name__ == '__main__':
  
  unittest.main(verbosity=2)