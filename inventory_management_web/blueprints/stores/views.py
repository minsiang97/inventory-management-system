from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.store import Store


stores_blueprint = Blueprint('stores',
                            __name__,
                            template_folder='templates')


@stores_blueprint.route("/new", methods = ['GET'])
def store_new():
    return render_template('stores/addstore.html')
    
@stores_blueprint.route("/", methods =['POST'])
def store_created() :
    
    store_name = request.form.get("store_name")
    store = Store(name=store_name)
    if store.save():
        flash("Successfully added","success")
    else :
        flash("Duplicate Entry!!","danger")
    return redirect(url_for("stores.store_new"))

@stores_blueprint.route("/", methods = ['GET'])
def store_index():
    stores = Store.select()
    return render_template('stores/store_index.html',stores=stores)
    
    

@stores_blueprint.route("/<store_id>", methods = ['GET'])
def store_show(store_id):
    store = Store.get_by_id(store_id)
    return render_template('stores/store_show.html', store=store) 

@stores_blueprint.route("/<store_id>", methods = ['POST'])
def store_update(store_id):
    store = Store.get_by_id(store_id)
    store.name = request.form.get("store_name")
    if store.save():
        flash("Store name successfully updated.", "success")
    else :
        flash("The name entered is same as the previous", "danger")
    return redirect(url_for('stores.store_show', store_id = store.id))


@stores_blueprint.route("/<store_id>/delete", methods = ['POST'])
def store_delete(store_id):
    store = Store.get_by_id(store_id)
    if store.delete_instance():
        flash("Store successfull deleted.", "success")
    return redirect(url_for('stores.store_index'))