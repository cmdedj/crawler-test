from flask import Flask, render_template


def create_app():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = "cmdedj"
	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)
	return app