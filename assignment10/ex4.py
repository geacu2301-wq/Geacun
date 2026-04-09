from flask import Flask, jsonify
import json

app = Flask(__name__)

with open("airports.json", "r", encoding="utf-8") as file:
    du_lieu_dia_diem_san_bay = json.load(file)

@app.route("/airport/<icao>")
def tim_san_bay(icao):
    for san_bay in du_lieu_dia_diem_san_bay:
        if san_bay["icao"] == icao:
            return jsonify({
                "icao": san_bay["icao"],
                "name": san_bay["name"],
                "city": san_bay["municipality"],
                "country": san_bay["iso_country"]
            })
    return jsonify({"error": "Khong tim thay san bay nao ca"}), 404

app.run()