class TimerProxy:
    def __init__(self):
        pass

    def init(self, user, project):
        return {
            'key': 'xyz123'
        }

    def start(self, user, project, label):
        return {
            'result': 'ok'
        }
        
    def stop(self, user, project, label):
        return {
            'result': 'error',
            'type': 'no_start',  # other valid error type is 'dup_start'
        }
