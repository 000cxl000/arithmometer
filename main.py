from ariExpression import Ari_Expression
from infixTosuffix import infix_to_suffix
import Calculate
import profile

def main():
    max_num=10
    problem = int(input('请输入需要的题目数量：'))
    i = 1
    correct =0
    wrong =0
    print("本次测试共{}题，满分100分".format(problem))
    while i < problem + 1:
        ari = Ari_Expression(max_num)
        inf = infix_to_suffix()
        real_res = Calculate.getResult(inf.str_to_fraction(inf.to_suffix_expression(ari.str)))
        if real_res >= 0:
            print("------------------------------")
            real_res = ari.str_num(real_res)
            print(str(i)+'. ' + ari.str, end = '')
            res = input()
            if res == real_res:
                correct += 1
                print("回答正确！")
            else:
                wrong += 1
                print("回答错误！正确答案为：{}".format(real_res))
            i += 1
    print('\n得分为：' + str(correct/problem*100))

if __name__ == '__main__':
    profile.run("main()")
