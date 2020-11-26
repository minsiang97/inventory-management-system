from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.store import Store
from models.warehouse import Warehouse
from models.product import Product


products_blueprint = Blueprint('products',
                            __name__,
                            template_folder='templates')

@products_blueprint.route("/new", methods = ['GET'])
def product_new() :
    warehouses = Warehouse.select()
    return render_template("products/product_new.html", warehouses=warehouses)

@products_blueprint.route("/", methods = ['POST'])
def product_created() :
    warehouse = request.form.get("warehouse_id")
    product_name = request.form.get("product_name")
    product_description = request.form.get("product_description")
    product_color = request.form.get("product_color")
    p = Product(warehouse=warehouse ,  name= product_name, description = product_description, color = product_color)
    if p.save() :
        flash("Product Created!","success")
    else :
        flash("Product Duplicated","danger")
    return redirect(url_for('products.product_new'))

@products_blueprint.route("/", methods = ['GET'])
def product_index():
    products = Product.select()
    return render_template('products/product_index.html',products=products)

@products_blueprint.route("/<product_id>", methods = ['GET'])
def product_show(product_id):
    product = Product.get_by_id(product_id)
    return render_template('products/product_show.html', product=product) 


@products_blueprint.route("/<product_id>", methods = ['POST'])
def product_update(product_id):
    product = Product.get_by_id(product_id)
    product.name = request.form.get("product_name")
    product.description = request.form.get("product_description")
    product.color = request.form.get("product_color")

    if product.save():
        flash("Product successfully updated.", "success")
    else :
        flash("The product entered is same as the previous", "danger")
    return redirect(url_for('products.product_show', product_id = product.id))

@products_blueprint.route("/<product_id>/delete", methods = ['POST'])
def product_delete(product_id):
    product = Product.get_by_id(product_id)
    if product.delete_instance():
        flash("Product successfull deleted.", "success")
    return redirect(url_for('products.product_index'))
