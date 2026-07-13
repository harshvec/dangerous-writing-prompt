from flask import Flask,render_template,request
from flask_bootstrap import Bootstrap



app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
  return render_template('index.html')



@app.route("/write")
def writing_page():
    seconds = request.args.get('seconds', default=5, type=int)
    return render_template('write.html', idle_seconds=seconds)

@app.route('/idle', methods=['POST'])
def idle():
    print("User went idle for 5 seconds!")
    return {"status": "wiped"}, 200


if __name__=='__main__':
  app.run(debug=True)