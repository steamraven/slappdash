#__pragma__('skip')
this = None
#__pragma__('noskip')

def wrap(f):
    def inner():
        return f.call(this, this)
    return inner

