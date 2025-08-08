import json
import sys
import requests

def get_abnormal_components(data):
    abnormal = []
    sensors_info = data.get("sensors_info", {})
    for sensor_name, sensor_data in sensors_info.items():
        if not sensor_data.get("gps_signal_good", False):
            abnormal.append(f"Sensor {sensor_name} - GPS")
        if sensor_data.get("wifi_status", "") != "connected":
            abnormal.append(f"Sensor {sensor_name} - WIFI")
        mgmt_details = sensor_data.get("mgmt_details", {})
        for module_name, module_data in mgmt_details.items():
            if module_data.get("engine_status", "") != "connected":
                abnormal.append(f"Sensor {sensor_name} - Engine ({module_name})")
    return abnormal

def fetch_data_from_api():
    try:
        response = requests.get("https://41e497e9-9dc5-40d1-a1c2-22d8db54d6fd.mock.pstmn.io", timeout=5) #you can generate any api and use here
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None

def health_check():
    data = fetch_data_from_api()
    if data is None:
        sys.exit(1)
    abnormal_components = get_abnormal_components(data)
    if not abnormal_components:
        print("System health check passed. All components are normal.")
        sys.exit(0)
    else:
        for component in abnormal_components:
            print(f"ERROR: Component '{component}' is abnormal.")
        sys.exit(1)

if __name__ == "__main__":
    health_check()