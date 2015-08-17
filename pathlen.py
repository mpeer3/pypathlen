#PyPathLen directory length checker
#Michael Peer michael@michael-peer.net
#v0.1
#17/08/2015

import os,sys,getopt
# Global default values
def_path= "./" # Default directory
def_alert=200  # Alert if path length >= def_alert
def_fail=255   # Alert if path length >= def_fail 
# Please note: def_fail must be >= def_alert
# Error handler
def errors(ind):
 if ind==1:
     print "Error #1: No options specified. Try '-h'"
     sys.exit(2)
 elif ind==2:
     print "Error #2: Param 'Alert' - Out of range (0-255)...using default (200)"
 elif ind==3:
     print "Error #3: Param 'Alert' - No integer (0-255)...using default (200)"  
 elif ind==4:
     print "Error #4: Param 'Fail' - Out of range (0-255)...using default (255)"
 elif ind==5:
     print "Error #5: Param 'Fail' - No integer (0-255)...using default (255)"
 elif ind==6: 
     print "Error #6: Wrong syntax. Get help with '-h'"
     sys.exit(2)
 elif ind==7:
     print "Error #4: Invalid pathname...using default ('./')" 

#Directory Scanner Function plus Analyzer
def scan(path,alert,fail):
    results=[]
    #Get all subdirectories and files, store complete pathnames in list
    for dir_name,subdirs,files in os.walk(path):
       for f in files:
           res=os.path.join(dir_name,f)      
           results.append(res)
       for s in subdirs:
           res=os.path.join(dir_name,s)
           results.append(res)
       results.sort()
    #Check length of each pathname
    for res in results:
       flen=len(res)
       status="[OK   ]";
       if flen < alert:
           status="[OK   ]"
       elif flen < fail:
           status="[ALERT]"
       else:
        status="[FAIL ]"
       print status + " " + res + " ("+str(flen)+")"
#Main - parse commandline options and arguments 
def main(argv):
    try:
        opts,args=getopt.getopt (argv,"ha:f:p:")
    except getopt.GetoptError:
        errors(6);
       
    mpath= def_path
    malert=def_alert
    mfail=def_fail
    for opt, arg in opts:
        if opt == "-h":
             print "Usage: pathlen.py -p pathname [-a alert_at -f fail_at]"
             print "Default values: Alert=200, Fail=255"
             sys.exit(2)
        if opt == "-p":
            if os.path.isdir(arg):
                mpath=arg
            else:
                errors(7);
        elif opt == "-a":
            try:
                alert_inp=int(arg)
                if alert_inp <= 255:
                    malert=alert_inp
                else:
                    errors(2)
            except ValueError:
                    errors(3)
        elif opt == "-f":
            try:
                fail_inp=int(arg)
                if fail_inp <= 255:
                    mfail=fail_inp
                else:
                    errors(4)
            except ValueError:
                 errors(5)

    print "Parameters:"
    print "...Directory = " + mpath
    print "...Alert at  = " + str(malert)
    print "...Fail  at  = " + str(mfail)
    scan(mpath,malert,mfail) 

if __name__ == "__main__":
    print "Path length checker v0.1 by Michael Peer"
    print "========================================="
    if len(sys.argv)==1:
        errors(1)
    main(sys.argv[1:])


