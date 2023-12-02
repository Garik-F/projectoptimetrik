from typing import Annotated, Optional
from bson import ObjectId
from pydantic import BaseModel, BeforeValidator,Field

PyObjectId =  Annotated[str,BeforeValidator(str)]
#тут типо моделька пользователя и функционал его
class User(BaseModel):
    id:PyObjectId = Field(alias='_id', default=None)
    name:str=Field()
    email:str=Field()
    class Config:
        populate_by_name = True
        json_schema_extra={
            "example":{
                "_id":"",
                "name":"Ivan234",
                "email":"iva.aaa@mai;.ru"
            }
        }
        
class AddUser(BaseModel):
    name:str=Field()
    email:str=Field()
    class Config:
        populate_by_name = True
        json_schema_extra={
            "example":{
                "_id":"",
                "name":"Ivan234",
                "email":"iva.aaa@mail.ru"
            }
        }
        
class UpdateUser(BaseModel):
    name:Optional[str]
    email:Optional[str]
    class Config:
        json_schema_extra={
            "example":{
                "_id":"",
                "name":"Ivan234",
                "email":"iva.aaa@mail.ru"
            }
        }