#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        put = fct(*args)
        return put
    except Exception as err:
        print("Exception: {}".format(0), file=sys.stderr)
        return None
