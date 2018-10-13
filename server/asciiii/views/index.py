import flask
import asciiii


@asciiii.app.route('/', methods=['GET', 'POST'])
def show_index():
    if flask.request.method == 'GET':
        context = {'ifcontent': False}
        return flask.render_template("index.html", **context)
    photo = asciiii.model.save_file(flask.request.files['file'])
    lines = flask.request.form['lines']
    color = flask.request.form['color']
    res = asciiii.model.create_ascii(photo, lines, color)
    context = {'ifcontent': True, 'origin': photo, 'ascii': res}
    return flask.render_template("index.html", **context)
