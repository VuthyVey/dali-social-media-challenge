from flask import Flask
from api.routes import configure_routes, stat_routes
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app = Flask(__name__)
configure_routes(app)
stat_routes(app)

if __name__ == '__main__':
    app.run(debug=True)