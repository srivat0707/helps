
from flask import Flask
from flask import request,render_template
app=Flask(__name__)
data={}

@app.route("/add",methods=["GET","POST"])
def home():
    if request.method=="GET":
        return render_template("form.html")
    if request.method=="POST":
        head=request.form["heading"]
        lvl=request.form["level"]
        topic=request.form["topic"]
        print(head,lvl,topic) 
        data[head]=[head,lvl,topic]
        return render_template("home.html",sd=data.keys())
@app.route("/<tp>",methods=["GET","POST"])
def event(tp):
    h=data[tp]
    print(h)
    return render_template("events.html",sd=h)
if(__name__=="__main__"):
    app.run(debug=True)