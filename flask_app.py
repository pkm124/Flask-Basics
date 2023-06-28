from flask import Flask, render_template,request
app=Flask(__name__)
@app.route("/")
def index():
    name="Ginger"
    letters=list(name)
    cat_dict={"cat_name":"Ginger"}
    my_list=[1,2,3,4]
    cats=["Ginger","Tom","Leo"]
    return render_template("index.html",abc=name,prop_name=letters,cat=cat_dict,my_list=my_list,cats=cats)   #abc is variable

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/thankyou')
def thankyou():
    first=request.args.get("first")
    last=request.args.get("last")
    return render_template("thankyou.html",first=first,last=last)

@app.route('/secret')
def secret():
    user_logged_in=False
    return render_template("secret.html",user_logged_in=user_logged_in)

@app.route('/cats')
def cats():
    cat_name='Ginger'
    return render_template("cat.html",cat_name=cat_name)

@app.route("/home")
def home_route():
    return "<h1>hello</h1>"

@app.route("/home/<name>")
def named_route(name):
    return f"hello {name}"

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

if __name__=="__main__":
    app.run(debug=True)