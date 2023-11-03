from flask import Flask , render_template , request , jsonify ,redirect
import tinydb 
from mycypher import encrypt
import time



db = tinydb.TinyDB("./db/db.json")
chatroom =  []
users = tinydb.Query()
app = Flask(__name__)

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
    token = int(request.args.get("token")) + 10
    print("AUTH KEY", key,"TOKEN", token)
    Auth_Token = int(time.time())
    if token >= Auth_Token or token:
        print("TOKEN ACCEPTED")
        return render_template("chatroom.html")
    else: 
        print("TOKEN EXPIRED")
        return "token expired login again"


@app.get("/api/room-updates")
def room_updates():
    return "200"

@app.get("/api/send-msg")
def send_msg():
    return "200"

@app.get("/admin")
def admin():
    return render_template("admin.html")

if __name__== "__main__":
    app.run(debug=True, host="0.0.0.0")