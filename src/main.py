from thermostat import Thermostat
from relay_controller import RelayController



def main():
    home_thermostat = Thermostat()
    try:
        home_thermostat.run()
    except Exception as e:
        print('An Exception Occured!')
        print(e.message)
    finally:
        home_thermostat.shutdown()


if __name__ == "__main__":
    main()
