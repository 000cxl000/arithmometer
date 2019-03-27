from fractions import Fraction
import random

class Ari_Expression():
    '''算术表达式的生成'''
    def __init__(self, max_num):
        '''生成运算符'''
        self.init_operators()
        '''生成随机数字'''
        self.init_nums(max_num)
        '''生成表达式'''
        self.init_expression()
        
    def init_num(self, max_num):
        '''随机生成数'''
        denominator = random.randint(1, max_num)#分母
        numerator = random.randint(0, max_num)#分子
        return Fraction(numerator, denominator)#通过Fraction类产生一个分数

    
    def insert_bracket(self):
        '''插入括号'''
        bracket = ['(', ')']
        n=len(self.operators)
        if n > 1:
            x = random.randint(0, n-2)
            while x < n-2:
                y = random.randint(x, n-2)
                low=False
                for a in self.operators[x:y+1]:
                     if a in ['+', '-']:
                         low = True
                         break
                if self.operators[y] in ['×', '÷'] and low:
                    self.operators.insert(x, '(')
                    self.operators.insert(y+2,')')
                x = y+2
                
    def init_operators(self):
        '''随机生成一个运算符并随机插入括号'''
        self.operators = []
        operator = ['+', '-', '×', '÷']
        for x in range(5):
            if x == 1:
                self.operators.append(random.choice(operator[:-2]))
            else:
                y = random.choice(operator)
                if y != 'null':
                    self.operators.append(y)
        self.insert_bracket()
    
    def init_nums(self, max_num):
        self.nums = []
        self.nums.append(self.init_num(max_num))
        for x in range(len(self.operators)):
            y = self.init_num(max_num)
            if self.operators[x] == '÷':
                while y.numerator == 0:
                    y = self.init_num(max_num)
            self.nums.append(y)
    
    def str_num(self, num):
        '''字符串化一个分数'''
        inter = int(num.numerator / num.denominator)
        numerator = int(num.numerator % num.denominator)
        if numerator == 0:
            '''如果为空'''
            str_num = str(inter)
        else:
            str_num = str(num.numerator) + '/' + str(num.denominator)
        return str_num
    
    def init_expression(self):
        '''生成一个算术表达式的字符串形式'''
        self.str = ''
        i = 0
        self.exp = []
        again = False
        for x in self.operators:
            if again:
                self.str += x + ' '
            elif x == '(':
                self.str += x + ' '
            elif x == ')':
                self.str += self.str_num(self.nums[i]) + ' '
                i += 1
                self.str += x + ' '
                again = True
            else:
                self.str += self.str_num(self.nums[i]) + ' '
                self.str += x + ' '
                i += 1
        self.str += self.str_num(self.nums[-1]) + ' ='
