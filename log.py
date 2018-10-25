import logging
import logging.handler
import os
import sys
import time


def __setuplogging(logfile, loglevel, runAs, console=False):

    log = logging.getLogger()

    logfile = os.path.expanduser(logfile)
    if logfile == 'syslog':
        logStream = logging.handlers.SysLogHandler('/dev/log')
    elif logfile == 'stdout':
        logStream = logging.StreamHandler()
    else:
        lf = os.path.expanduser(logfile)
        logdir = os.path.dirname(lf)
        if not os.path.exists(logdir):
            os.makedirs(logdir)
        runuid = pwd.getpwnam(runAs).pw_uid
        rungid = pwd.getpwnam(runAs).pw_gid                  
        os.chown(logdir, runuid, rungid)
        logStream = logging.FileHandler(filename=lf)    

    FORMAT='%(asctime)s (UTC) [ %(levelname)s ] %(name)s %(filename)s:%(lineno)d %(funcName)s(): %(message)s'
    formatter = logging.Formatter(FORMAT)
    formatter.converter = time.gmtime  # to convert timestamps to UTC
    logStream.setFormatter(formatter)
    log.addHandler(logStream)

    # adding a new Handler for the console, 
    # to be used only for DEBUG and INFO modes. 
    if logLevel in [logging.DEBUG, logging.INFO]:
        if console:
            console = logging.StreamHandler(sys.stdout)
            console.setFormatter(formatter)
            console.setLevel(logLevel)
            log.addHandler(console)
    log.setLevel(logLevel)
    log.info('Logging initialized.')
