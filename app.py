import os
from flask import Flask, render_template
from JobSearchAgreggator.py import rodar

app = Flask(__name__)

@app.route('/')
def index():
    jobs = rodar()
    return render_template('index.html', jobs=jobs.to_html())

if __name__ == '__main__':
    app.run(port=int(os.environ.get('PORT', 5000)), debug=True)
