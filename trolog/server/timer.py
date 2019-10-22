from itsdangerous import URLSafeSerializer
import os

class TimerProxy:
    def __init__(self):
        pass

    def generate_key(self, user, project):
        auth_s = URLSafeSerializer(os.environ['SECRET_KEY'], 'auth')
        project_key = auth_s.dumps({'user': user, 'project': project})
        return project_key

    def get_user_project_from_key(self, project_key):
        auth_s = URLSafeSerializer('FIXME_READ_FROM_ENV', 'auth')
        data = auth_s.loads(project_key)
        return data['user'], data['project']

    def init(self, user, project):
        project_key = self.generate_key(user, project)

        # FIXME
        # Once generated, the key should be stored along with the
        # project name and the user name who created the project.
        # When something calls start() or stop(), the project key
        # can be passed to self.get_user_project_from_key()
        # to determine where the label should be logged.

        return {
            'key': project_key
        }

    def start(self, user, project_key, label):
        return {
            'result': 'ok'
        }
        
    def stop(self, user, project_key, label):
        return {
            'result': 'error',
            'type': 'no_start',  # other valid error type is 'dup_start'
        }
