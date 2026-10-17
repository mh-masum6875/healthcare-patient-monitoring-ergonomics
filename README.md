# Patient Monitoring and Workplace Ergonomics Vision

[![Healthcare AI](https://img.shields.io/badge/Application-Patient%20Monitoring%20%26%20Safety-red)](https://github.com/mh-masum6875/healthcare-patient-monitoring-ergonomics)
[![Ergonomics](https://img.shields.io/badge/Ergonomics-Posture%20Assessment-green)](https://github.com/mh-masum6875/healthcare-patient-monitoring-ergonomics)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8+-5C3EE8?logo=opencv&logoColor=white)](https://opencv.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A non-invasive vision intelligence system designed for hospital wards, elderly care environments, and corporate ergonomics monitoring.

---

## Core Clinical & Ergonomic Capabilities

### 1. In-Bed Patient Agitation & Restlessness Tracking (`inbed_restlessness_tracker.py`)
- Automatically identifies patient bed boundaries.
- **Centroid Displacement Tracking**: Measures patient centroid motion vectors over temporal windows:
  $$\Delta d = \sqrt{(C_{x, t} - C_{x, t-1})^2 + (C_{y, t} - C_{y, t-1})^2}$$
  - $\Delta d > 20\text{px}$: Flags patient as **Restless / Agitated**.
  - Inactivity $\ge 60\text{s}$: Flags patient as **Resting / Sleeping**.

### 2. Bed-Exit Fall Prevention & Bathroom Departure Alerting (`bed_fall_monitor.py`)
- Bounding-box aspect ratio calculation detecting when a patient moves from horizontal lying to sitting or ground collapse (Aspect ratio $\frac{W}{H} > 1.5$).
- Tracks unassisted departure beyond clinical perimeter lines towards wet bathroom zones.

### 3. Workplace Sitting & Ergonomic Posture Monitoring (`ergonomic_sitting_detector.py`)
- Evaluates torso-to-chair angle and slouching duration, providing automated wellness and posture prompts for desk workers.

---

## Quickstart

```bash
git clone https://github.com/mh-masum6875/healthcare-patient-monitoring-ergonomics.git
cd healthcare-patient-monitoring-ergonomics
pip install -r requirements.txt

# Run In-Bed Patient Monitor
python src/inbed_restlessness_tracker.py --source patient_room.mp4
```

---

## License
This project is licensed under the MIT License.
