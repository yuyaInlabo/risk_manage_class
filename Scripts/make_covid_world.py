# author yuya
import math
import random


# 感染している場合はtrue, そうでない場合はfalseを吐く、感染している割合は0.0009(0.09%で固定とした)
def InfectedOrNo(infection_rate = 0.0009):
    if(random.random() < infection_rate):
        return True
    else:
        return False

# 感染している人が陽性と判断される場合true, そうでない場合はfalseをはく
def InfectedJudgePositive(judge_rate = 0.95):
    if(random.random() < judge_rate):
        return True
    else:
        return False

# 感染していない人が陰性と判断される場合true, そうでない場合false
def NoninfectedJudgeNegative(judge_rate = 0.8):
    if(random.random() < judge_rate):
        return True
    else:
        return False


# 標本抽出数
nums = 100000
# 感染していて陽性と判断された人数
infected_positive_num = 0
# 感染しているのに陰性と判断された人数
infected_negative_num = 0
# 感染していなくて陰性と判断される人数
noninfected_negative_num = 0
# 感染していないのに陽性と判断される人数
noninfected_positive_num = 0
for i in range(nums):
    infected = InfectedOrNo()
    # 感染している人に陽性と出るかのチェックを行う。
    if(infected):
        positive_check = InfectedJudgePositive()
        # 感染していてかつ陽性と正しく判断された場合
        if(positive_check):
            infected_positive_num += 1
        # 感染しているのにもかかわらず陰性と判断された場合
        else:
            infected_negative_num += 1
    # 感染していない場合
    else:
        negative_check = NoninfectedJudgeNegative()
        # 感染していない人が陰性と判断される場合
        if(negative_check):
            noninfected_negative_num += 1
        # 感染していない人が陽性と判断される場合
        else:
            noninfected_positive_num += 1

# 陽性と判断された人の合計
positive_judged_num = infected_positive_num + noninfected_positive_num
# 陽性者が実際に感染している割合
positive_infected_rate = infected_positive_num / positive_judged_num


print("陽性者が実際に感染している確率は " + str(round(positive_infected_rate*100, 2)) + "% です")