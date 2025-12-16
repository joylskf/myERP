from flask import Flask, render_template
from master.partner import partner_bp

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="首頁")

app.register_blueprint(partner_bp, url_prefix="/master")

if __name__ == "__main__":
    app.run(debug=True)