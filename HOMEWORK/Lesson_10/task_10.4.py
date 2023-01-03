from csv import DictReader
from pydantic import BaseModel, Field, validator


with open('file_for_task4.csv', 'r', encoding='utf-8') as file:
    data = list(DictReader(file))

for dtc in data:
    dtc['price'] = int(dtc['price'])


dictdata = {index: dtc for index, dtc in enumerate(data)}

class DataSchema(BaseModel):
    article: str = Field(min_length=3)
    title: str = Field(min_length=2)
    description: str = Field(min_length=4)
    price: int

    @validator('article', pre=True)
    def article_check(cls, value):
        if value == 'ноутбук':
            with open('nootbook.csv', 'a', encoding='utf-8') as file:
                file.write(cls)
        if value == 'смартфон':
            with open('smartphone.csv', 'a', encoding='utf-8') as file:
                file.write(cls)

class DictSchema(BaseModel):
    def dict_check(self, dct: dict):
        for index in dct:
            index = DataSchema

DictSchema(**dictdata)
