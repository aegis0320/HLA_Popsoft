from flask import Flask, render_template

import config
from exts import db

from blueprints import index_bp
from blueprints import user_bp
from blueprints import data_bp

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

app.register_blueprint(index_bp)
app.register_blueprint(user_bp)
app.register_blueprint(data_bp)


@app.route("/jq")
def login():
    return render_template("JQtry.html")


if __name__ == '__main__':
    app.run()
