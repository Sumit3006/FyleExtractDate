import re
import os

def read_file(filename):
    output_string = ""
    filehandle = open(filename)
    while True:
        line = filehandle.readline()
        output_string += line
        if not line:
            # pass
            return str(output_string) 


# input_string = '24/Jun/2019'

def match_type_1(input_string):
    m = re.findall(r"\s[\d]{1,2}[/ .-][\d]{1,2}[/ .-][\d]{4}\s", input_string)
    for s in m:
        x='-'
        s=s.strip()
        for a in s:
            if not a.isdigit():
                x=a
                break
        if s.count(x)<2:
            return
        l=s.split(r'{}'.format(x))
        print(l)
        mon=int(l[1])
        if(mon>12):
            p=[1,2,3]
            p[0]=l[2]
            p[1]=l[0]
            p[2]=l[1]
            return "-".join(p)
        else:
            p=[1,2,3]
            p[0]=l[2]
            p[1]=l[1]
            p[2]=l[0]
            return "-".join(p)    

def match_type_7(input_string):
    m = re.findall(r"\s[\d]{1,2}[/ .-][\d]{1,2}[/ .-][\d]{2}\s", input_string)
    for s in m:
        s=s.strip()
        x='-'
        for a in s:
            if not a.isdigit():
                x=a
                break
        if(s.count(x)<2):
            return 
        l=s.split(r'{}'.format(x))
        mon=int(l[1])
        year=int(l[2])
        if(mon>12):
            
            if year>19:
                year=19*100+year
            else:
                year=20*100+year    
            p=[1,2,3]
            p[0]=str(year)
            p[1]=l[0]
            p[2]=l[1]
            return "-".join(p)
        else:
            if year>19:
                year=19*100+year
            else:
                year=20*100+year    
            p=[1,2,3]
            p[0]=str(year)
            p[1]=str(mon)
            p[2]=l[0]
            return "-".join(p) 


def match_type_7a(input_string):
    m = re.findall(r"[\d]{1,2}[-][\d]{1,2}[-][\d]{2}\s", input_string)
    for s in m:
        s=s.strip()
        l=s.split(r'-')
        mon=int(l[1])
        year=int(l[2])
        if(mon>12):
            
            if year>19:
                year=19*100+year
            else:
                year=20*100+year    
            p=[1,2,3]
            p[0]=str(year)
            p[1]=l[0]
            p[2]=l[1]
            return "-".join(p)
        else:
            if year>19:
                year=19*100+year
            else:
                year=20*100+year    
            p=[1,2,3]
            p[0]=str(year)
            p[1]=l[1]
            p[2]=l[0]
            return "-".join(p) 

            
#07-May-2018
def match_type_8(input_string):
    all =re.findall(r'\s[\d]{1,2}[- /.]\w\w\w[- /.]\d\d\d\d\s', input_string)
    for s in all:
        s=s.strip()
        print("A"+s+"a")
        x='-'
        for a in s:
            if not a.isdigit():
                x=a
                break
        if s.count(x)<2:
            return
        l=s.split(r'{}'.format(x))
    
        mon=l[1]
        act_mon="00"
        if(re.findall(r'[jJ][aA][Nn]',mon)):
            act_mon="01"
        elif(re.findall(r'[fF][Ee][Bb]',mon)):
            act_mon="02"  
        elif(re.findall(r'[mM][aA][rR]',mon)):  
            act_mon="03"
        elif(re.findall(r'[aA][pP][rR]',mon)):
            act_mon="04"
        elif(re.findall(r'[mM][aA][Yy]',mon)):
            act_mon="05"
        elif(re.findall(r'[jJ][uU][nN]',mon)):
            act_mon="06"
        elif(re.findall(r'[jJ][uU][lL]',mon)):
            act_mon="07"
        elif(re.findall(r'[aA][uU][gG]',mon)):
            act_mon="08"
        elif(re.findall(r'[sS][eE][pP]',mon)):
            act_mon="09"
        elif(re.findall(r'[oO][cC][tT]',mon)):
            act_mon="10"    
        elif(re.findall(r'[nN][oO][vV]',mon)):
            act_mon="11"
        elif(re.findall(r'[dD][Ee][cC]',mon)):
            act_mon="12"
        if act_mon=="00":
            return "Null"    
        p=[1,2,3]
        p[0]=l[2]
        p[1]=act_mon
        p[2]=l[0]
        return "-".join(p)
