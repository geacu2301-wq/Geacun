import requests

ten_thanh_pho = input("Ten thanh pho la gi: ")

api_key = "your_api"

duong_dan = f"https://api.openweathermap.org/data/2.5/weather?q={ten_thanh_pho}&appid={api_key}"

ket_qua = requests.get(duong_dan)

du_lieu = ket_qua.json()

if ket_qua.status_code == 200:
    mo_ta = du_lieu["weather"][0]["description"]
    nhiet_do_k = du_lieu["main"]["temp"]
    nhiet_do_c = nhiet_do_k - 273.15

    print(mo_ta)
    print(round(nhiet_do_c, 2), "°C")
else:
    print("Khong tim thay thanh pho  hoac co the bi loi")
print(round(nhiet_do_c, 2), "°C")