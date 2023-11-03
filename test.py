from tinydb import TinyDB,Query,where
import tinydb
db =  TinyDB("./db/db.json")

person = tinydb.Query()

# db.insert({'username': 'NormVg', 'password': "08b63d8ade1bd145200a3aeced242edceb0180cec322ec26d7997932b1315025"})
# db.insert({'username': 'vishnu_gupta_vg', 'password': "ab6b786aa204199a39492078eab36895cfa6b650d969c79f85a0055d461a0c52"})
print(db.all())

# [
#     {"msg":"hello","by":"Norm","time"}
# ]