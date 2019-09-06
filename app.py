from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import threading

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

class observador(threading.Thread):
   def run(self):
      print ("Acaba de entrar a la Lista")

class observador1(threading.Thread):
   def run(self):
      print ("Acaba de entrar al Json")

class Singleton:
	_instance = None
	
	def __new__(cls, *args, **kwargs):
		if not cls._instance:
			cls._instance = object.__new__(cls, *args, **kwargs)
		
		return cls._instance

class datosl(Singleton):
  t=[]
  resultado= db.engine.execute('select * from users;')
  for row in resultado:
    t.append(row)
  
lista1=datosl.t
lis=datosl.t

@app.route('/')
def inicio():
 
  return render_template('lista.html')

@app.route('/users/list')
def usersJ():
  tt = observador()
  tt.start()

  print (hex(id(lista1)))
  return render_template('index.html',lista=lista1)

@app.route('/api/v1/users')
def usersJson():
  t = observador1()
  t.start()
  datos=[]
  print (hex(id(lis)))
  for i in range(len(lis)):
    datos.append({'Firstname':lis[i][0],'Lastname':lis[i][1],'Username':lis[i][2],'Email':lis[i][3],'Password':lis[i][4]})
  return jsonify(datos)
 
app.run(debug=True, host="0.0.0.0")
