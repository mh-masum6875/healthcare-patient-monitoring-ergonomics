# Bed-Exit Fall and Collapse Monitor
def check_patient_fall(person_box):
    px1, py1, px2, py2 = person_box
    width = px2 - px1
    height = py2 - py1
    aspect_ratio = width / max(1, height)
    # Aspect ratio > 1.5 indicates horizontal ground position outside bed
    return aspect_ratio > 1.5

if __name__ == "__main__":
    print("Bed Fall Monitor initialized.")
