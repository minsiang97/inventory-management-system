from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.store import Store
from models.warehouse import Warehouse


warehouses_blueprint = Blueprint('warehouses',
                            __name__,
                            template_folder='templates')


@warehouses_blueprint.route("/new", methods = ['GET'])
def warehouse_new() :
    stores = Store.select()
    return render_template("warehouses/warehouse_new.html", stores=stores)

@warehouses_blueprint.route("/", methods = ['POST'])
def warehouse_created() :
    store = request.form.get("store_id")
    location = request.form.get("location")
    w = Warehouse(store=store , location = location)
    if w.save() :
        flash("Warehouse Created!","success")
    else :
        flash("Warehouse Duplicated","danger")
    return redirect(url_for('warehouses.warehouse_new'))

@warehouses_blueprint.route("/", methods = ['GET'])
def warehouse_index():
    warehouses = Warehouse.select()
    return render_template('warehouses/warehouse_index.html',warehouses=warehouses)

@warehouses_blueprint.route("/<warehouse_id>", methods = ['GET'])
def warehouse_show(warehouse_id):
    warehouse = Warehouse.get_by_id(warehouse_id)
    return render_template('warehouses/warehouse_show.html', warehouse=warehouse) 

@warehouses_blueprint.route("/<warehouse_id>", methods = ['POST'])
def warehouse_update(warehouse_id):
    warehouse = Warehouse.get_by_id(warehouse_id)
    warehouse.location = request.form.get("warehouse_location")
    if warehouse.save():
        flash("Warehouse location successfully updated.", "success")
    else :
        flash("The location entered is same as the previous", "danger")
    return redirect(url_for('warehouses.warehouse_show', warehouse_id = warehouse.id))

@warehouses_blueprint.route("/<warehouse_id>/delete", methods = ['POST'])
def warehouse_delete(warehouse_id):
    warehouse = Warehouse.get_by_id(warehouse_id)
    if warehouse.delete_instance():
        flash("Warehouse successfull deleted.", "success")
    return redirect(url_for('warehouses.warehouse_index'))