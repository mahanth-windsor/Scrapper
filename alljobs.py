from bottle import run, route, view, static_file, debug

from Scrapper import startCrawling
from job_recommender import getRowsWithHeading


@route('/alljobs')
@view('index')
def index():
    jobList = startCrawling()
    return dict(
        title="All Jobs",
        jobs=jobList
    )
    # pass

@route('/static/<filepath:path>')
def load_static(filepath):
    return static_file(filepath, root='./static')
# Start the website
run(host='0.0.0.0', port=8080, reloader=True, debug=True)

@route('/recommended')
@view('index')
def index():
    jobList = getRowsWithHeading()
    return dict(
        title="All Jobs",
        jobs=jobList
    )

debug(True)
run()