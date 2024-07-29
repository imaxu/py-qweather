#coding : utf-8

from enum import Enum
from abc import ABC

class QWeatherDto(ABC):
  
  def __init__(self, **data):
    self.__dict__.update(data)


class QWeatherReferDto(QWeatherDto):
  sources : str = None
  """原始数据来源，或数据源说明，可能为空"""
  license : str = None
  """数据许可或版权声明，可能为空"""


class QWeatherWeatherDataDto(QWeatherDto):
  """城市天气预报数据"""
  
  obsTime : str = None
  """数据观测时间"""
  temp  : str = None
  """温度，默认单位：摄氏度"""
  feelsLike  : str = None
  """体感温度，默认单位：摄氏度"""
  icon   : str = None
  """天气状况的图标代码"""
  text  : str = None
  """天气状况的文字描述，包括阴晴雨雪等天气状态的描述"""
  wind360  : str = None
  """风向360角度"""
  windDir  : str = None
  """风向"""
  windScale  : str = None
  """风力等级"""
  windSpeed  : str = None
  """风速，公里/小时"""
  humidity  : str = None
  """相对湿度，百分比数值"""
  precip  : str = None
  """过去1小时降水量，默认单位：毫米"""
  pressure  : str = None
  """大气压强，默认单位：百帕"""
  vis  : str = None
  """能见度，默认单位：公里"""
  cloud  : str = None
  """云量，百分比数值。可能为空"""
  dew  : str = None
  """露点温度。可能为空"""
  
  
class QWeatherWeatherDailyDataDto(QWeatherDto):
  """每日天气预报数据"""
  
  fxDate: str = None
  """预报日期"""
  sunrise : str = None
  """ 日出时间，在高纬度地区可能为空"""
  sunset : str = None
  """ 日落时间，在高纬度地区可能为空"""
  moonrise : str = None
  """当天月升时间，可能为空"""
  moonset : str = None
  """当天月落时间，可能为空"""
  moonPhase : str = None
  """月相名称"""
  moonPhaseIcon : str = None
  """月相图标代码"""
  tempMax : str = None
  """预报当天最高温度"""
  tempMin : str = None
  """预报当天最低温度"""
  iconDay : str = None
  """预报白天天气状况的图标代码"""
  textDay : str = None
  """预报白天天气状况文字描述，包括阴晴雨雪等天气状态的描述"""
  iconNight : str = None
  """预报夜间天气状况的图标代码，"""
  textNight : str = None
  """预报晚间天气状况文字描述，包括阴晴雨雪等天气状态的描述"""
  wind360Day : str = None
  """预报白天风向360角度"""
  windDirDay : str = None
  """预报白天风向"""
  windScaleDay : str = None
  """预报白天风力等级"""
  windSpeedDay : str = None
  """预报白天风速，公里/小时"""
  wind360Night : str = None
  """预报夜间风向360角度"""
  windDirNight : str = None
  """预报夜间当天风向"""
  windScaleNight : str = None
  """预报夜间风力等级"""
  windSpeedNight : str = None
  """预报夜间风速，公里/小时"""
  precip : str = None
  """预报当天总降水量，默认单位：毫米"""
  uvIndex : str = None
  """紫外线强度指数"""
  humidity : str = None
  """相对湿度，百分比数值"""
  pressure : str = None
  """大气压强，默认单位：百帕"""
  vis : str = None
  """能见度，默认单位：公里"""
  cloud : str = None
  """云量，百分比数值。可能为空"""


class QWeatherWeatherHourlyDataDto(QWeatherDto):
  """逐小时天气预报数据"""
  
  fxTime: str = None
  """预报时间"""
  temp : str = None
  """温度，默认单位：摄氏度"""
  icon : str = None
  """天气状况的图标代码"""
  text : str = None
  """天气状况的文字描述，包括阴晴雨雪等天气状态的描述"""
  wind360 : str = None
  """ 风向360角度"""
  windDir : str = None
  """风向"""
  windScale : str = None
  """风力等级"""
  windSpeed : str = None
  """风速，公里/小时"""
  humidity : str = None
  """相对湿度，百分比数值"""
  precip : str = None
  """ 当前小时累计降水量，默认单位：毫米"""
  pop : str = None
  """逐小时预报降水概率，百分比数值，可能为空"""
  pressure : str = None
  """大气压强，默认单位：百帕"""
  cloud : str = None
  """云量，百分比数值。可能为空"""
  dew : str = None
  """露点温度。可能为空"""


