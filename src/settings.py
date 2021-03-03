# import json

# class Settings(object):
#     _instance = None

#     def __new__(cls):
#         if cls._instance is None:
#             with open('config.json', 'r') as json_file:
#                 data = json.load(json_file)
#                 cls._instance = super(Settings, cls).__new__(cls)
#                 cls.mqtt = data['mqtt']
#                 cls.temperature_controller = data['temperature_controller']
        
#         return cls._instance

#     @classmethod
#     def commit_settings(cls, settings):
#         cls.mqtt = settings.mqtt
#         cls.temperature_controller = settings.temp_controller
#         with open('./config/config.json', 'w') as json_file:
#             json.dump(cls, json_file)
