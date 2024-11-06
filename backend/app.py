from flask import Flask
from routes import crop_monitoring, marketplace, fintech
from database import db_setup

app = Flask(__name__)
app.config.from_object("config.Config")

# Register blueprints for modular routes
app.register_blueprint(crop_monitoring.bp, url_prefix="/api/crop")
app.register_blueprint(marketplace.bp, url_prefix="/api/marketplace")
app.register_blueprint(fintech.bp, url_prefix="/api/fintech")

# Initialize database
db_setup.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
