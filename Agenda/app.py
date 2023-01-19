from flask import Flask, render_template, request, flash, redirect
import sqlite3

app = Flask(__name__, template_folder='templates')
app.secret_key = "149205"

connection = sqlite3.connect('agenda.db', check_same_thread=False)
cursor = connection.cursor()

id = 1

@app.route("/")
def Login():
    return render_template("login_page.html")

@app.route("/registering")
def Registering():
     return render_template("registering_page.html")

@app.route("/back_login")
def Back_lgpage():
     return render_template("login_page.html")

@app.route("/user_info")
def User_info():
     return render_template("user_s_informations_page.html")

@app.route("/back_calendar")
def Back_calendar():
     return render_template("calendar_page.html")

@app.route("/verify_login", methods=["GET", "POST"])
def Verify():
   global id
   connection = sqlite3.connect('agenda.db', check_same_thread=False)
   cursor = connection.cursor()

   cursor.execute("select * from user_data")
   user_data_search = cursor.fetchall()
   
   valid = "False"
   if request.method == "POST":
       for dt in user_data_search:
           if type(dt) == int:
               id = dt
           if dt[2] == request.form['username'] and dt[4] == request.form['password']:
               valid = "True"
               break

   return Initial_page(valid)

@app.route("/initial_page")
def Initial_page(val):
    if val == "True":
        return render_template("calendar_page.html")
    
    flash("uncorrect username or password")
    return redirect("/")
        

@app.route("/add_user", methods=["GET", "POST"])
def Signing():
   user_dt = []
   connection = sqlite3.connect('agenda.db', check_same_thread=False)
   cursor = connection.cursor()
  
   if request.method == 'POST':
       user_dt.append(request.form['your_full_name'])
       user_dt.append(request.form['your_username'])
       user_dt.append(request.form['your_email'])
       user_dt.append(request.form['your_password'])
       confirmation = request.form['confirm_your_password']
       user_dt = tuple(user_dt)

   if "" not in user_dt and user_dt[3] == confirmation:
        
        cursor.execute("insert into user_data(full_name, username,"
           "email, password) values(?, ?, ?, ?)", user_dt)
        connection.commit()
   else:
       flash("uncorrect data insertion")

   connection.close()

   return render_template("registering_page.html")

@app.route("/update_user", methods=["GET", "POST"])
def Update():
   global id
   user_dt = []
   connection = sqlite3.connect('agenda.db', check_same_thread=False)
   cursor = connection.cursor()
   if request.method == 'POST':
       user_dt.append(request.form['full_name'])
       if user_dt[0] != "":
           cursor.execute(f"UPDATE user_data SET full_name = ? WHERE id = ?",
    (user_dt[0], id))
           
       user_dt.append(request.form['username'])
       if user_dt[1] != "":
           cursor.execute(f"UPDATE user_data SET username = ? WHERE id = ?",
    (user_dt[1], id))
           
       user_dt.append(request.form['email'])
       if user_dt[2] != "":
           cursor.execute(f"UPDATE user_data SET email = ? WHERE id = ?",
    (user_dt[2], id))
           
       user_dt.append(request.form['password'])
       if user_dt[3] != "":
           cursor.execute(f"UPDATE user_data SET password = ? WHERE id = ?",
    (user_dt[3], id))
           
       user_dt = tuple(user_dt)

   connection.commit()

   connection.close()
   return redirect("/user_info")

@app.route("/delete_user", methods=["GET", "POST"])
def Delete():
   global id
   print(id)
   connection = sqlite3.connect('agenda.db', check_same_thread=False)
   cursor = connection.cursor()
   if request.method == 'POST':
       cursor.execute("Delete from user_data where id = ?", str(id))

   connection.commit()
   connection.close()

   return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
