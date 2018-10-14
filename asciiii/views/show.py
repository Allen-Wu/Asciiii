import flask
import asciiii

@asciiii.app.route('/uploads/<path:filename>')
def show(filename):
    print('*****************8')
    """show upload files."""
    return flask.send_from_directory(
        asciiii.app.config['UPLOAD_FOLDER'], filename
    )