
from pyqweather import QWeatherRequestBase, QWeatherResponseBase
from pyqweather.packages import QWeatherWeatherDataDto
from dataclasses import dataclass


class GridWeatherNowRequest(QWeatherRequestBase):

    _PATH = '/grid-weather/now'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.location = self.get_arg('location', kwargs, required=True)
        self.lang = self.get_arg('lang', kwargs)
        self.unit = self.get_arg('unit', kwargs)

    def __str__(self) -> str:
        return f'location={self.location}'


@dataclass
class GridWeatherNowResponse(QWeatherResponseBase):

    updateTime: str
    fxLink: str
    now: list[QWeatherWeatherDataDto]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.updateTime = self.get_arg('updateTime', kwargs, None)
        self.fxLink = self.get_arg('fxLink', kwargs, None)
        self.now: QWeatherWeatherDataDto = self.get_obj(
            'now', kwargs, QWeatherWeatherDataDto)
