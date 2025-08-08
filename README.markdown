# System Health Check and Monitoring

This project includes Python scripts to check and monitor the health of system components (GPS, WIFI, Engine) using data from a JSON file as REST API.

## Scripts
### 0. Json Structure Understanding (`Undersatand_json.py`)
This is just for my learning, how data looks like.

### 1. Health Check (`health_check_Task1.py`)
Checks the health of GPS, WIFI, and Engine components once.

#### How to Run
```bash
python health_check_Task1.py
```

#### Expected Output
- **All components normal**:
  ```
  System health check passed. All components are normal.
  ```
  Exit code: 0
- **Some components abnormal** (e.g., with provided `data.json`):
  ```
ERROR: Component 'Sensor SF1311013350 - GPS' is abnormal.
ERROR: Component 'Sensor SF1311013350 - WIFI' is abnormal.
An exception has occurred, use %tb to see the full traceback.
  ```
  Exit code: 1
- **File error** (e.g., `data.json` missing):
  ```
  Error fetching data from file: [error message]
  ```
  Exit code: 1

### 2. Monitoring (`monitor_health_Task2.py`)
Monitors component health for 10 minutes, reporting new abnormal components with timestamps.

#### How to Run
```bash
python monitor_health_Task2.py
```

#### Expected Output
Try to change the component information mannaully to see the abnormalities while runing the code!
- **New abnormal component detected**:
  ```
Component 'Sensor SF1311013350 - WIFI' became abnormal at 2025-07-09 12:24:30
Component 'Sensor SF1311013350 - GPS' became abnormal at 2025-07-09 12:24:30
  ```
- **File error**:
  ```
  Error fetching data from file: [error message]
  ```

### 3. API Health Check (`health_check_api_Task3.py`)
Checks health using a REST API.

### Used Postman to Create a Mock API
Signup an account here
1. https://www.postman.com/
#### How to Run
1. Created a dummy nested Json file on postman
2. Update the API URL in the script (replace `https://41e497e9-9dc5-40d1-a1c2-22d8db54d6fd.mock.pstmn.io`).
3. Run: `python health_check_api.py`
4. I kept public to i guess you can try to run the code as well

#### Expected Output
-  Similar `health_check.py`, but with API self created dummy errors:
  ```
ERROR: Component 'Sensor Sensor2 - GPS' is abnormal.
ERROR: Component 'Sensor Sensor2 - WIFI' is abnormal.
ERROR: Component 'Sensor Sensor2 - Engine (Module1)' is abnormal.
An exception has occurred, use %tb to see the full traceback.

SystemExit: 1
  ```