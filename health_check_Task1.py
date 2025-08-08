import json
import sys

def get_abnormal_components(data):
    abnormal = []
    sensors_info = data.get("sensors_info", {})
    for sensor_name, sensor_data in sensors_info.items():
        # Check GPS
        if not sensor_data.get("gps_signal_good", False):
            abnormal.append(f"Sensor {sensor_name} - GPS")
        # Check WIFI
        if sensor_data.get("wifi_status", "") != "connected":
            abnormal.append(f"Sensor {sensor_name} - WIFI")
        # Check Engine
        mgmt_details = sensor_data.get("mgmt_details", {})
        for module_name, module_data in mgmt_details.items():
            if module_data.get("engine_status", "") != "connected":
                abnormal.append(f"Sensor {sensor_name} - Engine ({module_name})")
    return abnormal

def fetch_data_from_file():
    try:
        with open(r"Enter your json location here from local folder", "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error fetching data from file: {e}")
        return None

def health_check():
    data = fetch_data_from_file()
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