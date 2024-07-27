# coding: utf-8

import unittest
from pyqweather import QWeatherConfig
from pyqweather.factories import QWeatherFactory

from pyqweather.auth import EnvironmentVariableSimpleAuthCredential

class TestStringMethods(unittest.TestCase):


  def test_qweather_config(self):
    
    conf = QWeatherConfig('', EnvironmentVariableSimpleAuthCredential())
    self.assertIsNotNone(conf)


  def test_qweather_factory_create_pack_not_exists(self):
    
    conf = QWeatherConfig('', EnvironmentVariableSimpleAuthCredential())
    factory = QWeatherFactory()
    pack = factory.create_pack('geo1', conf)
    
    self.assertTrue(pack == None)
    
    
  def test_qweather_factory_create_pack(self):
    
    conf = QWeatherConfig('', EnvironmentVariableSimpleAuthCredential())
    factory = QWeatherFactory()
    pack = factory.create_pack('geo', conf)
    
    self.assertTrue(pack is not None)
    
  
    
    

if __name__ == '__main__':
  
  unittest.main()
  