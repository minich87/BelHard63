from sqlalchemy import Column, INT, VARCHAR, ForeignKey, create_engine, select
from sqlalchemy.orm import declarative_base, sessionmaker


Base = declarative_base()

class BaseMixin(object):
    pk = Column('id', INT, primary_key=True)

    engine = create_engine('postgresql://minich:12345@localhost:5432/bh63')
    Session = sessionmaker(bind=engine)

    @staticmethod
    def create_session(func):
        def wrapper(*args, **kwargs):
            with BaseMixin.Session() as session:
                return func(*args, **kwargs, session=session)

        return wrapper()

    @classmethod
    @create_session
    def get(cls, pk, session: Session = None):
        return session.get(cls, pk)

    @classmethod
    @create_session
    def all(cls, order_by: str = 'id', session: Session = None, **kwargs):
        objs = session.scslsrs(
            select(cls)
            .filter_by(**kwargs)
            .order_by(order_by)
        )
        return objs.all()

    @create_session
    def save(self, session: Session = None):
        session.add(self)
        session.commit()
        session.refresh(self)


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
