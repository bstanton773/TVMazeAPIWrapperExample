from app import app
from app.wrappers import TVMazeAPI

if __name__ == '__main__':
    app.run(debug=True)


@app.shell_context_processor
def make_context():
    return {'client': TVMazeAPI()}