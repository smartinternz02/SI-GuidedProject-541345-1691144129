from flask import Flask, render_template,request
import ibm_db
app= Flask (__name__) 
conn= ibm_db.connect("database=bludb; hostname=6667d8e9-9d4d-4ccb-ba32-21da3bb5aafc.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud; port=30376; UID=bjx62090; PWD=eW9010O8ovK6emVI; SECURITY = SSL;SSLSERVERCERTIFICATE = DigiCertGlobalRootCA.crt", ' ',' ')
ibm_db.active(conn)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method =="POST":
      uname =  request.form['username']
      pword = request.form['password']
      print(uname,pword)
      sql = 'SELECT *FROM REGISTER WHERE USERNAME=?' 
      stmt = ibm_db.prepare(conn, sql)
      ibm_db.bind_param(stmt,1, uname) 
      ibm_db.bind_param(stmt,2, pword)
      ibm_db.execute(stmt)
      out = ibm_db.fetch_assoc(stmt)
      print(out)
      if out == False:
         msg = "Invalid Credentials"
         return render_template("login.html", login_message=msg)
      else: 
         role = out['ROLE']
         if role == 0:
            return render_template("Adminprofile.html")
    elif role== 1:
       return render_template("facultyprofile.html")
    elif role== 2:
     return render_template("studentprofile.html")
if __name__ == "main":
   app.run(debug= True)