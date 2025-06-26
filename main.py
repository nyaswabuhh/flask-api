from flask import Flask, jsonify, request

app=Flask(__name__)

product_list=[]

@app.route("/")
def index():

    res = {"Flask-API":"1.0"}
    return jsonify(res),200

@app.route("/api/products", methods=["GET","POST"])
def products():
    if request.method=="GET":
        return jsonify(product_list),200
    elif request.method=="POST":
        data = dict(request.get_json())
        if "name" not in data.keys()or "bp" not in data.keys() or "sp" not in data.keys():
            error={"error":"Invalid Keys"}
            return jsonify(error),401

        elif data["name"]=="" or data["bp"]=="" or data["sp"]=="":
            error={"error":"Ensure all fields are filled"}
            return jsonify(error),401

        else:
            product_list.append(data)
            return jsonify(data), 201
    else:
        error = {"error": "Method not allowed"}
        return jsonify(error),401
       
app.run(debug=True)


