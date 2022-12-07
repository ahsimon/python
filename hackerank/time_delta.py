import os
import datetime
import logging


FORMATTER="%a %d %b %Y %H:%M:%S %z"
LINE_SEPARATOR="\n"
def time_delta(t1, t2):
    dt1 = datetime.datetime.strptime(t1,FORMATTER)
    dt2 = datetime.datetime.strptime(t2,FORMATTER)
    diff = dt1 -dt2
    delta = abs(int(diff.total_seconds()))
    return str(delta)


if __name__== '__main__':
    logging.basicConfig(level=logging.DEBUG)
    outFile = open(os.environ["OUT_PATH"],'w')
    inFile =  open(os.environ["IN_PATH"],'r',newline='\n',encoding='utf8')
    
    lines= int(inFile.readline())
    logging.debug(lines)
    for line in range(lines):
        t1=inFile.readline().strip()
        t2=inFile.readline().strip()
        logging.debug(t1)
        logging.debug(t2)
        value = time_delta(t1,t2)
        logging.debug(value)
        outFile.write(value+LINE_SEPARATOR)
    outFile.close()  
    inFile.close()   