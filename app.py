from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return '登楼项目启动成功！准备部署 Railway'

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
        
        