def describe_cabin_class():
    cabin = input("Enter cabin class (LUX/A/B/C): ").strip().upper()

    if cabin == "LUX":
        print("LUX: upper-deck cabin with a balcony.")
    elif cabin == "A":
        print("A: above the car deck, equipped with a window.")
    elif cabin == "B":
        print("B: windowless cabin above the car deck.")
    elif cabin == "C":
        print("C: windowless cabin below the car deck.")
    else:
        print("Invalid cabin class")


if __name__ == "__main__":
    describe_cabin_class()
