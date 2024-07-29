# coding: utf-8

import unittest
from pyqweather.auth import \
  EnvironmentVariableSignAuthCredential,  \
    EnvironmentVariableSimpleAuthCredential,\
      SimpleAuthCredential, \
        SignAuthCredential


class TestStringMethods(unittest.TestCase):

  def test_qweather_simple_auth_credential(self):
    auth_credential = SimpleAuthCredential('1234')
    self.assertEqual(auth_credential.create_sign_param(arg1='arg1')['key'], '1234')


  def test_qweather_env_simple_auth_credential(self):
    auth_credential = EnvironmentVariableSimpleAuthCredential()
    self.assertTrue('key' in auth_credential.create_sign_param(arg1='arg1'))


  def test_qweather_sign_auth_credential(self):
    auth_credential = SignAuthCredential('1234567890', '1234')
    self.assertTrue('cff8bb3d71419d50618331b63388dca1' in auth_credential.create_sign_param(arg1='arg1')['sign'])


  def test_qweather_env_sign_auth_credential(self):
    auth_credential = EnvironmentVariableSignAuthCredential()
    self.assertTrue('c344388ac19d577e5ebbbaaf894581af' in auth_credential.create_sign_param(arg1='arg1')['sign'])


if __name__ == '__main__':
  
  unittest.main()
  