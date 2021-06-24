from flask import *
import pyrebase
from DB_handler import *
app = Flask(__name__)
@app.route("/")
def main():
    return redirect("/ramen")
@app.route("/ramen")
def ramen():
    id="admin"
    ramen=db.child("id").child(id).child("ramen").get().val()
    from collections import OrderedDict
    import json
    ramen = json.dumps(ramen,ensure_ascii=False)
    characters = """""{}"""
    ramen = ''.join( x for x in ramen if x not in characters)
    return render_template("ramen.html",id=id,ramen=ramen)  
@app.route("/plusramen")
def plusramen():
    return render_template("plusramen.html")
@app.route("/plusramen-info",methods=['POST'])
def plusrameninfo():
    ramenname = request.form['ramen-name']
    ramennumber = request.form['ramen-number']
    id="admin"
    dbramennumberno = db.child("id").child(id).child("ramen").child(ramenname).get()
    dbramennumber = dbramennumberno.val()
    if dbramennumber is None:
        dbramennumber=int("0")
    totalramennumber=int(dbramennumber) + int(ramennumber)
    db.child("id").child(id).child("ramen").update({ramenname: totalramennumber})
    ramen=db.child("id").child(id).child("ramen").get().val()
    from collections import OrderedDict
    import json
    ramen = json.dumps(ramen,ensure_ascii=False)
    characters = """""{}"""
    ramen = ''.join( x for x in ramen if x not in characters)
    return render_template("ramen.html",id=id,ramen=ramen)
    
@app.route("/minusramen")
def minusramen():
    return render_template("minusramen.html")
@app.route("/minusramen-info",methods=['POST'])
def minusrameninfo():
    ramenname = request.form['ramen-name']
    ramennumber = request.form['ramen-number']
    id="admin"
    dbramennumberno = db.child("id").child(id).child("ramen").child(ramenname).get()
    dbramennumber = dbramennumberno.val()
    if dbramennumber is None:
        dbramennumber=int("0")
    totalramennumber=int(dbramennumber) - int(ramennumber)
    db.child("id").child(id).child("ramen").update({ramenname: totalramennumber})
    ramen=db.child("id").child(id).child("ramen").get().val()
    from collections import OrderedDict
    import json
    ramen = json.dumps(ramen,ensure_ascii=False)
    characters = """""{}"""    
    ramen = ''.join( x for x in ramen if x not in characters)
    return render_template("ramen.html",id=id,ramen=ramen)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="80",debug=True)
