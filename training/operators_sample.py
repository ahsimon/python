import logging

def operator(a,b,oper):
        if oper in ['+','-','/','*']:
            c=eval(str(a)+ oper+ str(b))  
            logging.warning("the value of a %s b  is %f %f %f",oper,a,b,c)     
        else:
            logging.error("invalid operator %s",oper)   

operator(5,6,'+')        