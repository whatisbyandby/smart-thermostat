from thermostat import Thermostat
from relay_controller import RelayController
from server import create_server, update_server
from threading import Thread



def main():
    home_thermostat = Thermostat(update_server)
    thermostat_server = create_server(home_thermostat.update_set_temperature)
    try:
        thermostat_thread = Thread(target=home_thermostat.run)
        #server_thread.daemon = True
        thermostat_thread.start()
        thermostat_server.run(host='0.0.0.0')
    except Exception as e:
        print('An Exception Occured!')
        print(e.message)
    finally:
        home_thermostat.shutdown()


if __name__ == "__main__":
    main()
