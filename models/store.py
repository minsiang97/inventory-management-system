from models.base_model import BaseModel
import peewee as pw


class Store(BaseModel):
   name = pw.CharField(unique=True)
   
   def validate(self):
        duplicate_stores = Store.get_or_none(Store.name == self.name)

        if duplicate_stores:
            self.errors.append('Store name not unique')
