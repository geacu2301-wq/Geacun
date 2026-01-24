def check_hemoglobin():
    sex = input("Enter biological sex (female/male): ").strip().lower()
    hb = float(input("Enter hemoglobin value (g/l): "))

    if sex == "female":
        low, high = 117.0, 155.0
    elif sex == "male":
        low, high = 134.0, 167.0
    else:
        print("Invalid sex")
        return

    if hb < low:
        print("Hemoglobin level is low.")
    elif hb > high:
        print("Hemoglobin level is high.")
    else:
        print("Hemoglobin level is normal.")


if __name__ == "__main__":
    check_hemoglobin()
