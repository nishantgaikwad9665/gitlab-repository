from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Paresh! 🚀 Your Python app is running in Docker."

#Expose
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
