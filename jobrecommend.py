from bottle import run, route, view, static_file

from src.Scrapper import startCrawling


@route('/')
@view('index')
def index():
    jobList = startCrawling()
    print(jobList[0].link)
    return dict(
        jobs = jobList
    )
    # pass

@route('/static/<filepath:path>')
def load_static(filepath):
    return static_file(filepath, root='./static')
# Start the website
run(host='0.0.0.0', port=8080, reloader=True, debug=True)