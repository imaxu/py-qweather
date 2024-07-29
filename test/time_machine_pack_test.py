# coding: utf-8

import unittest
from datetime import datetime, timedelta
from pyqweather import QWeatherConfig
from pyqweather.factories import QWeatherFactory


from pyqweather.auth import EnvironmentVariableSignAuthCredential


class TestMethods(unittest.TestCase):
  
  _domain = 'https://api.qweather.com/v7'
  
  def test_qweather_time_machine_historical_weather(self):
    
    conf = QWeatherConfig(self._domain, EnvironmentVariableSignAuthCredential())
    factory = QWeatherFactory()
    pack = factory.create_time_machine_pack(conf)
    
    self.assertTrue(pack is not None)
    
    date = (datetime.now().date() - timedelta(days=3)).strftime('%Y%m%d')
    resp = pack.historical_weather('101090101', date)
    self.assertEqual('200', resp.get_code())
    
    self.assertTrue(resp.weatherDaily is not None)
    print(resp.weatherDaily)
    
    
  def test_qweathertime_machine_historical_air(self):
    
    conf = QWeatherConfig(self._domain, EnvironmentVariableSignAuthCredential())
    factory = QWeatherFactory()
    pack = factory.create_time_machine_pack(conf)
    
    self.assertTrue(pack is not None)
    date = (datetime.now().date() - timedelta(days=3)).strftime('%Y%m%d')
    resp = pack.historical_air('101090101', date)
    self.assertEqual('200', resp.get_code())
    
    self.assertTrue(resp.airHourly is not None)
    print(f'aqi = {resp.airHourly[0].aqi}')
    

    
    
if __name__ == '__main__':
  
  unittest.main(verbosity=2)