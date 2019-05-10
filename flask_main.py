"""
개발자: 박성훈(hoonhoons.park@gmail.com)
마지막 수정: 2019-05-11

무학 QR 챌린지 2019용 웹 서버
QR코드를 찍으면 이 웹 서버 링크와 연결된다.
한 QR코드는 딱 두번까지만 이미지를 보여준다.
"""

from flask import Flask, request

this_app = Flask(__name__)

@this_app.route('/')
def index():
	return "박성훈의 flask 서버"
	
@this_app.route('/hello')
def hello():
	return "hello world"
	
if __name__ == '__main__':
	this_app.run(debug=True, host='0.0.0.0', port=5002, threaded=True)