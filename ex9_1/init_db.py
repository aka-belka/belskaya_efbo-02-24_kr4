from models import engine, Base, SessionLocal, Product

Base.metadata.create_all(bind=engine)

db = SessionLocal()
db.add_all([
    Product(title="Кровать", price=80000.0, count=10),
    Product(title="Подушка", price=4500.0, count=50)
])
db.commit()
db.close()
