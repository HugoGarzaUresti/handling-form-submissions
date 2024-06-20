from flask import render_template, redirect, url_for, request
from app import app
from app.forms import NameForm

@app.route('/', methods=['GET', 'POST'])
def form():
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        return redirect(url_for('result', name=name))
    return render_template('form.html', form=form)

@app.route('/result')
def result():
    name = request.args.get('name')
    return render_template('result.html', name=name)
