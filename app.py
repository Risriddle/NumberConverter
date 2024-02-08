from flask import *
from con import conversion

app = Flask(__name__)


@app.route('/')
def index():
    return redirect('/home')

buttons=[]
@app.route('/home',methods=['POST','GET'])
def home():
    if request.method=='POST':
      data = request.json
      number=data['number']
      f=data['from']
      to=data['to']
      c=data['c']
      if c:
        o=conversion(number,f,to)
        output={"msg":o}
        print(output)
        return jsonify(output)
      return render_template("home.html")
    
    return render_template("home.html")



if __name__ == '__main__':  
   app.run(debug = True)  