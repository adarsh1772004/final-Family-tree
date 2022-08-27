from flask import Flask,render_template
app=Flask(__name__,template_folder='templates')
@app.route('/Adarsh')
def showAdarsh():
    return render_template('adarsh.html')
@app.route('/Uncle')
def showuncle():
    return render_template('uncle.html')
@app.route('/Dad')
def showdad():
    return render_template('dad.html')
@app.route('/Mom')
def showMom():
    return render_template('mom.html')
app.run(debug=True)
