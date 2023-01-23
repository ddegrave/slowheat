from flask import Flask, request, render_template, url_for


app = Flask(__name__)

@app.route('/')

def index():
   Ta = request.args.get('Ta')
   if Ta:
      roomresultvalue=Ta
      return render_template('index.html', roomresult=roomresultvalue)
   else :
      return render_template('index.html', roomresult='Ta Not Found')

if __name__ == '__main__':
      app.run(debug=True)
