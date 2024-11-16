class User:
    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.role = kwargs['role']
        self.session = kwargs['session']

class Project:
    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.stages = kwargs['stages']