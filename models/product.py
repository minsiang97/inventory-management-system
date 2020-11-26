from models.base_model import BaseModel
from models.store import Store
from models.warehouse import Warehouse
import peewee as pw

class Product(BaseModel):
   name = pw.CharField(index=True)
   description = pw.TextField()
   warehouse = pw.ForeignKeyField(Warehouse, backref='products')
   color = pw.CharField(null=True)

   def validate(self):
        duplicate_products_name = Product.get_or_none(Product.name == self.name)
        duplicate_products_color = Product.get_or_none(Product.color == self.color)

        if duplicate_products_name and duplicate_products_color:
            self.errors.append('Product name and color not unique')