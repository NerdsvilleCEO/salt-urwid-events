
def be_root_you_fool():
    import os
    if os.getuid() > 0:
        import sys
        a = [ x for x in sys.argv ]
        a.insert(0, a[0])
        a.insert(0, 'sudo')
        os.execlp(a[0], *a)
        print "error??"
        exit(1)

def setup_file_logger(tag='component-name-here', file='urwid-events.log', format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"):
    import logging, sys

    fh = logging.FileHandler(file)
    fh.setFormatter(logging.Formatter(format))
    logging.root.addHandler(fh)
    logging.root.setLevel(logging.DEBUG)
    logging.root.debug("logging configured")
    log = logging.getLogger(tag)
    class LogWriter(object):
        def __init__(self,fn):
            self.fn = fn
        def write(self,message):
            self.fn( message.rstrip() )
        def flush(self):
            pass
    sys.stderr = LogWriter(log.warning)
    return log
