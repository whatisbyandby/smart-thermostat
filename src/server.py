from quart import Quart, render_template, websocket, request
import asyncio
import json
from decimal import Decimal



app = Quart(__name__, static_url_path='')
update_set_temperature = None

data = {
    "setTemperature": None,
    "currentTemperature": None,
    "humidity": None,
    "mode": None,
    "status": None
}

def create_server(update_function):
    global update_set_temperature
    update_set_temperature = update_function
    return app

def update_server(new_data):
    global data
    data = {
        "setTemperature": new_data.get('set_temperature'),
        "currentTemperature": f"{new_data.get('temperature'):.1f}",
        "humidity": f"{new_data.get('humidity'):.1f}",
        "mode": new_data.get('mode'),
        "status": new_data.get('state')
    }
    #print(data)

@app.route("/", methods=['GET'])
async def handle_root():
    return await app.send_static_file('index.html')


@app.route("/api", methods=['GET', 'POST'])
async def handle_api_request():
    if request.method == 'GET':
        print('Get Request')
    if request.method == 'POST':
        request_data = await request.json
        print(request_data)
        update_set_temperature(request_data.get("setTemperature"))
    return json.dumps(data)

@app.websocket('/ws')
async def handle_ws():
    while True:
        await websocket.send(json.dumps(data))
        await asyncio.sleep(1)

if __name__ == "__main__":
    app.run()