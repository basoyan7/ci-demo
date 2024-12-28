from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return "<h1>Hello World!</h1><p>This is the home page.</p>"

# Route to return a JSON response
@app.route('/api/data', methods=['GET'])
def get_data():
    sample_data = {
        "id": 1,
        "name": "Flask App",
        "description": "This is a sample API endpoint."
    }
    return jsonify(sample_data)

# Route with URL parameters
@app.route('/greet/<name>', methods=['GET'])
def greet(name):
    return f"<h1>Hello, {name}!</h1>"

# Route to handle POST request
@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    name = data.get("name", "Guest")
    return jsonify({"message": f"Data received from {name}"})

# Route for rendering a template
@app.route('/about')
def about():
    return render_template('about.html', title="About Page")

# Run the app
if __name__ == '__main__':
    app.run(host="0.0.0.0")
