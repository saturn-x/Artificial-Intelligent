#使用在广度优先使用启发式搜索
#启发函数设置的是判断是否在位
from Lab01.State import State, Is_Solve, String_to_Array, Array_to_String
import numpy as np
#启发函数1
def ret_value(SubState,Ans_State):
    #该函数返回启发式值
    values=[]
    #将两个二维矩阵转为字符串，直接比较字符串
    ans=Array_to_String(Ans_State.digital_matrix)
    for i in SubState:
        value=0
        tmp=Array_to_String(i.digital_matrix)
        for j in range(0,len(tmp)):
            if(ans[j]!=tmp[j]):
                value+=1
        values.append(value)
    return values
#启发函数2

def Solution(State,Ans_State):
    Activity_State=[]
    Activity_State_depth=[]
    Activity_State_Values=[]
    #初始进去的节点
    Activity_State.append(State)
    Activity_State_depth.append(0)
    Activity_State_Values.extend(ret_value(Activity_State,Ans_State))
    Not_Activity=[]
    step=0
    while len(Activity_State)>0:
        #选择最小的节点
        if len(Activity_State)==1:
            Cur_index=0
        else:
            tmp_value=[]
            for i in range(0,len(Activity_State)):
                #计算深度+启发式函数和
                tmp_value.append(Activity_State_depth[i]+Activity_State_Values[i])
            Cur_index=tmp_value.index(min(tmp_value))
        Cur_State=Activity_State[Cur_index]
        Cur_State_depth=Activity_State_depth[Cur_index]
        path=[]
        #生成自己子节点存入子序列中
        step+=1
        Sub_State=Cur_State.generateSubmatrix()
        # 深度+1
        Cur_State_depth+=1
        Sub_State_depth = []
        for i in range(len(Sub_State)):
            Sub_State_depth.append(Cur_State_depth)
        for i in Sub_State:
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
        #没找到子节点，需要将子节点全部加入队列中
        Activity_State.extend(Sub_State)
        Activity_State_depth.extend(Sub_State_depth)
        Activity_State_Values.extend(ret_value(Sub_State,Ans_State))
        Not_Activity.append(Activity_State.pop(Cur_index))
        Activity_State_depth.pop(Cur_index)
        Activity_State_Values.pop(Cur_index)
    print("无解！")
    return None

if __name__ == '__main__':
    print("启发式···")
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





