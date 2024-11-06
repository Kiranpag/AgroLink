import requests

def control_irrigation(sensor_data):
    threshold = 30
    if sensor_data["moisture"] < threshold:
        requests.post("http://iot-device.local/control", json={"action": "start"})
    else:
        requests.post("http://iot-device.local/control", json={"action": "stop"})