class QWeatherMinutelyRainDataDto(QWeatherDto):
  """分钟级降水量数据"""
  
  fxTime : str = None
  """预报时间"""
  precip : str = None
  """5分钟累计降水量，单位毫米"""
  type : str = None
  """降水类型：rain = 雨，snow = 雪"""


class QWeatherLocationDto(QWeatherDto):
  """搜索城市返回的地区详情"""
  
  id:str = None
  """地区/城市ID"""
  name:str = None
  """地区/城市名称"""
  lat:str = None
  """地区/城市纬度"""
  lon:str = None
  """地区/城市经度"""
  adm2:str = None
  """地区/城市的上级行政区划名称"""
  adm1:str = None
  """地区/城市所属一级行政区域"""
  country:str =None
  """地区/城市所属国家名称"""
  tz: str = None
  """地区/城市所在时区"""
  utcOffset:str = None
  """地区/城市目前与UTC时间偏移的小时数"""
  isDist:str = None
  """地区/城市是否当前处于夏令时。1 表示当前处于夏令时，0 表示当前不是夏令时。"""
  type:str = None
  """地区/城市的属性"""
  rank :str = None
  """地区评分"""
  fxLink : str = None
  """该地区的天气预报网页链接，便于嵌入你的网站或应用"""


class QWeatherWarningDto(QWeatherDto):
  """天气预警数据"""

  id: str = None
  """本条预警的唯一标识，可判断本条预警是否已经存在"""
  sender : str = None
  """预警发布单位，可能为空"""
  pubTime : str = None
  """预警发布时间"""
  title : str = None
  """预警信息标题"""
  startTime : str = None
  """预警开始时间，可能为空"""
  endTime : str = None
  """预警结束时间，可能为空"""
  status : str = None
  """预警信息的发布状态"""
  severity: str  = None
  """预警严重等级"""
  severityColor : str  = None
  """预警严重等级颜色，可能为空"""
  type : str = None
  """预警类型ID"""
  typeName : str = None
  """预警类型名称"""
  urgency : str = None
  """ 预警信息的紧迫程度，可能为空"""
  certainty : str = None
  """预警信息的确定性，可能为空"""
  text : str = None
  """预警详细文字描述"""
  related : str = None
  """与本条预警相关联的预警ID，当预警状态为cancel或update时返回。可能为空"""


class QWeatherWarningCityDto(QWeatherDto):
  """预警城市信息"""
  locationId : str = None
  """当前国家预警的LocationID"""
  
  
class QWeatherIndicesDailyDto(QWeatherDto):
  """天气指数每日数据"""
  date : str = None
  """预报日期"""
  type : str = None
  """ 生活指数类型ID"""
  name  : str = None
  """生活指数类型的名称"""
  level  : str = None
  """生活指数预报等级"""
  category  : str = None
  """生活指数预报级别名称"""
  text : str = None
  """生活指数预报的详细描述，可能为空"""


class QWeatherAirQualityAQIDto(QWeatherDto):
  """空气质量AQI数据"""
  code :str = None
  """空气质量指数Code"""
  name  :str = None
  """空气质量指数的名字"""
  defaultLocalAqi  :str = None
  """是否是默认/推荐的当地AQI"""
  value  :str = None
  """空气质量指数的值"""
  valueDisplay  :str = None
  """空气质量指数的值的文本显示"""
  level  :str = None
  """空气质量指数等级，可能为空"""
  category  :str = None
  """空气质量指数类别，可能为空"""
  color  :str = None
  """空气质量指数的颜色，RGB格式"""
  primaryPollutant : dict = None
  """ 首要污染物"""
  health : dict = None
  """健康指导"""
  
  
class QWeatherAirQualityPollutantDto(QWeatherDto):
  """空气质量污染物数据"""
  code: str = None
  """污染物的Code"""
  name : str = None
  """ 污染物的名字"""
  fullName : str = None
  """污染物的全称"""
  concentration: any = None
  """污染物的浓度值"""
  subIndex: any = None
  """ 污染物的分指数"""


class QWeatherAirQualityStationDto(QWeatherDto):
  """空气质量（Beta）监测站数据"""
  
  id:str = None
  """AQI相关联的监测站Location ID，可能为空"""
  name: str = None
  """AQI相关联的监测站名称"""
  
  
class QWeatherAirQualityStationPollutantDto(QWeatherDto):
  """空气质量监测站污染物数据"""
  code : str = None
  """污染物的Code"""
  name  : str = None
  """ 污染物的名字"""
  fullName  : str = None
  """污染物的全称"""
  concentration : any = None
  """污染物的浓度"""
  
  
