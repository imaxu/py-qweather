import unittest

from air_pack_test import AirPackTest
from airquality_pack_test import AirQualityPackTest
from astronomy_pack_test import AstronomyPackTest
from geo_pack_test import GeoPackTest
from grid_weather_pack_test import GridWeatherPackTest
from indices_pack_test import IndicesPackTest
from minutely_pack_test import MinutelyPackTest
from ocean_pack_test import OceanPackTest
from solar_radiation_pack_test import SolarRadiationPackTest
from time_machine_pack_test import TimeMachinePackTest
from tropical_cyclone_pack_test import TropicalCyclonePackTest
from weather_pack_test import WeatherPackTest
from weather_warning_pack_test import WeatherWarningPackTest


if __name__ == '__main__':
  
  unittest.main(verbosity=2)