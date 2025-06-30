from flask import Flask, jsonify, request
from dbservice import Product, Sale,db,app



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
            # product_list.append(data)
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
            return jsonify(error),401

        elif data["pid"]=="" or data["quantity"]=="":
            error={"error":"Ensure all fields are filled"}
            return jsonify(error),401
        
        else:
            
            new_sale=Sale(pid=data["pid"], quantity=data["quantity"])
            db.session.add(new_sale)
            db.session.commit()
            return jsonify(data), 201

    else:
        error={"error":"Method not allowed"}
        return jsonify(error), 201

       
app.run(debug=True)


