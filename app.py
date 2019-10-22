from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
	{
		'name':'My store',
		'items':[{
				'name':'My item',
				'price':15.99
				}
   			] 
	}
]
#POST /store data: {name}
@app.route('/store',methods=['POST'])
def create_store():
	pass

#GET /store/<stringL:name>
@app.route('/store/<string:name>')
def get_store(name):
	pass

#GET /store
@app.route('/store')
def get_stores():
	pass

@app.route('/store/<string:name>/item',methods=['POST'])
def create_item_in_store(name):
    pass

@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    pass
 
app.run(port = 5000)	