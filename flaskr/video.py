from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
import os
from flaskr.db import get_db
from flaskr import UPLOAD_FOLDER
from flask import Flask
from flaskr.auth import login_required

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
bp = Blueprint('video', __name__)


@bp.route('/')
def index():
    db = get_db()
    videos = db.execute(
        'SELECT p.id, postername, filename, created, author_id, username'
        ' FROM video p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()

    for v in videos:
        v['posterloc'] = os.path.join(UPLOAD_FOLDER,v['postername'])
    return render_template('video/index.html', videos=videos)

@bp.route('/<int:id>/delete', methods=('GET',))
@login_required
def delete(id):
    db = get_db()
    db.execute('DELETE FROM video WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('video.index'))