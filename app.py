from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/orders', methods=['POST'])
def write_order():
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address1_receive = request.form['address1_give']
    address2_receive = request.form['address2_give']
    phone_number_receive = request.form['phone_number_give']


    order = {
        'name': name_receive,
        'count': count_receive,
        'address1': address1_receive,
        'address2': address2_receive,
        'phone_number': phone_number_receive
    }

    db.orders.insert_one(order)

    return jsonify({'result': 'success', 'msg': 'Ordered successfully'})


@app.route('/orders', methods=['GET'])
def read_orders():
    orders = list(db.orders.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'orders': orders})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
