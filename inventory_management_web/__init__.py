from app import app
from flask import render_template
from inventory_management_web.blueprints.stores.views import stores_blueprint
from inventory_management_web.blueprints.warehouses.views import warehouses_blueprint
from inventory_management_web.blueprints.products.views import products_blueprint
from flask_assets import Environment, Bundle
from .util.assets import bundles

assets = Environment(app)
assets.register(bundles)

app.register_blueprint(stores_blueprint, url_prefix="/stores")
app.register_blueprint(warehouses_blueprint, url_prefix="/warehouses")
app.register_blueprint(products_blueprint, url_prefix="/products")

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route("/")
def home():
    return render_template('home.html')
