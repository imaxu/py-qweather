# pyqweather
和风天气 api for python3。

[![Supported Versions](https://img.shields.io/badge/python-&nbsp;&nbsp;3.10&nbsp;|&nbsp;3.11&nbsp;|&nbsp;3.12&nbsp;-blue)](https://pypi.org/project/pyqweather/)

## 安装

使用pip

```console
pip install pyqweather
```



## 前置条件
通过和风天气官网获取开发Key [如何获取你的Key](https://dev.qweather.com/docs/configuration/project-and-key/)


## 快速使用
调用“城市搜索”接口

```python
# coding:utf-8
from pyqweather import QWeatherConfig
from pyqweather.auth import SimpleAuthCredential
from pyqweather.factories import QWeatherFactory

endpoint = 'https://geoapi.qweather.com/v2'
auth_credential = SimpleAuthCredential('key')
conf = QWeatherConfig(endpoint, auth_credential)
pack = QWeatherFactory().create_geo_pack(conf)
resp = pack.city_lookup('北京')

if resp.get_code() == '200':
  print('OK')
else:
  print('Error')
```


### 使用App Key设置环境变量

#### Mac OS X/Linux/Unix

```bash
export QWEATHER_SDK_APP_KEY=<Your App Key>
export QWEATHER_SDK_PUBLIC_ID=<Your PublicId>
```

#### Windows

```shell
set QWEATHER_SDK_APP_KEY=<Your App Key>
set QWEATHER_SDK_PUBLIC_ID=<Your PublicId>
```

#### 通过环境变量进行接口调用

```python
# coding:utf-8
from pyqweather import QWeatherConfig
from pyqweather.auth import EnvironmentVariableSignAuthCredential
from pyqweather.factories import QWeatherFactory

endpoint = 'https://geoapi.qweather.com/v2'
conf = QWeatherConfig(endpoint, EnvironmentVariableSignAuthCredential()) # 使用数字签名的方式
factory = QWeatherFactory()

pack = factory.create_geo_pack(conf)
resp = pack.city_lookup('北京')

print(resp)
```

### <span style="color:#F44336">特殊的地方</span>

目前仅支持以**简单KEY认证的方式**调用空气质量（Beta）接口， 使用数字签名会报错。

使用简单KEY认证的方式示例：

```python
conf = QWeatherConfig(self._domain,EnvironmentVariableSimpleAuthCredential())
factory = QWeatherFactory()
pack = factory.create_airquality_pack(conf)
resp = pack.airquality_now('101090101')
print(resp.aqi)
```

## 接口的映射

对应官网的[接口列表](https://dev.qweather.com/docs/api/)，组件也定义了相应的Package类， 你总是可以通过工厂方法 ```QWeatherFactory().create_xxx()```的方式创建对应的API类（xxx表示下表的Package）。

具体对应关系如下表所示：



| 接口分组  |  Package   | 
|----------| ---------- |
| GeoAPI | geo_pack |
| 城市天气 | weather_pack |
| 分钟预报 | minutely_pack |
| 格点天气 | grid_weather_pack |
| 预警 | weather_warning_pack |
| 天气指数 |  indices_pack |
| 空气质量(beta) | air_quality_pack | 
| 空气质量 | air_pack |
| 时光机 | time_machine_pack |
| 热带气旋（台风） | tropical_cyclone_pack | 
| 海洋数据 | ocean_pack |
| 太阳辐射 | solar_radiation_pack | 
| 天文 | astronomy_pack |


## 更多内容

### [官方文档](https://dev.qweather.com/docs/start/)