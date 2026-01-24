def check_zander_length():
    length_cm = float(input("Enter the length of the zander (cm): "))
    size_limit = 42.0

    if length_cm < size_limit:
        below = size_limit - length_cm
        print("Release the fish back into the lake!")
        print(f"The fish was {below:.1f} cm below the size limit.")
    else:
        print("The fish meets the size limit. You may keep it.")


if __name__ == "__main__":
    check_zander_length()
