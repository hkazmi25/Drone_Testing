import json
import time
from datetime import datetime

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
    return set(abnormal)

def fetch_data_from_file():
    try:
        with open(r"Enter your json location here from local folder", "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error fetching data from file: {e}")
        return None

def monitor_health(duration_minutes=10, interval_seconds=60):
    previous_abnormal = set()
    start_time = time.time()
    duration = duration_minutes * 60
    while time.time() - start_time < duration:
        data = fetch_data_from_file()
        if data:
            current_abnormal = get_abnormal_components(data)
            new_abnormal = current_abnormal - previous_abnormal
            if new_abnormal:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                for component in new_abnormal:
                    print(f"Component '{component}' became abnormal at {timestamp}")
            previous_abnormal = current_abnormal
        time.sleep(interval_seconds)

if __name__ == "__main__":
    monitor_health()