class QWeatherAirRealDataDto(QWeatherDto):
  """空气质量实时数据"""
  pubTime : str = None
  """空气质量数据发布时间"""
  aqi  : str = None
  """空气质量指数"""
  level  : str = None
  """空气质量指数等级"""
  category  : str = None
  """空气质量指数级别"""
  pm10   : str = None
  """ PM10"""
  pm2p5  : str = None
  """ PM2.5"""
  no2  : str = None
  """二氧化氮"""
  so2  : str = None
  """ 二氧化硫"""
  co  : str = None
  """一氧化碳"""
  o3  : str = None
  """臭氧"""
  primary  : str = None
  """空气质量的主要污染物，空气质量为优时，返回值为NA"""

class QWeatherAirStationDataDto(QWeatherDto):
  """空气质量监测站数据"""
  name : str = None
  """监测站名称"""
  id  : str = None
  """监测站ID"""
  pubTime  : str = None
  """空气质量数据发布时间"""
  aqi  : str = None
  """空气质量指数"""
  level  : str = None
  """空气质量指数等级"""
  category  : str = None
  """ 空气质量指数级别"""
  primary  : str = None
  """空气质量的主要污染物，空气质量为优时，返回值为NA"""
  pm10  : str = None
  """PM10"""
  pm2p5  : str = None
  """PM2.5"""
  no2  : str = None
  """ 二氧化氮"""
  so2  : str = None
  """二氧化硫"""
  co  : str = None
  """一氧化碳"""
  o3  : str = None
  """臭氧"""
  

class QWeatherAirDailyDto(QWeatherDto):
  """空气质量每日预报数据"""
  fxDate : str = None
  """预报日期"""
  level : str = None
  """空气质量指数等级"""
  category : str = None
  """空气质量指数级别"""
  primary  : str = None
  """空气质量的主要污染物，空气质量为优时，返回值为NA"""
  aqi  : str = None
  """空气质量指数"""
  
  
class QWeatherSimpleWeatherDto(QWeatherDto):
  """每日天气简单数据"""
  date : str = None
  """当天日期"""
  sunrise  : str = None
  """当天日出时间，在高纬度地区可能为空"""
  sunset  : str = None
  """日落时间，在高纬度地区可能为空"""
  moonrise  : str = None
  """当天月升时间，可能为空"""
  moonset  : str = None
  """当天月落时间，可能为空"""
  moonPhase  : str = None
  """当天月相名称"""
  tempMax  : str = None
  """当天最高温度"""
  tempMin  : str = None
  """当天最低温度"""
  precip : str = None
  """当天总降水量，默认单位：毫米"""
  pressure  : str = None
  """大气压强，默认单位：百帕"""
  humidity  : str = None
  """当天每小时相对湿度，百分比数值"""


class QWeatherSimpleWeatherHourlyDto(QWeatherDto):
  """逐小时天气简单数据"""
  time : str = None
  """当天时间"""
  temp  : str = None
  """ 当天每小时温度，默认单位：摄氏度"""
  icon  : str = None
  """ 当天每小时天气状况的图标代码"""
  text  : str = None
  """当天每小时天气状况的文字描述，包括阴晴雨雪等天气状态的描述"""
  wind360  : str = None
  """ 当天每小时风向360角度"""
  windDir  : str = None
  """当天每小时风向"""
  windScale  : str = None
  """ 当天每小时风力等级"""
  windSpeed  : str = None
  """当天每小时风速，公里/小时"""
  humidity  : str = None
  """当天每小时相对湿度，百分比数值"""
  precip  : str = None
  """当天每小时累计降水量，默认单位：毫米"""
  pressure  : str = None
  """大气压强，默认单位：百帕"""


class QWeatherSimpleAirHourlyDto(QWeatherDto):
  """逐小时空气质量简单数据"""
  pubTime : str = None
  """空气质量数据发布时间"""
  aqi  : str = None
  """空气质量指数"""
  level  : str = None
  """空气质量指数等级"""
  category  : str = None
  """空气质量指数级别"""
  primary  : str = None
  """空气质量的主要污染物，空气质量为优时，返回值为NA"""
  pm10  : str = None
  """PM10"""
  pm2p5  : str = None
  """ PM2.5"""
  no2  : str = None
  """二氧化氮"""
  so2  : str = None
  """二氧化硫"""
  co  : str = None
  """一氧化碳"""
  o3  : str = None
  """臭氧"""


