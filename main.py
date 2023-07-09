from flask import Flask, render_template, jsonify, request

from flask_pymongo import PyMongo






app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://SUMIT:Sumit%402003@sumit.ssyvqjx.mongodb.net/chatgpt"
mongo = PyMongo(app)




@app.route("/")
def home():
    chats= mongo.db.chats.find({})
    mychats = [chat for chat in chats]
    print(mychats)
    return render_template("index.html",mychats = mychats)


@app.route("/api",methods=["GET","POST"])
def qa():
    if request.method == "POST":
        print(request.json)
        question = request.json.get("question")
        chat = mongo.db.chats.find_one({"question":question})
        print(chat)

        if chat:
            data={"result":f"{chat['answer']}"}
            return jsonify(data)
        else:
            data={"result":f"Answer Of {question}"}
            mongo.db.chats.insert_one({"question": question,"answer":f"Answer from openAI for {question}"})
            return jsonify(data)
    data={"result":" heyyyyyyyyyyyyy"}

    return jsonify(data)
    
app.run(debug=True)