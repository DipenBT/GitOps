# app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

# Remove debug=True and hard-coded host/port in production
if __name__ == "__main__":
    app.run(debug=True)
