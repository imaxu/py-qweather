
from abc import abstractmethod, ABC
import hashlib
import os
import time


class AuthCredentialBase(ABC):

  def __init__(self, **kwargs):
    self._kwargs = kwargs

  @abstractmethod
  def is_valid(self) -> bool:
    return True

  @abstractmethod
  def create_sign_param(self, **kwargs) -> dict[str, str]:
    return {}
  


class SimpleAuthCredential(AuthCredentialBase):
  """简单认证凭据， 直接使用ApiKey

  Args:
      AuthCredentialBase (_type_): _description_
  """

  def __init__(self, app_key: str):
    super().__init__(app_key=app_key)
    
    self.app_key = app_key

  def is_valid(self):
    return super().is_valid() and self.app_key is not None and len(self.app_key) > 0

  def create_sign_param(self, **kwargs) -> dict[str, str]:
    return {'key': self.app_key }


class EnvironmentVariableSimpleAuthCredential(SimpleAuthCredential):
  
  def __init__(self):
    super().__init__(os.getenv('QWEATHER_SDK_APP_KEY', ''))



class SignAuthCredential(AuthCredentialBase):
  """数字签名认证凭据

  Args:
      AuthCredentialBase (_type_): _description_
  """

  def __init__(self, public_id: str, app_key: str):
    super().__init__(public_id=public_id, app_key=app_key)
    self.app_key = app_key
    self.public_id = public_id
    self.t = int(time.time())

  def _generate_signature(self, parameters: dict[str, str | int]):
    """
    生成签名的函数。
    :param parameters: 包含请求参数的字兂数组
    :param api_key: 用于签名的API密钥
    :return: 生成的签名
    """
    
    parameters.update({'t': self.t, 'publicid': self.public_id})
    
    # 1. 将请求参数格式化为“key=value”格式
    key_value_pairs = [f"{key}={value}" for key, value in parameters.items() if value]
    
    # 2. 去除请求参数中值为空的参数（已在上一步完成）
    # 3. 去除请求参数中参数为'sign'的参数
    key_value_pairs = [item for item in key_value_pairs if not item.startswith('sign=')]
    
    # 4. 将剩余的键值对以字典序升序排列，并用'&'符号连接
    key_value_pairs.sort()
    sorted_str = '&'.join(key_value_pairs)
    # 5. 将排好序的字符串后拼接上API密钥
    string_to_sign = f'{sorted_str}{self.app_key}'
    # 6. 将得到的字符串进行MD5加密
    md5_hash = hashlib.md5()
    #print(string_to_sign)
    md5_hash.update(string_to_sign.encode('utf-8'))
    signature = md5_hash.hexdigest()
    #print(signature)
    
    return signature
  
    
  def is_valid(self):
    return super().is_valid() \
      and self.app_key is not None \
        and len(self.app_key) > 0 \
          and self.public_id is not None \
            and len(self.public_id) > 0
            
            
  def create_sign_param(self, **kwargs):
    return { 'sign' : self._generate_signature(kwargs), 't': self.t, 'publicid': self.public_id }  
  
  
class EnvironmentVariableSignAuthCredential(SignAuthCredential):
  
  def __init__(self):
    super().__init__(os.getenv('QWEATHER_SDK_PUBLIC_ID', ''), os.getenv('QWEATHER_SDK_APP_KEY', ''))