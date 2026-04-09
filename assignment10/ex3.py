from flask import Flask, jsonify
app = Flask(__name__)

def la_so_nguyen_to(so):
    if so < 2:
        return False
    for i in range(2, so):
        if so % i == 0:
            return False
    return True
@app.route("/prime_number/<int:so>")
def kiem_tra_so_nguyen_to(so):
    ket_qua = la_so_nguyen_to(so)
    return jsonify({
        "Number": so,
        "IsPrime": ket_qua
    })

app.run()