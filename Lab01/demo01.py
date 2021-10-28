
import numpy as np
from Lab01.State import State, String_to_Array,Is_Solve


#实现了广度优先搜索

def Solution(State,Ans_State):
    Activity_State = []
    Activity_State.append(State)
    Not_Activity=[]
    step=1
    while len(Activity_State)>0:
        #执行
        Sub_State=Activity_State[0].generateSubmatrix()
        step+=1
        path=[]
        # print("步数:",step)
        # print("矩阵个数", len(Activity_State))
        for i in Sub_State:
            #i.showMatrix()
            if(i.digital_matrix==Ans_State.digital_matrix).all():
                print("找到了！····")
                print("步数:",step)
                print("生成的节点数", len(Activity_State) + len(Not_Activity))
                i.showMatrix()
                path.append(i)
                while i.parent!=None:
                    path.append(i.parent)
                    i=i.parent
                path.reverse()
                return path
        Activity_State.extend(Sub_State)
        Not_Activity.append(Activity_State.pop(0))
    print("无解！")
    return None

if __name__ == '__main__':
    print("使用广度优先搜索···")
    State.scale=3
    Symbol_Empty=0
    beginState="283104765"
    ansState="123804765"
    if Is_Solve(beginState,ansState,State.scale):
        print("可以找到答案")
    else:
        print("不可以找到答案")
    beginState=String_to_Array(beginState, State.scale)
    ansState=String_to_Array(ansState,State.scale)


    beginState=State(np.array(beginState))
    ansState=State(np.array(ansState))
    path=Solution(beginState,ansState)
    if path:
        print("打印路径如下")
        for i in path:
            print("第", path.index(i), "层")
            i.showMatrix()





