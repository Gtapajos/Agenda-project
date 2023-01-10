from flask import Flask, render_template, request, flash, redirect

app = Flask(__name__, template_folder='templates')
app.secret_key = "149205"

@app.route("/login")
def Login():
    return render_template("login_page.html")

@app.route("/add_user", methods=["GET", "POST"])
def Signing():
   name = request.form.get['your_full_name']
   print(name)

app.run(debug=True)