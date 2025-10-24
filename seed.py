from models import db, Product
from app import app

with app.app_context():
    db.create_all()
    products = [
        Product(name="Paracetamol", category="General", price=25.0, image="paracetamol.jpg", quantity=100),
        Product(name="Folic Acid", category="Pregnancy", price=45.0, image="folic_acid.jpg", quantity=50),
        Product(name="Insulin", category="Diabetes", price=120.0, image="insulin.jpg", quantity=30),
        Product(name="Multivitamin Gummies", category="Supplements", price=60.0, image="multivitamin.jpg", quantity=80),
    ]
    db.session.bulk_save_objects(products)
    db.session.commit()
    print("Products seeded!")
