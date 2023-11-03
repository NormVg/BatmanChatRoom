from tinydb import TinyDB,Query,where
import tinydb
db =  TinyDB("./db/db.json")

person = tinydb.Query()

db.insert({'username': 'MrPixel', 'password': "12f0a4ba22f08d7499fc7def1c98c680ac2c99c67fc7ba2cbcc5ec2f6a8c6a16"})
# db.insert({'username': 'vishnu_gupta_vg', 'password': "ab6b786aa204199a39492078eab36895cfa6b650d969c79f85a0055d461a0c52"})
print(db.all())

# [
#     {"msg":"hello","by":"Norm","time"}
# ]