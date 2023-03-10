# CS 361 Microservice
# Vi Nguyen
# 2/13/23

from flask import Flask, request, jsonify

import os
import sqlite3
import random

app = Flask(__name__)

#Default route which returns all quotes of inspiration
@app.route('/inspire', methods=['GET'])
def get_handle():
    d_base = sqlite3.connect('inspire.db')
    if request.method == 'GET':
        query1 = "SELECT * FROM Inspirations"
        cur = d_base.cursor()
        cur.execute(query1)
        data = cur.fetchall()
        d_base.close()
        return jsonify(data)

#Route that handles specific searches with ID number
@app.route('/inspire/<int:id_input>', methods=['GET'])
def get_ID(id_input):
    d_base = sqlite3.connect('inspire.db')
    if request.method == 'GET':
        query = "SELECT * FROM Inspirations WHERE id = %s" % (id_input,)
        cur = d_base.cursor()
        cur.execute(query)
        data = cur.fetchone()
        d_base.close()
        return jsonify(data)

#Route that handles specific searches with a string keyword
@app.route('/inspire/<string:str_input>', methods=['GET'])
def get_str(str_input):
    d_base = sqlite3.connect('inspire.db')
    if request.method == 'GET':
        query = "SELECT * FROM Inspirations WHERE quote LIKE '%{}%'".format(str_input)
        cur = d_base.cursor()
        cur.execute(query)
        data = cur.fetchone()
        d_base.close()
        return jsonify(data)

#Route that returns random quotes from database
@app.route('/inspire/random', methods=['GET'])
def get_random():
    d_base = sqlite3.connect('inspire.db')
    ran_num = random.randint(1,50)
    if request.method == 'GET':
        query = "SELECT * FROM Inspirations WHERE id = ?"
        cur = d_base.cursor()
        cur.execute(query, (ran_num,))
        data = cur.fetchone()
        d_base.close()
        return jsonify(data)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True)
