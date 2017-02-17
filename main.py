from flask import Flask, render_template, request, redirect, url_for
from rename import run_it
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        directory = request.form['directory']
        extensions = request.form.getlist('extensions')
        if extensions:
          run_it(path=directory, extensions=extensions)
        return redirect(url_for('main'))
    else:
        return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)