from flask import Flask, render_template
from flask_sqlalchemy import *
import pandas as pd
from sqlalchemy import insert
from werkzeug import datastructures

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:dexter@localhost/postgres"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

engine = sqlalchemy.create_engine('postgresql://postgres:dexter@localhost/postgres')

db = SQLAlchemy(app)

class CSV(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    file_name=db.Column(db.String(200))
    

@app.route('/',methods = ['POST', 'GET'])
def result():
    data = pd.read_csv(r"C:\Users\Syn_A\syno.csv")
    data.to_sql( name="syno",con=engine)
    query=''' SELECT * FROM syno where fname='Nishant' '''
    data = pd.read_sql_query(query, engine)
    header = data.columns
    data = data.to_numpy()
    result = {"header": header, "body": data}
    print(data)
    return render_template("table.html", data=result)

if __name__ == '__main__':
    app.run()
  

