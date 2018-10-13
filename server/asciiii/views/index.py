import flask
import asciiii


@asciiii.app.route('/', methods=['GET', 'POST'])
def show_index():
    if flask.request.method == 'GET':
        context = {'ifcontent': False, 'ifdebug': False}
        return flask.render_template("index.html", **context)
    photo = asciiii.model.save_file(flask.request.files['file'])
    if photo == "":
        context = {'ifcontent': False, 'ifdebug': True}
        return flask.render_template("index.html", **context)
    lines = flask.request.form['lines']
    color = flask.request.form['color']
    res, res_ascii = asciiii.model.create_ascii(photo, lines, color)
    print(photo, lines, colors)
    context = {'ifcontent': True, 'ifdebug' : False, 'origin': photo, 'ascii': res_ascii}
    return flask.render_template("index.html", **context)
