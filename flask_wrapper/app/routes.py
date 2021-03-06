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


@app.route('/show/<int:id>')
def show_info(id):
    show = client.get_show_info(id)
    return render_template('show.html', show=show)


@app.route('/actor/<int:id>/shows')
def actor_shows(id):
    shows = client.get_actor_cast_credits(id)
    actor = client.get_actor_data(id)
    return render_template('actor_shows.html', shows=shows, actor=actor)