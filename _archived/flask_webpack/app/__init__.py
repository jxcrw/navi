from flask import Flask, render_template
from flask_webpack import Webpack

from flask_webpack import Webpack
webpack = Webpack()

def create_app(settings_override=None):
    """
    Create a test application.
    :param settings_override: Override settings
    :type settings_override: dict
    :return: Flask app
    """
    app = Flask(__name__)

    params = {
        'DEBUG': True,
        'WEBPACK_MANIFEST_PATH': './manifest.json'
    }

    app.config.update(params)

    if settings_override:
        app.config.update(settings_override)

    webpack.init_app(app)
    return app

app = create_app()
# app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