class QWeatherTropicalCycloneForecastDto(QWeatherDto):
  """台风预报数据"""
  fxTime : str = None
  """台风预报时间"""
  lat  : str = None
  """台风所处纬度"""
  lon  : str = None
  """台风所处经度"""
  type  : str = None
  """ 台风类型"""
  pressure  : str = None
  """台风中心气压"""
  windSpeed : str = None
  """台风附近最大风速"""
  moveSpeed  : str = None
  """台风移动速度"""
  moveDir  : str = None
  """台风移动方位"""
  move360  : str = None
  """台风移动方位360度方向"""
  

class QWeatherTropicalCycloneDataDto(QWeatherDto):
  """台风实况数据"""
  pubTime : str = None
  """台风预报时间"""
  lat  : str = None
  """台风所处纬度"""
  lon  : str = None
  """台风所处经度"""
  type  : str = None
  """ 台风类型"""
  pressure  : str = None
  """台风中心气压"""
  windSpeed : str = None
  """台风附近最大风速"""
  moveSpeed  : str = None
  """台风移动速度"""
  moveDir  : str = None
  """台风移动方位"""
  move360  : str = None
  """台风移动方位360度方向"""  
  windRadius30: any  = None
  """当前台风7级风圈信息，可能为空"""
  windRadius50: any = None
  """台风10级风圈信息，可能为空"""
  windRadius64: any = None
  """台风12级风圈信息，可能为空"""
  
  
class   QWeatherTropicalCycloneStormDto(QWeatherDto):
  """台风信息"""
  id : str = None
  """台风ID"""
  stormId  : str = None
  """台风ID"""
  name  : str = None
  """台风名称"""
  basin  : str = None
  """台风所处流域"""
  year  : str = None
  """ 台风所处年份"""
  isActive  : str = None
  """是否为活跃台风。1 活跃台风，0 停编。"""


class QWeatherOceanTideDto(QWeatherDto):
  """潮汐数据"""
  fxTime : str = None
  height  : str = None
  type  : str = None
  
  
class QWeatherOceanTideHourlyDto(QWeatherDto):
  """潮汐逐小时数据"""
  fxTime : str = None
  height  : str = None
  

class QWeatherOceanCurrentsDto(QWeatherDto):
  """潮流数据"""
  fxTime : str = None
  """潮流最大流速时间"""
  speedMax   : str = None
  """ 潮流最大流速，单位：厘米/秒"""
  dir360   : str = None
  """潮流360度方向"""
  
  
class QWeatherOceanCurrentsHourlyDto(QWeatherDto):
  """潮流逐小时数据"""
  fxTime : str = None
  """潮流逐小时预报时间"""
  speed    : str = None
  """ 潮流流速，单位：厘米/秒"""
  dir360   : str = None
  """潮流360度方向"""
  

class QWeatherSolarRadiationDto(QWeatherDto):
  """太阳辐射数据"""
  fxTime : str = None
  """逐小时预报时间"""
  net : str = None
  """净太阳辐射，W/m2"""
  diffuse : str = None
  """太阳散射辐射，W/m2"""
  direct : str = None
  """太阳直接辐射，W/m2"""
  

class QWeatherMoonPhaseDto(QWeatherDto):
  """月相数据"""
  fxTime : str = None
  """月相逐小时预报时间"""
  value : str = None
  """月相数值"""
  name : str = None
  """月相名称"""
  icon : str = None
  """月相图标代码"""
  illumination : str = None
  """月亮照明度，百分比数值"""

class INDICES_TYPE(Enum):
  """天气指数类型"""
  
  ALL     = '0'
  """全部天气指数"""
  
  SPT     = '1'
  """运动指数"""
  
  CW      = '2'
  """洗车指数"""
  
  DRSG    = '3'
  """穿衣指数"""
  
  FIS     = '4'
  """钓鱼指数"""
  
  UV      = '5'
  """紫外线指数"""
  
  TRA     = '6'
  """旅游指数"""
  
  AG      = '7'
  """花粉过敏指数"""
  
  COMF    = '8'
  """舒适度指数"""
  
  FLU     = '9'
  """感冒指数"""
  
  AP      = '10'
  """空气污染扩散条件指数"""
  
  AC      = '11'
  """空调开启指数"""
  
  GL      = '12'
  """太阳镜指数"""
  
  MU      = '13'
  """化妆指数"""
  
  DC      = '14'
  """晾晒指数"""
  
  PTFC    = '15'
  """交通指数"""
  
  SPI     = '16'
  """防晒指数"""