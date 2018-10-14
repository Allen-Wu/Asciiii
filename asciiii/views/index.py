import flask
import asciiii
from asciiii import model, util


@asciiii.app.route('/', methods=['GET', 'POST'])
def show_index():
    if flask.request.method == 'GET':
        context = {'ifcontent': False, 'ifdebug': False}
        return flask.render_template("index.html", **context)
    photo = model.save_file(flask.request.files['file'])
    lines = flask.request.form['lines']
    eta = flask.request.form['etaRange']
    # color = flask.request.form['color']
    color = '0'
    light = flask.request.form['light']
    if photo == "":
        context = {'ifcontent': False, 'ifdebug': True}
        return flask.render_template("index.html", **context)
    res = model.create_ascii(photo, lines, eta, color, light)
    print("-----", res)
    context = {'ifcontent': True, 'ifdebug': False, 'original': '/var/uploads/' + photo, 'ascii': res}
    return flask.render_template("index.html", **context)
