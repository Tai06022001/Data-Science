#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
import numpy as np

# Task 2: Tiếp theo, bạn sẽ cần phân tích dữ liệu có trong tệp bạn vừa mở để đảm bảo rằng nó ở đúng định dạng
def check_valid_id(id_number):
    count = 0
    for num in id_number:
        if (num.isalpha()):
            count += 1
    if (count == 1 and len(id_number) == 9 and id_number[0] == 'N'):
        return True
    else:
        return False
    

def check_file_valid(file):
    count = 0
    valid_line = 0
    print('\n**** ANALYZING ****')
    for line in file:
        check = True
        count += 1
        line_split = line.split(',')
        if (len(line_split) != 26):
            print('Invalid line of data: does not contain exactly 26 values')
            print(line)
            check=False
        if (check_valid_id(line_split[0]) == False):
            print('Invalid line of data: N# is invalid')
            print(line)
            check=False
        if (check == True):
            valid_line += 1
    if (valid_line == count):
        print('No errors found!')
    print('\n**** REPORT ****')
    print('Total valid lines of data: ',valid_line)
    print('Total invalid lines of data',count-valid_line)
    file.seek(0)
    
# Task 3 Tiếp theo, bạn sẽ viết một chương trình để chấm điểm các bài thi cho một phần nhất định. 
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
def grade_calculation(answer_key,line):
    total_grade = 0
    answer = answer_key.split(',')
    for index in range(len(answer)):
        if (line[index] == answer[index]):
            total_grade += 4
        elif (line[index] != answer[index] and line[index]!=''):
            total_grade -= 1
        else:
            total_grade += 0
    return total_grade
    

def grade_calculation_dict(file, answer_key):
    grade_dict = {}
    for line in file:
        line = line.strip()
        line_split = line.split(',')
        if (len(line_split)==26 and check_valid_id(line_split[0])==True):
            line_cal = line_split[1:]
            grade = grade_calculation(answer_key,line_cal)
            grade_dict[line_split[0]]=grade
    return grade_dict

def metrics_calculation(file, answer_key):
    score = np.array([])
    grade_dict = grade_calculation_dict(file, answer_key)
    for key, value in grade_dict.items():
        score = np.append(score,value)
    print('Mean (average) score: ', np.mean(score))
    print('Highest score: ', np.max(score))
    print('Lowest score: ', np.min(score))
    print('Range of scores: ', np.max(score)-np.min(score))
    print('Median score: ', np.median(score)) 

# Task 4 Cuối cùng, yêu cầu chương trình của bạn tạo một tệp “kết quả” chứa các kết quả chi tiết cho từng học sinh trong lớp của bạn

def file_conversion(file,answer_key,filename):
    grade_dict = grade_calculation_dict(file, answer_key)
    grade_items = grade_dict.items()
    data_grade = pd.DataFrame(list(grade_items))
    name_file = filename+'_grades'+'.txt'
    data_grade.to_csv(name_file,index=False,header=False) 
    
# Task 1 Tiếp theo, viết một chương trình cho phép người dùng nhập tên của một tệp. Cố gắng mở tệp được cung cấp để truy cập đọc. 
import pandas as pd
import numpy as np
filename = input('Enter a class file to grade (i.e. class1 for class1.txt): ')
filename_use = filename + '.txt'
try:
    file = open(filename_use,"r")
    print('Successfully opened ',filename_use)
    check_file_valid(file)
    metrics_calculation(file,answer_key) 
    file_conversion(file,answer_key,filename)
except IOError:
    print('File cannot be found')

