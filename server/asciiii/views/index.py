import flask
import asciiii
import os

@asciiii.app.route('/', methods=['GET', 'POST'])
def show_index():
    if flask.request.method == 'GET':
        context = {'ifcontent': False, 'ifdebug': False}
        return flask.render_template("index.html", **context)
    photo = asciiii.model.save_file(flask.request.files['file'])
    lines = flask.request.form['lines']
    eta = flask.request.form['etaRange']
    color = flask.request.form['color']
    light = flask.request.form['light']
    if photo == "":
        context = {'ifcontent': False, 'ifdebug': True}
        return flask.render_template("index.html", **context)
    print(photo, lines, eta, color, light)
    res = asciiii.model.create_ascii(photo, lines, eta, color, light)
    context = {'ifcontent': True, 'ifdebug' : False, 'origin': photo, 'ascii': res}
    return flask.render_template("index.html", **context)
