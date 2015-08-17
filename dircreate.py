#simple testscript to create directory with 100 char length
#Michael Peer michael@michael-peer.net
#v0.1
#17/08/2015

import os;
dir_name="x"
for y in range (1,100):
    dir_name=dir_name+"x";    
print dir_name
if not os.path.exists(dir_name):
    os.makedirs(dir_name)
