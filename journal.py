from flask import Flask, redirect, request, jsonify

import os
import sqlite3

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

# @app.route('/inspire')
# def getNum():
#     d_base = sqlite3.connect('inspire.db')
#     arg = request.args.get('quote')
#     quote_num = request.args.get('num')
#
#     if arg is None:
#         arg = 'default_query'
#
#     return redirect('/inspire?q={}&quote_num={}'.format(arg, quote_num))

# @app.route('/inspire', methods=['POST'])
# def post_handle():
#     d_base = sqlite3.connect('inspire.db')
#     if request.method == 'POST':


# @app.route("/delete/<int:id>", methods=['DELETE'])
# def delete_entry(id):
#     query = "DELETE from Inspirations WHERE id = '%s';"
#     cur = get_db.cursor()
#     cur.execute(query, (id,))
#     get_db.commit()

    # return redirect("/inspire")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True)
