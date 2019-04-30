

from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
@app.route("/hello")
def hello_world():
	return "hello world"

@app.route("/test/<query_parameter>")
def search(query_parameter):
	return query_parameter

@app.route("/path/<path:value>")
def path_type(value):
	print(value)
	return"correct"


@app.route("/name/<name>")
def index(name):
	if name.lower() == "micheal":
		return "hello {}".format(name), 200
	else:
		return "NOT FOUND ",404




if __name__ == "__main__":
	app.run()
