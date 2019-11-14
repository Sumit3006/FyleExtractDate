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
    m = re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}", input_string)
    for s in m:
        return(s)

def match_type_7(input_string):
    m = re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{2}\s", input_string)
    for s in m:
        return(s)



def match_type_2(input_string):
    all = re.findall(r"[\d]{1,2}-[\d]{1,2}-[\d]{4}\s", input_string)
    for s in all:
        return(s)

def match_type_3(input_string):
    all = re.findall(r"[\d]{1,2} [ADFJMNOS]\w* [\d]{4}\s", input_string) 
    for s in all:
        print(s)

def match_type_4(input_string):
    all = re.findall(r"[\d]{1,2}/[ADFJMNOS]\w*/[\d]{4}\s", input_string) 
    for s in all:
        return(s)

def match_type_5(input_string):
    all = re.findall(r"[\d]{1,2} [adfjmnos]\w* [\d]{4}\s", input_string)
    for s in all:
        return(s)

def match_type_6(input_string):
    pattern = re.compile("^(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d$")
    all = re.findall(pattern, input_string)
    for s in all:
        return(s)
# print(read_file('output_processed.txt'))

def run_func(input_string):
    return_list = []
    return_list.append(match_type_1(input_string))    
    return_list.append(match_type_2(input_string)) 
    return_list.append(match_type_3(input_string)) 
    return_list.append(match_type_4(input_string)) 
    return_list.append(match_type_5(input_string)) 
    return_list.append(match_type_6(input_string)) 
    return_list.append(match_type_7(input_string)) 
    return return_list
    
    # match_type_2(input_string)
    # match_type_3(input_string)
    # match_type_4(input_string)
    # match_type_5(input_string)
    # match_type_6(input_string)
    # match_type_7(input_string)
