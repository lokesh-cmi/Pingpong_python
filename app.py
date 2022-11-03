from flask import Flask, render_template, request, url_for, redirect,render_template
app = Flask(__name__)
@app.route("/")
def index():
    return render_template('./index.html')

@app.route('/success')
def success():
    return "pong"

@app.route('/fail')
def fail():

    return "fail"

@app.route('/log' ,methods=['Post', 'Get'])
def log():
    if request.method == 'POST':
        user=request.form['ping']
        if user.lower()== 'ping':
            return redirect(url_for('success'))
        else:
            return redirect(url_for('fail'))

    else:
        user = request.args.get('ping')
        if user.lower()== 'ping':
            return redirect(url_for('success'))
        else:
            return redirect(url_for('fail'))

if __name__ == "__main__":
    app.run(debug=True)