from fastapi import FastAPI,Depends
from models import product
from database import session,engine
import database_models
from fastapi.middleware.cors import CORSMiddleware
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"]
)

database_models.Base.metadata.create_all(bind=engine)
@app.get("/")
def greet():
    return "hello indu"
products=[product(id=1,name="phone",description="samsung",price=999,quantity=10),
          product(id=2,name="laptop",description="a samsung laptop",price=99,quantity=20),
          product(id=3,name="pen",description="a blue ink pen",price=9990,quantity=30),
          product(id=4,name="book",description="a long book",price=1999,quantity=40)
          ]
def get_db():
    db=session()
    try:
        yield db
    finally:
        db.close()
def init_db():
    db=session()
    count=db.query(database_models.product).count()
    if count ==0:
        for product in products:
            db.add(database_models.product(**product.model_dump()))
            db.commit()
#get all products
@app.get("/products")
def get_all_products(db:session=Depends(get_db)):
    db_product=db.query(database_models.product).all()
    return db_product
#get single product by ID
@app.get("/products/{id}")
def get_product_by_id(id:int, db:session=Depends(get_db)):
    db_product=db.query(database_models.product).filter(database_models.product.id==id).first()
    if db_product:
        return db_product
    return "product not found"
#create data
@app.post("/products")
def add_product(product:product,db:session=Depends(get_db)):
    db.add(database_models.product(**product.model_dump()))
    db.commit()
    return product
#update data
@app.put("/products/{id}")
def update_product(id:int,product:product,db:session=Depends(get_db)):
    db_product=db.query(database_models.product).filter(database_models.product.id==id).first()
    if db_product:
        db_product.name=product.name
        db_product.description=product.description
        db_product.price=product.price
        db_product.quantity=product.quantity
        db.commit()
        return "product updated successfully"
    else:
        return "No prodcuts available"
#delete product
@app.delete("/products/{id}")
def delete_product(id:int,db:session=Depends(get_db)):
    db_product=db.query(database_models.product).filter(database_models.product.id==id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    else:
        return "Product not found"
#intialize the date
def init_db():
    db=session()
    count=db.query(database_models.product).count()
    if count ==0:
        for product in products:
            db.add(database_models.product(**product.model_dump()))
            db.commit()
init_db()

