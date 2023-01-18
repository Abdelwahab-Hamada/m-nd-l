from flask import (
    Flask,
    request,
    make_response
)

from auth_svc.views import (
    bp as auth_bp,
)

from post_svc.views import (
    bp as post_bp
)

from flask_cors import CORS

app=Flask(__name__)
CORS(app,supports_credentials=True,origins=['http://127.0.0.1:3000'])



app.register_blueprint(auth_bp)
app.register_blueprint(post_bp)

@app.after_request
def middleware_for_response(response):
    # Allowing the credentials in the response.
    return response



