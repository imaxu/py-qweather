
#coding: utf-8

import json

class QWeatherDtoEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, object):
            return object.__dict__
        return json.JSONEncoder.default(self, obj)