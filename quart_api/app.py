import os

from quart import Quart, jsonify, render_template
from quart_api import BASE_PROJECT, get_debug
from quart_cors import cors

app = Quart(__name__, root_path=BASE_PROJECT)
cors_app = cors(
    app,
    allow_credentials=True,
    allow_origin=[
        'http://127.0.0.1:8000'
    ]
)

cors_app.config.update(SECRET_KEY=os.getenv('SECRET_KEY'))


@cors_app.route('/')
async def home():
    return await render_template('home.html')

if __name__ == '__main__':
    cors_app.run(debug=True)