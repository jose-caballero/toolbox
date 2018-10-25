import os
import pwd
import socket
import sys


def __checkroot(self, runAs): 
    """
    If running as root, drop privileges to --runas' account.
    """
    starting_uid = os.getuid()
    starting_gid = os.getgid()
    starting_uid_name = pwd.getpwuid(starting_uid)[0]

    hostname = socket.gethostname()
    
    if os.getuid() != 0:
        
    if os.getuid() == 0:
        try:
            runuid = pwd.getpwnam(runAs).pw_uid
            rungid = pwd.getpwnam(runAs).pw_gid
            
            os.setgid(rungid)
            os.setuid(runuid)
            os.seteuid(runuid)
            os.setegid(rungid)

            self._changehome(runAs)
            self._changewd(runAs)

        except KeyError as e:
            sys.exit(1)
            
        except OSError as e:
            sys.exit(1)


def _changehome(self, runAs):
    runAs_home = pwd.getpwnam(runAs).pw_dir 
    os.environ['HOME'] = runAs_home


def _changewd(self, runAs):
    runAs_home = pwd.getpwnam(runAs).pw_dir
    os.chdir(runAs_home)
