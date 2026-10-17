# In-Bed Patient Restlessness & Sleep State Analyzer
import numpy as np

class InBedRestlessnessTracker:
    def __init__(self, bed_box, movement_threshold_px=20, sleep_timeout_sec=60):
        self.bed_box = bed_box
        self.thresh = movement_threshold_px
        self.sleep_timeout = sleep_timeout_sec
        self.last_center = None
        self.seconds_since_move = 0.0

    def update(self, person_center, dt=0.033):
        if self.last_center is None:
            self.last_center = person_center
            return "SLEEPING"

        dist = np.linalg.norm(np.array(person_center) - np.array(self.last_center))
        if dist > self.thresh:
            self.seconds_since_move = 0.0
            self.last_center = person_center
            return "RESTLESS_AGITATED"
        else:
            self.seconds_since_move += dt
            if self.seconds_since_move >= self.sleep_timeout:
                return "SLEEPING"
            return "QUIET_REST"

if __name__ == "__main__":
    tracker = InBedRestlessnessTracker(bed_box=[100, 100, 500, 400])
    print("In-Bed Patient Restlessness Tracker initialized.")
