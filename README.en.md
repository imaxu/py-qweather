# pyqweather
**QWeather api for python3。**

## Setup

```bash
pip install pyqweather
```



## Ready
通过和风天气官网获取开发Key [如何获取你的Key](https://dev.qweather.com/docs/configuration/project-and-key/)


## Easy to go
Call the "City Lookup" API

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


###  Set Environment Variable With App Key

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

#### Invoke API With Environment Variable

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

### <span style="color:#F44336">Notice</span>

Currently, only **Simple KEY Authentication** is supported for calling the air quality (Beta) interface. Using a digital signature will result in an error.

Example of using simple KEY authentication:

```python
conf = QWeatherConfig(self._domain,EnvironmentVariableSimpleAuthCredential())
factory = QWeatherFactory()
pack = factory.create_airquality_pack(conf)
resp = pack.airquality_now('101090101')
print(resp.aqi)
```

## API Mapping

Corresponding to the [interface list](https://dev.qweather.com/docs/api/) on the official website, the component also defines the corresponding Package class. You can always create the corresponding API class through the factory method ```QWeatherFactory().create_xxx()``` (xxx represents the Package in the table below).

The specific corresponding relationships are shown in the following table:



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


## More

### [Office Document](https://dev.qweather.com/docs/start/)