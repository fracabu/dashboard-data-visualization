from flask import Flask, jsonify

app = Flask(__name__)

# Dati demo delle vendite
sales_data = [
    {"Data": "2023-01-01", "Prodotto": "Prodotto A", "Categoria": "Elettronica", "Regione": "Nord Italia", "Vendite": 500, "Quantità": 2},
    {"Data": "2023-01-02", "Prodotto": "Prodotto B", "Categoria": "Moda", "Regione": "Sud Italia", "Vendite": 300, "Quantità": 1},
    {"Data": "2023-01-03", "Prodotto": "Prodotto C", "Categoria": "Alimentare", "Regione": "Centro", "Vendite": 100, "Quantità": 5},
    {"Data": "2023-01-04", "Prodotto": "Prodotto A", "Categoria": "Elettronica", "Regione": "Nord Italia", "Vendite": 200, "Quantità": 1},
    {"Data": "2023-01-05", "Prodotto": "Prodotto B", "Categoria": "Moda", "Regione": "Sud Italia", "Vendite": 400, "Quantità": 2},
]

@app.route("/api/vendite", methods=["GET"])
def get_sales():
    return jsonify(sales_data)

if __name__ == "__main__":
    app.run(debug=True)
