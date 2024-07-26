# coding : utf-8
from abc import abstractmethod, ABC
from pyqweather.auth import AuthCredentialBase
import requests
from requests import Response


class QWeatherConfig:
  """配置类
  """
  
  def __init__(self, credential:AuthCredentialBase=None):
    self._credential = credential


  def get_credential(self):
    return self._credential


class QWeatherPackBase(ABC):
  """QWeather接口包基类

  """
  
  _URL = ''
  
  def __init__(self, conf:QWeatherConfig):
    self._conf = conf
    
  
  def get_conf(self):
    return self._conf
  
  
class QWeatherRequestBase(ABC):
  """QWeather请求对象
  """
  
  
  _PATH = ''
  
  
  def __init__(self, **kwargs):
    self._kwargs = kwargs
  
  
  def with_url(self, url:str):
    self._url = url
    return self
    
  
  def with_credential(self, credential:AuthCredentialBase=None):
    self._credential = credential
    return self
    
    
  def get_arg(self, name, dict, default=None, required=False):
    arg = dict[name] if name in dict else default
    if required and dict[name] is None :
      raise Exception(f'{name} is required ,but missing now.')
    
    return arg
    
    
  def get(self) -> dict:
    if not self._credential.is_valid():
      raise Exception(f'Auth credential required, but it is empty or None') 
    
    fullurl = f'{self._url}{self._PATH}'
    print(fullurl)
    self._kwargs.update(self._credential.create_sign_param(**self._kwargs))
    resp = requests.get(fullurl, params=self._kwargs)
    
    if resp.status_code != 200:
      raise Exception(f'response status code {resp.status_code}, at {fullurl}')
    
    return resp.json()
    
  
  
class QWeatherResponseBase(ABC):
  
  def __init__(self, **kwargs):
    self.code = self.get_arg('code', kwargs)
    
    
  def get_arg(self, name, dict, default=None):
    return dict[name] if name in dict else default
    
    
  def get_code(self) -> str:
    return self.code

  