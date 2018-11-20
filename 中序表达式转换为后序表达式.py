# -*- coding: utf-8 -*-
# @Time    : 2018/10/31 0031 下午 2:49
# @Author  : 杨宏兵
# @File    : 中序表达式转换为后序表达式.py
# @Software: PyCharm



MAX = 50
infix_q = ['']*MAX


def compare(stack_o, infix_o):
    infix_priority = ['']*9
    stack_priority = ['']*8
    index_s = index_i = 0
    infix_priority[0] = 'q'; infix_priority[1] = ')';
    infix_priority[2] = '+'; infix_priority[3] = '-';
    infix_priority[4] = '*'; infix_priority[5] = '/';
    infix_priority[6] = '^'; infix_priority[7] = ' ';
    infix_priority[8] = '(';

    stack_priority[0] = 'q'; stack_priority[1] = '(';
    stack_priority[2] = '+'; stack_priority[3] = '-';
    stack_priority[4] = '*'; stack_priority[5] = '/';
    stack_priority[6] = '^'; stack_priority[7] = ' ';

    while stack_priority[index_s] != stack_o:
        index_s += 1
    while infix_priority[index_i] != infix_o:
        index_i += 1
    if int(index_s/2) >= int(index_i/2):
        return  1
    else:
        return 0


def infix_to_position():
    global MAX
    global infix_q

    rear = 0
    top = 0
    i = 0
    index = -1
    stack_t = ['']*MAX   # 储存不必输出的运算符

    str_ = str('9'+'+'+'2')


    while i <len(str_):  # 将中序表达式转化为Arrey储存
        index += 1
        infix_q[index] = str_[i]
        print(infix_q[index])
        print(type(infix_q[index]))
        i += 1

    infix_q[index+1] = 'q'   #  以q符号作为队列的结束符号
    print('后序法表达式：', end='')
    stack_t[top] = 'q'

    for flag in range(index+2):
        if infix_q[flag] == ')':
            while stack_t[top] != '(':
                print('%c' %stack_t[top], end='')
                top -= 1
            top -= 1
        elif infix_q[flag] == 'q':
            while stack_t[top] != 'q':
                print('%s' %stack_t[top], end='')
                top -= 1
        elif infix_q[flag] == '+' or infix_q[flag] == '^' or \
             infix_q[flag] == '*' or infix_q[flag] == '^' or \
             infix_q[flag] == '(' or infix_q[flag] == '-':
            while compare(stack_t[top], infix_q[flag]) == 1:
                print('%c' %stack_t[top], end='')
                top -=1
            top +=1
            stack_t[top] = infix_q[flag]
        else:
            print('%c'%infix_q[flag], end='')


print('--------------------------------------------------')
print('中序表达式转换为后序表达式')
print('可以使用的运算符号符号包括：^,*,+,-,/,(,)等')
print('--------------------------------------------------')
infix_to_position()