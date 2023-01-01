# ____________________________________________
# Date: 23.12.2022 11:18
# _____________________________________________
# Реализовать класс Category

list_categories = ['action', 'adventure', 'comedy', 'fantasy', 'mystic']

class Category:
    categories = list_categories

    @classmethod
    def add(cls, categories: str) -> int:
        if categories.lower() in list_categories:
            raise ValueError('This category is already in the list.')
        if categories.lower() not in list_categories:
            list_categories.append(categories.lower())
            return list_categories.index(categories.lower())

    @classmethod
    def get(cls, index_in_list: int) -> str:
        if index_in_list < len(list_categories):
            return list_categories[index_in_list]
        else:
            raise ValueError('There isn\'t element')

    @classmethod
    def update(cls, index_in_list: int, new_category: str) -> None:
        if index_in_list >= len(list_categories):
            list_categories.append(new_category.lower())
        else:
            raise ValueError('There is element in this index.')
