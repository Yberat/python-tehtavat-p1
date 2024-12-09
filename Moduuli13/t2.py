from flask import Flask, jsonify

app = Flask(__name__)

kentat = {
    "EFHK": {"Name": "Helsinki Vantaa Airport", "Municipality": "Helsinki"},
    "EGLL": {"Name": "London Heathrow Airport", "Municipality": "London"},
    "JFK": {"Name": "John F. Kennedy International Airport", "Municipality": "New York"},
    "LFPG": {"Name": "Charles de Gaulle Airport", "Municipality": "Paris"},
}

@app.route('/kenttä/<icao_code>', methods=['GET'])
def kentta(icao_code):
    kentta = kentat.get(icao_code.upper())  # Haetaan ICAO-koodia vastaava kenttä
    if kentta:
        return jsonify({"ICAO": icao_code.upper(), "Name": kentta["Name"], "Municipality": kentta["Municipality"]})
    else:
        return jsonify({"error": "Kenttää ei löydy"}), 404

if __name__ == '__main__':
    app.run(debug=True)
