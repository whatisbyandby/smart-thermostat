import datetime

schedule = {
    "Monday": [{"time": 600, "temp": 71.0}, {"time": 2200, "temp": 67.0}],
    "Tuesday": [{"time": 600, "temp": 71.0}, {"time": 2200, "temp": 67.0}],
    "Wednesday": [{"time": 600, "temp": 71.0}, {"time": 2200, "temp": 67.0}],
    "Thursday": [{"time": 600, "temp": 71.0}, {"time": 2200, "temp": 67.0}],
    "Friday": [{"time": 600, "temp": 71.0}, {"time": 2200, "temp": 67.0}],
    "Saturday": [{"time": 600, "temp": 71.0}, {"time": 2200, "temp": 67.0}],
    "Sunday": [{"time": 600, "temp": 71.0}, {"time": 2200, "temp": 67.0}]
}

 
class ScheduleController:
    def __init__(self, thermostat):
        self.thermostat = thermostat
        self.days_of_the_week = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
        
    def get_day_of_the_week(self):
        now = datetime.datetime.now()
        print(self.days_of_the_week[now.weekday()])

    def get_temperature(self):
        now = datetime.datetime.now()
        schedule_day = schedule[self.days_of_the_week[now.weekday()]]
        temp = None
        for cur_schedule in schedule_day:
            print(cur_schedule["time"], now.hour * 100)
            if now.hour * 100 >= cur_schedule["time"]:
                temp = cur_schedule["temp"]
        return temp
        

if __name__ == "__main__":
    controller = ScheduleController()
    controller.get_day_of_the_week()
    print(controller.get_temperature())

