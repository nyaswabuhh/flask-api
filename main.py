from datetime import datetime
from flask import Flask, jsonify, request
from dbservice import Product, Sale,db,app
from flask_cors import CORS



# app=Flask(__name__)

# product_list=[]


@app.route("/")
def index():

    res = {"Flask-API":"1.0"}
    return jsonify(res),200

@app.route("/api/products", methods=["GET","POST"])
def products():
    if request.method=="GET":
        product_list =Product.query.all()
        print ('product list', product_list)

        prods=[]
        for prod in product_list:
            product_data={
                "id":prod.id,
                "name":prod.name,
                "bp":prod.bp,
                "sp":prod.sp
            }
            prods.append(product_data)
        return jsonify(prods), 200
    elif request.method=="POST":
        data = dict(request.get_json())
        if "name" not in data.keys()or "bp" not in data.keys() or "sp" not in data.keys():
            error={"error":"Invalid Keys"}
            return jsonify(error),401

        elif data["name"]=="" or data["bp"]=="" or data["sp"]=="":
            error={"error":"Ensure all fields are filled"}
            return jsonify(error),401

        else:
            
            new_product=Product(name=data["name"], bp=data["bp"], sp=data["sp"])
            db.session.add(new_product)
            db.session.commit()
            return jsonify(data), 201
    else:
        error = {"error": "Method not allowed"}
        return jsonify(error),401
    

@app.route("/api/sales", methods=["GET", "POST"])
def sales():
    if request.method=="GET":
        sold_items =Sale.query.all()
        print ('sold items', sold_items)

        sold=[]
        for i in sold_items:
            sold_items_data={
                "id":i.id,
                "pid":i.pid,
                "quantity":i.quantity,
                "created_at":i.created_at
            }
            sold.append(sold_items_data)
        return jsonify(sold), 200
    
    elif request.method=="POST":
        data = dict(request.get_json())
        if "pid" not in data.keys()or "quantity" not in data.keys():
            error={"error":"Invalid Keys"}
            return jsonify(error),400

        elif data["pid"]=="" or data["quantity"]=="":
            error={"error":"Ensure all fields are filled"}
            return jsonify(error),401
        
        else:
                
            if "created_at" in data and data["created_at"]:
                try:
                    created_at = datetime.strptime(data["created_at"], '%Y-%m-%d %H:%M:%S')
                except ValueError:
                    return jsonify({"error": "Invalid datetime format. Use YYYY-MM-DD HH:MM:SS"}), 400
            else:
                created_at = datetime.utcnow()  # Default fallback
                                 
            
            new_sale=Sale(pid=data["pid"], quantity=data["quantity"], created_at=created_at)
            db.session.add(new_sale)
            db.session.commit()

            updated_sale={
                "id":new_sale.id,
                "pid":new_sale.pid,
                "quantity":new_sale.quantity,
                "created_at":new_sale.created_at
            }

            return jsonify(updated_sale), 201

    else:
        error={"error":"Method not allowed"}
        return jsonify(error), 405
    
# app.run(debug=True)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)


