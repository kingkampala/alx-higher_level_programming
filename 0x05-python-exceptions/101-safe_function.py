#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        func = fct(*args)
        return func
    except Exception as e:
        print('Exception: {}'.format(e), file=sys.stderr)
