import os
from flask import Flask, flash, request, redirect, url_for
from flaskr.db import get_db
from flaskr import UPLOAD_FOLDER
from werkzeug.utils import secure_filename
from flask import send_from_directory
from flaskr.auth import login_required
from .utils import cephboto
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

UPLOAD_FOLDER=os.path.join(__name__.split('.')[0],UPLOAD_FOLDER)
bp = Blueprint('upload', __name__, url_prefix='/upload')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@bp.route('/', methods=('GET', 'POST'))
@login_required
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        poster = request.files['poster']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            postername = secure_filename(poster.filename)
            poster.save(os.path.join(UPLOAD_FOLDER, postername))
            #save file by boto to ceph
            cephboto.save_file(filename, file)
            # insert database
            insert_db(postername, filename)

            return redirect(url_for('video.index'))
    return render_template('upload/index.html')

@bp.route('/files/<filename>')
def uploaded_file(filename):
     return send_from_directory(UPLOAD_FOLDER,
                                filename)

def insert_db(postername, filename):
    db = get_db()
    db.execute(
        'INSERT INTO video (postername, filename, author_id)'
        ' VALUES (?, ?, ?)',
        (postername, filename, g.user['id'])
    )
    db.commit()