#07-mAY-18
def match_type_8a(input_string):
    all =re.findall(r'\s[\d]{1,2}[- /.][A-Za-z]{3}[- /.]\d\d\s', input_string)
    for s in all:
        print(s)
        s=s.strip()
        x='-'
        for a in s:
            if not a.isdigit():
                x=a
                break
        if s.count(x)<2:
            return
        l=s.split(r'{}'.format(x))
        mon=l[1]
        act_mon="00"
        year=int(l[2])
        if year>19:
                year=19*100+year
        else:
                year=20*100+year
        year=str(year)
        if(re.findall(r'[jJ][aA][Nn]',mon)):
            act_mon="01"
        elif(re.findall(r'[fF][Ee][Bb]',mon)):
            act_mon="02"  
        elif(re.findall(r'[mM][aA][rR]',mon)):  
            act_mon="03"
        elif(re.findall(r'[aA][pP][rR]',mon)):
            act_mon="04"
        elif(re.findall(r'[mM][aA][Yy]',mon)):
            act_mon="05"
        elif(re.findall(r'[jJ][uU][nN]',mon)):
            act_mon="06"
        elif(re.findall(r'[jJ][uU][lL]',mon)):
            act_mon="07"
        elif(re.findall(r'[aA][uU][gG]',mon)):
            act_mon="08"
        elif(re.findall(r'[sS][eE][pP]',mon)):
            act_mon="09"
        elif(re.findall(r'[oO][cC][tT]',mon)):
            act_mon="10"    
        elif(re.findall(r'[nN][oO][vV]',mon)):
            act_mon="11"
        elif(re.findall(r'[dD][Ee][cC]',mon)):
            act_mon="12"
        if act_mon=="00":
            return "Null"    
        p=[1,2,3]
        p[0]=year
        p[1]=act_mon
        p[2]=l[0]
        return "-".join(p)       
                
def match_type_9(input_string):
    all =re.findall(r'[A-Za-z]{3}[- /.]{0,1}[\d]{1,2}[\w]{0,1}\d\d\s', input_string)
    for s in all:
        s=s.strip()
        mon=s[:3]
        day=" "
        if s[3].isdigit():
            day=s[3:5]
        else:
            day=s[4:6]
        if not day[1].isdigit():
            day=day[:1]
        year=int(s[-2:])

        act_mon="00"
        if year>19:
                year=19*100+year
        else:
                year=20*100+year
        year=str(year)
        if(re.findall(r'[jJ][aA][Nn]',mon)):
            act_mon="01"
        elif(re.findall(r'[fF][Ee][Bb]',mon)):
            act_mon="02"  
        elif(re.findall(r'[mM][aA][rR]',mon)):  
            act_mon="03"
        elif(re.findall(r'[aA][pP][rR]',mon)):
            act_mon="04"
        elif(re.findall(r'[mM][aA][Yy]',mon)):
            act_mon="05"
        elif(re.findall(r'[jJ][uU][nN]',mon)):
            act_mon="06"
        elif(re.findall(r'[jJ][uU][lL]',mon)):
            act_mon="07"
        elif(re.findall(r'[aA][uU][gG]',mon)):
            act_mon="08"
        elif(re.findall(r'[sS][eE][pP]',mon)):
            act_mon="09"
        elif(re.findall(r'[oO][cC][tT]',mon)):
            act_mon="10"    
        elif(re.findall(r'[nN][oO][vV]',mon)):
            act_mon="11"
        elif(re.findall(r'[dD][Ee][cC]',mon)):
            act_mon="12"
        if act_mon=="00":
            return "Null"    
        p=[1,2,3]
        p[0]=year
        p[1]=act_mon
        p[2]=day
        return "-".join(p)     
