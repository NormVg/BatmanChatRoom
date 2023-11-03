from flask import Flask , render_template , request , jsonify ,redirect
import tinydb 
from mycypher import encrypt
import time
import uuid 
# from flask_cors import CORS


db = tinydb.TinyDB("./db/db.json")

chatroom =  []
users = tinydb.Query()
app = Flask(__name__)
# CORS(app)

@app.route("/",methods=['GET','POST'])
def login():
    if request.method == "POST":
        uname = request.form.get("username")
        upasw = request.form.get("password")
        # print(uname,upasw)
        
        
        pasKey = encrypt(upasw)
        userCred = db.search(users.username == uname)
        # print(userCred[0])
        if len(userCred)!=0:
            # print('ACCOUNT EXIST')
            if userCred[0].get("password") ==  pasKey:
                # print("PASSWORD CORRECT")
                return redirect(f"/chat?auth-key={pasKey}&token={int(time.time())}&user={uname}")

            else: return "password wrong"
        else: return " account not exist "
    return render_template("login.html")

@app.get("/chat")
def chat():
    key = request.args.get("auth-key")
    uname = request.args.get("user")
    token = int(request.args.get("token")) + 150
    print("AUTH KEY", key,"TOKEN", token)
    Auth_Token = int(time.time())
    if token >= Auth_Token :
        print("TOKEN ACCEPTED")
        return render_template("chatroom.html")
    else: 
        print("TOKEN EXPIRED")
        return "token expired login again"


@app.get("/api/room-updates")
def room_updates():
    msg_id = request.args.get("id")
    try :
        latestmsg =jsonify({"messages":[chatroom[-1]]}) 
    except:
        latestmsg =jsonify({"messages":[]}) 
    if msg_id == "new-client-200":

        return latestmsg
    else:
        for i,k in enumerate(chatroom):
            if k['id'] == msg_id:             
                data = chatroom.copy()
                data = data[i+1:]
                print(data)
                return jsonify({"messages":data})
        return latestmsg

@app.post("/api/send-msg")
def send_msg():
    reply = request.get_json()
    id = uuid.uuid4()
    data = {"user":reply['user'], "msg":reply['msg'],"id":str(id.int)}
    if len(chatroom)> 40:
        try: 
            chatroom.remove(chatroom[0])
        except:
            pass
    chatroom.append(data)
    

    return jsonify({"status":200})

@app.get("/admin")
def admin():
    return render_template("admin.html")

if __name__== "__main__":
    app.run(debug=True, host="0.0.0.0")