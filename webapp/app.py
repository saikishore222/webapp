from flask import Flask,render_template
import pymongo
app = Flask(__name__)
myclient = pymongo.MongoClient("mongodb://localhost:5000/")
mydb=myclient["mydatabase"]
mycol=mydb["users"]
@app.route('/')
def index():
    return render_template('login.html')
if __name__ == '__main__':
   app.run(debug = True)