from enum import Enum

class UnitRegion(Enum):
    US = 1
    EU = 2
    

class UnitController:
    def __init__(self, region=UnitRegion.US):
        self.region = region

    @staticmethod
    def convert_c_to_f(temp_c):
        temp_f = temp_c * (9/5)
        temp_f = temp_f + 32
        return temp_f

    @staticmethod
    def convert_f_to_c(temp_f):
        temp_c = temp_f - 32
        temp_c = temp_c * (5/9)
        return temp_c

    def convert(self, data_dict):
        if self.region == UnitRegion.US:
            data_dict['temperature'] = self.convert_c_to_f(data_dict['temperature'])
            return data_dict
        return data_dict
