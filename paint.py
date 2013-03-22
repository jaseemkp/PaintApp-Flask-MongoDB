from flask import Flask, render_template, request, redirect
from pymongo import Connection

app = Flask(__name__)

connection = Connection()
collection = connection.paintdb.drawings

@app.route('/', methods=['GET', 'POST'])
def paint():
    if request.method == 'GET':
        all_data = {}
        datas = collection.find()
        for data in datas:
            all_data[data["fname"]] = data["image_data"]
        return render_template('paint.html', py_all= all_data)
    elif request.method == 'POST':
        filename = request.form['fname']
        data = request.form['whole_data']
        collection.insert({"fname":filename, "image_data":data})
        return redirect('/')

if __name__ == '__main__':
   app.run()
