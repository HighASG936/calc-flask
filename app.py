from flask import Flask, render_template
from microservices.adder import adder_bp
from microservices.multiplier import multiplier_bp
from microservices.subtractor import subtractor_bp
from microservices.divider import divider_bp

app = Flask(__name__, template_folder='statics')

app.register_blueprint(adder_bp)
app.register_blueprint(multiplier_bp)
app.register_blueprint(subtractor_bp)
app.register_blueprint(divider_bp)

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