def match_type_10(input_string):
    all =re.findall(r'\s\w\w\w[- /.][\d]{1,2}[- /.]\d\d\d\d\s', input_string)
    for s in all:
        s=s.strip()
        x='-'
        for a in s:
            if not a.isdigit():
                x=a
                break
        if s.count(x)<2:
            return
        l=s.split(r'{}'.format(x))
        mon=l[0]
        act_mon="00"
        year=l[2]
        if(re.findall(r'[jJ][aA][Nn]',mon)):
            act_mon="01"
        elif(re.findall(r'[fF][Ee][Bb]',mon)):
            act_mon="02"  
        elif(re.findall(r'[mM][aA][rR]',mon)):  
            act_mon="03"
        elif(re.findall(r'[aA][pP][rR]',mon)):
            act_mon="04"
        elif(re.findall(r'[mM][aA][Yy]',mon)):
            act_mon="05"
        elif(re.findall(r'[jJ][uU][nN]',mon)):
            act_mon="06"
        elif(re.findall(r'[jJ][uU][lL]',mon)):
            act_mon="07"
        elif(re.findall(r'[aA][uU][gG]',mon)):
            act_mon="08"
        elif(re.findall(r'[sS][eE][pP]',mon)):
            act_mon="09"
        elif(re.findall(r'[oO][cC][tT]',mon)):
            act_mon="10"    
        elif(re.findall(r'[nN][oO][vV]',mon)):
            act_mon="11"
        elif(re.findall(r'[dD][Ee][cC]',mon)):
            act_mon="12"
        if act_mon=="00":
            return "Null"    
        p=[1,2,3]
        p[0]=year
        p[1]=act_mon
        p[2]=l[0]
        return "-".join(p)


def match_type_11(input_string):
    all =re.findall(r'\s[\d]{1,2}[- /.]\w\w\w[- /.]\d\d\d\d\s', input_string)
    for s in all:
        x='-'
        s=s.strip()
        for a in s:
            if not a.isdigit():
                x=a
                break
        if s.count(x)<2:
            return
        l=s.split(r'{}'.format(x))
        mon=l[1]
        act_mon="00"
        year=l[2]
        if(re.findall(r'[jJ][aA][Nn]',mon)):
            act_mon="01"
        elif(re.findall(r'[fF][Ee][Bb]',mon)):
            act_mon="02"  
        elif(re.findall(r'[mM][aA][rR]',mon)):  
            act_mon="03"
        elif(re.findall(r'[aA][pP][rR]',mon)):
            act_mon="04"
        elif(re.findall(r'[mM][aA][Yy]',mon)):
            act_mon="05"
        elif(re.findall(r'[jJ][uU][nN]',mon)):
            act_mon="06"
        elif(re.findall(r'[jJ][uU][lL]',mon)):
            act_mon="07"
        elif(re.findall(r'[aA][uU][gG]',mon)):
            act_mon="08"
        elif(re.findall(r'[sS][eE][pP]',mon)):
            act_mon="09"
        elif(re.findall(r'[oO][cC][tT]',mon)):
            act_mon="10"    
        elif(re.findall(r'[nN][oO][vV]',mon)):
            act_mon="11"
        elif(re.findall(r'[dD][Ee][cC]',mon)):
            act_mon="12"
        if act_mon=="00":
            return "Null"    
        p=[1,2,3]
        p[0]=year
        p[1]=act_mon
        p[2]=l[0]
        return "-".join(p)                  
def match_type_12(input_string):
    m = re.findall(r"\s[\d]{4}[/ .-][\d]{1,2}[/ .-][\d]{1,2}\s", input_string)
    for s in m:
        s=s.strip()
        x='-'
        for a in s:
            if not a.isdigit():
                x=a
                break
        if s.count(x)<2:
            return
        l=s.split(r'{}'.format(x))
        mon=int(l[1])
        if(mon>12):
            p=[1,2,3]
            p[0]=l[0]
            p[1]=l[2]
            p[2]=l[1]
            return "-".join(p)
        else:
            p=[1,2,3]
            p[0]=l[0]
            p[1]=l[1]
            p[2]=l[2]
            return "-".join(p)    
# print(read_file('output_processed.txt'))

def run_func(input_string):
    return_list = []
    return_list.append(match_type_1(input_string))     
    return_list.append(match_type_7(input_string)) 
    return_list.append(match_type_8(input_string))
    return_list.append(match_type_8a(input_string))
    return_list.append(match_type_9(input_string)) 
    return_list.append(match_type_10(input_string))
    return_list.append(match_type_11(input_string))
    return_list.append(match_type_12(input_string))
    return return_list
    
    # match_type_2(input_string)
    # match_type_3(input_string)
    # match_type_4(input_string)
    # match_type_5(input_string)
    # match_type_6(input_string)
    # match_type_7(input_string)
