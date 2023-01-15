from flask import (
    Flask,
)

from auth_svc.views import (
    bp as auth_bp,
)

from post_svc.views import (
    bp as post_bp
)

app=Flask(__name__)

app.register_blueprint(auth_bp)
app.register_blueprint(post_bp)


