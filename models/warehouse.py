from models.base_model import BaseModel
from models.store import Store
import peewee as pw


class Warehouse(BaseModel):
   store = pw.ForeignKeyField(Store, backref='warehouses')
   location = pw.TextField()

   def validate(self):
        duplicate_warehouses = Warehouse.get_or_none(Warehouse.location == self.location)

        if duplicate_warehouses:
            self.errors.append('Warehouse location not unique')