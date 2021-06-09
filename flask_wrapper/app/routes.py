from flask import render_template, request
from app import app
from app.forms import TVShowSearchForm
from app.wrappers import TVMazeAPI

client = TVMazeAPI()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = TVShowSearchForm()
    show_list = None
    if request.method == 'POST' and form.validate():
        show = form.title.data
        show_list = client.search_shows(show)
    return render_template('index.html', form=form, show_list=show_list)