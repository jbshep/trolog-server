from flask import Flask, abort, request, jsonify
app = Flask(__name__)

from trolog.server.timer import TimerProxy

timer = TimerProxy()


@app.route('/api/init', methods=['POST'])
def init():
    f = request.form
    if not f.get('user') or not f.get('project'):
        abort(400)

    result = timer.init(f['user'], f['project'])
    return jsonify(result)


@app.route('/api/start', methods=['POST'])
def start():
    f = request.form
    if not f.get('user') or not f.get('project') or not f.get('label'):
        abort(400)

    result = timer.start(f['user'], f['project'], f['label'])
    return jsonify(result)


@app.route('/api/stop', methods=['POST'])
def stop():
    f = request.form
    if not f.get('user') or not f.get('project') or not f.get('label'):
        abort(400)

    result = timer.stop(f['user'], f['project'], f['label'])
    return jsonify(result)


@app.route('/')
def index():
    return 'Server running... brief documentation should go here'


app.run()
