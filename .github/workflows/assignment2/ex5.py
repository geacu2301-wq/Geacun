import math

def pizza_unit_price(diameter_cm, price_usd):
    radius_m = (diameter_cm / 2) / 100
    area_m2 = math.pi * (radius_m ** 2)
    return price_usd / area_m2


def compare_two_pizzas():
    d1 = float(input("Enter diameter of pizza 1 (cm): "))
    p1 = float(input("Enter price of pizza 1 (USD): "))

    d2 = float(input("Enter diameter of pizza 2 (cm): "))
    p2 = float(input("Enter price of pizza 2 (USD): "))

    u1 = pizza_unit_price(d1, p1)
    u2 = pizza_unit_price(d2, p2)

    print(f"Pizza 1 unit price: {u1:.2f} USD/m^2")
    print(f"Pizza 2 unit price: {u2:.2f} USD/m^2")

    if u1 < u2:
        print("Pizza 1 provides better value for money.")
    elif u2 < u1:
        print("Pizza 2 provides better value for money.")
    else:
        print("Both pizzas provide the same value for money.")


if __name__ == "__main__":
    compare_two_pizzas()
