from flask import Flask, render_template, request, jsonify
 
app = Flask(__name__)

data_m = {'mode': 'NONE'}

 
@app.route('/')
def index():
	return render_template('index.html')
 

@app.route('/mode_mic/', methods=['POST'])
def mode_mic():
	global data_m
	data_m = {'mode': 'MIC'}
	return jsonify(data_m),204
	
@app.route('/mode_rehearsal/', methods=['POST'])
def mode_rehearsal():
	global data_m
	data_m = {'mode': 'REHEARSAL'}
	return jsonify(data_m),204

@app.route('/mode_air/', methods=['POST'])
def mode_air():
	global data_m
	data_m = {'mode': 'AIR'}
	return jsonify(data_m),204

@app.route('/mode_door/', methods=['POST'])
def mode_door():
	global data_m
	data_m = {'mode': 'DOOR'}
	return jsonify(data_m),204

@app.route('/mode_none/', methods=['POST'])
def mode_none():
	global data_m
	data_m = {'mode': 'NONE'}
	return jsonify(data_m),204
 
@app.route('/mode/', methods=['GET'])
def get_mode():
	global data_m
	return jsonify(data_m)

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0')