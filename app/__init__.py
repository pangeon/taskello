from flask import Flask
from app.config import Config

app = Flask(
    __name__, 
    static_url_path='', 
    static_folder='web/static', 
    template_folder='web/templates'
)
app.config.from_object(Config)
from app import routes

