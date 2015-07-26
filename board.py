"""
http://stackoverflow.com/questions/10158701/how-to-capture-output-of-curl-from-python-script
https://gist.github.com/gdamjan/2578080
"""

import subprocess
import sys


def clients(local_port, ssh_port='22'):
    SSH = 'ssh'
    #if sys.platform == 'win32':
     #   SSH = 'plink.exe'

    cmd = ['autossh', '-R', '0.0.0.0:%s:localhost:22' % local_port, 'openflow@83.212.121.12']
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # the ssh daemon sends the client this message, about the port it allocated
    # on the daemon side. we can't get that info easily in the server script so
    # just send it over from client side.
    msg = p.stderr.readline()
    p.stdin.write(msg)
    # now we wait for an url allocation
    url = p.stdout.readline()
    print url.strip()
    # and now just wait forever
    p.wait()

proc = subprocess.Popen(["curl", str(sys.argv[1])], stdout=subprocess.PIPE)
(out, err) = proc.communicate()
print ("Socket given is %s" % str(out))
a = clients(str(out))



#store port

#autossh ssh -R boxmainframe:<port_received>:localhost:22 boxuser@boxmainframe
# need keys to connect without passwd use keys
# "TCPKeep Alive"??
