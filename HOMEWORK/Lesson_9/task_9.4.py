# Date: 23.12.2022 16:36
# _____________________________________________

list_categories = [
    {'name': 'action', 'is_published': bool},
    {'name': 'adventure', 'is_published': bool},
    {'name': 'comedy', 'is_published': bool},
    {'name': 'fantasy', 'is_published': bool},
    {'name': 'mystic', 'is_published': bool}
]

class Category:
    categories = list_categories

    @classmethod
    def add(cls, dct: dict) -> int:
        for el in list_categories:
            if dct.get('name') == el.get('name'):
                raise ValueError('This category is already in the list.')
        else:
            list_categories.append(dct)
            return list_categories.index(dct)

    @classmethod
    def get(cls, index_in_list: int) -> dict:
        if index_in_list < len(list_categories):
            return list_categories[index_in_list]
        else:
            raise ValueError('There isn\'t element')

    @classmethod
    def update(cls, index_in_list: int, new_category: dict) -> None:
        if index_in_list >= len(list_categories):
            list_categories.append(new_category)
        else:
            raise ValueError('There is element in this index.')

    @classmethod
    def make_published(cls, index_in_list: int) -> None:
        if index_in_list < len(list_categories):
            list_categories[index_in_list]['is_published'] = True
        else:
            raise ValueError('There isn\'t this index in list.')

    @classmethod
    def make_unpublished(cls, index_in_list: int) -> None:
        if index_in_list < len(list_categories):
            list_categories[index_in_list]['is_published'] = False
        else:
            raise ValueError('There isn\'t this index in list.')
