# Version: 1.5
# Date: 16.12.2022 22:56 
# _____________________________________________

class Button:
    width = int
    height = int
    text = str

    @classmethod
    def change_color(cls, new_color: str) -> None:
        colors = ('black', 'blue', 'yellow', 'green', 'grey', 'red', 'white')
        if not isinstance(new_color, str):
            raise TypeError('Argument need enter str')
        if new_color not in colors:
            raise ValueError('Argument must be from the list of allowed values')
        cls.color = new_color.lower()

    @classmethod
    def from_dict(cls, **kwargs) -> 'Button':
        return Button(**kwargs)

    def to_dict(self) -> dict:
        return self.__dict__

    def press(self) -> bool:
        return not self.is_pressed

    def __init__(self, width: int, height: int, text: str) -> None:
        if not isinstance(width, int):
            raise TypeError('Argument must be int')
        if not isinstance(height, int):
            raise TypeError('Argument must be int')
        if not isinstance(text, str):
            raise TypeError('Argument must be str')
        self.width = width
        self.height = height
        self.text = text

    def __str__(self) -> str:
        return f'Button text: {self.text}'


NumLk = Button(40, 17, 'Numeric Lock')
NumLk.is_pressed = False
Button.color = 'white'
NumLk.press()

delete = {
    'width': 30,
    'height': 17,
    'text': 'Delete',
    'color': 'grey',
    'is_pressed': True
    }

delete.from_dict()
print(delete.text())
