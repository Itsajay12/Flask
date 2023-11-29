from flask import Flask
from flask import render_template
app=Flask(__name__)
@app.route('/')
def main_page():
    return render_template('index.html')
@app.route('/pro')
def pro_page():
    return render_template('propage.html')
if __name__=='__main__':
    app.run(debug=True,port=8002)