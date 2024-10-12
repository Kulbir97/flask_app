from flask import Flask, render_template
from pymongo import MongoClient

# Initialize Flask app
app = Flask(__name__)

# MongoDB Atlas connection
client = MongoClient("mongodb+srv://Kulbir:data23@cluster0.iwhul.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.shop_db  # Access the shop_db database
products_collection = db.products  # Access the products collection

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    products = products_collection.find()  # Fetch all products from the collection
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
