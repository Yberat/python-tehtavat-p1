from flask import Flask, jsonify
import math

app = Flask(__name__)

def onko_alkuluku(luku):
    if luku <= 1:
        return False
    for i in range(2, int(math.sqrt(luku)) + 1):
        if luku % i == 0:
            return False
    return True

@app.route('/alkuluku/<int:luku>', methods=['GET'])
def alkuluku(luku):
    result = onko_alkuluku(luku)
    return jsonify({"Number": luku, "isPrime": result})

if __name__ == '__main__':
    app.run(debug=True)
