# coding: utf-8

import unittest
from pyqweather import QWeatherConfig
from pyqweather.factories import QWeatherFactory

from pyqweather.auth import EnvironmentVariableSignAuthCredential
from pyqweather.packages import INDICES_TYPE


class TestMethods(unittest.TestCase):
  
  _domain = 'https://api.qweather.com/v7'
  
  def test_qweather_indices_daily(self):
    
    conf = QWeatherConfig(self._domain, EnvironmentVariableSignAuthCredential())
    factory = QWeatherFactory()
    pack = factory.create_indices_pack(conf)
    
    self.assertTrue(pack is not None)
    
    resp = pack.indices_3d('101090101', INDICES_TYPE.TRA.value)
    self.assertEqual('200', resp.get_code())
    
    self.assertTrue(resp.daily is not None)
    print(resp.daily)
    

    
    
if __name__ == '__main__':
  
  unittest.main(verbosity=2)