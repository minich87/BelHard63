from sqlalchemy import Column, INT, VARCHAR, BOOLEAN, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


Base = declarative_base()


class BaseMixin():
    pk = Column('id', INT, primary_key=True, autoincrement=True)

    engine = create_engine('sqlite:///bh63.sqlite3')
    _Session = sessionmaker(bind=engine)

    @staticmethod
    def create_session(func):
        def wrapper(*args, **kwargs):
            with BaseMixin._Session() as session:
                return func(*args, **kwargs, session=session)
        return wrapper

    @classmethod
    @create_session
    def get(cls, pk, session: Session = None):
        return session.get(cls, pk)

    @classmethod
    @create_session
    def all(cls, order_by: str = 'id', session: Session = None, **kwargs):
        objs = session.scalars(
            select(cls)
            .filter_by(**kwargs)
            .order_by(order_by)
        )
        return objs.all()

    @create_session
    def save(self, session: Session = None):
        session.add(self)
        session.comit()
        session.refresh(self)

    @create_session
    def delete(self, session: Session = None):
        session.delete(self)
        session.comit()


class Category(BaseMixin, Base):
    __tablename__ = 'categories'

    name = Column(VARCHAR(24), nullable=False, unique=True)


class Product(BaseMixin, Base):
    __tablename__ = 'products'

    title = Column(VARCHAR(36), nullable=False)
    description = Column(VARCHAR(140))
    category_id = Column(INT, ForeignKey('categories.id', ondelete='RESTRICT'), nullable=False)


class User(BaseMixin, Base):
    __tablename__ = 'users'

    name = Column(VARCHAR(24))
    email = Column(VARCHAR(24), unique=True)


class Status(BaseMixin, Base):
    __tablename__ = 'statuses'

    name = Column(VARCHAR(15), nullable=False, unique=True)


class Order(BaseMixin, Base):
    __tablename__ = 'orders'

    user_id = Column(INT, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    status_id = Column(INT, ForeignKey('statuses.id', ondelete='NO ACTION'), nullable=False)


class Order_item(BaseMixin, Base):
    __tablename__ = 'order_items'

    order_id = Column(INT, ForeignKey('orders.id', ondelete='NO ACTION'), nullable=False)
    product_id = Column(INT, ForeignKey('products.id', ondelete='CASCADE'), nullable=False)
