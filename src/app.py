from flask import Flask
from config import config
from routes import record_routes

app = Flask(__name__)

def page_not_found(error):
    return "<h1>No encontrado</h1>", 404

if __name__ == "__main__":
    app.config.from_object(config['development'])
    
    app.register_blueprint(record_routes.main, url_prefix='/api/records')
    
    app.register_error_handler(404, page_not_found)
    
    app.run()
