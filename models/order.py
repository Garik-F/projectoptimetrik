from typing import Annotated, Optional
from bson import ObjectId
from pydantic import BaseModel, BeforeValidator,Field

PyObjectId =  Annotated[str,BeforeValidator(str)]
statusorder = {
    'status': 'complete ' 'not complete'
}
#тут моделька уже заказа, если че он не дописан
class Order(BaseModel):
    id:PyObjectId = Field(alias='_id', default=None)
    status:statusorder=Field()#тут надо нормально составить коллекцию для того, чтобы статус заказа был выполнен или невыполнен в бд
    belongs:str=Field() # а тут ссылатся на имя создавшего пользователя
    class Config:
        populate_by_name = True
        json_schema_extra={
            "example":{
                "_id":"",
                "status":"",
                "belongs":""
            }
        }
        
class AddOrder(BaseModel):
    name:str=Field()
    email:str=Field()
    class Config:
        populate_by_name = True
        json_schema_extra={
            "example":{
                "status":"",
                "belongs":""
            }
        }
        
class UpdateOder(BaseModel):
    name:Optional[str]
    email:Optional[str]
    class Config:
        json_schema_extra={
            "example":{
                "status":"",
                "belongs":""
            }
        }