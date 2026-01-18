# app/main.py

from flask import Flask
from app.api.predict import predict_bp
from app.api.alerts import alerts_bp
from app.api.retrain import retrain_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(predict_bp, url_prefix="/api")
    app.register_blueprint(alerts_bp, url_prefix="/api")
    app.register_blueprint(retrain_bp, url_prefix="/api")

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
