class State(object):
    def handle(self, context): pass

class StateA(State):
    def handle(self, context):
        if isinstance(context.data, (int,float,complex)):
            print(f'{context.data} is a number')
        else:
            context.state = StateB()
            context.request()

class StateB(State):
    def handle(self, context):
        if isinstance(context.data, (bool,)):
            print(f'{context.data} is a bool')
        else:
            context.state = StateC()
            context.request()

class StateC(State):
    def handle(self, context):
        if isinstance(context.data, (str,)):
            print(f'{context.data} is a str')
        else:
            print(f'{context.data} is another type')

class Context(object):
    def __init__(self, data, state):
        self.data = data
        self.state = state
    def request(self): self.state.handle(self)

if __name__ == '__main__':
    Context(12, StateA()).request()
    Context(True, StateA()).request()
    Context('python', StateA()).request()
    Context([], StateA()).request()
