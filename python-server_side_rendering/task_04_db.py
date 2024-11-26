from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

def read_json_data():
  with open("products.json", "r") as f:
    return json.load(f)

def read_csv_data():
  with open("products.csv", "r") as f:
    reader = csv.DictReader(f)
    return list(reader)

@app.route("/products")
def product_display():
  source = request.args.get("source")
  product_id = request.args.get("id", type=int)

  if not source:
    return render_template("product_display.html", error="Missing source parameter (json or csv)")

  if source not in ["json", "csv"]:
    return render_template("product_display.html", error="Wrong source parameter")

  data = read_json_data() if source == "json" else read_csv_data()

  if product_id:
    filtered_data = [product for product in data if product["id"] == product_id]
    if not filtered_data:
      return render_template("product_display.html", error="Product not found")
    data = filtered_data

  return render_template("product_display.html", products=data)

@app.route('/items')
def show_items():
    with open('items.json', 'r') as f:
        data = json.load(f)
        items = data['items']  # Extraer la lista de items del diccionario

    return render_template('items.html', items=items)

# Función para obtener los productos desde la base de datos
def fetch_products(source):
    if source == 'sql':
        try:
            conn = get_db()
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Products')
            products = cursor.fetchall()
            return products
        except sqlite3.Error as e:
            # Manejar errores de la base de datos (loggear, mostrar mensaje, etc.)
            return None
    else:
        # Implementar lógica para obtener datos de JSON o CSV (si es necesario)
        return None
    
@app.route('/productos')
def product_display():
    source = request.args.get('source')
    products = fetch_products(source)

    if products is None:
        error_message = "Error al obtener datos" if source == 'sql' else "Fuente de datos inválida"
        return render_template('product_display.html', error_message=error_message)

    return render_template('product_display.html', products=products)



if __name__ == "__main__":
  app.run(debug=True)