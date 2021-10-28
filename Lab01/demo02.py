#使用深度优先搜索

import numpy as np
from Lab01.State import State, String_to_Array, Is_Solve


def Solution(State, Ans_State, depths=None):
    Activity_State=[]
    Activity_State_depth=[]
    Activity_State.append(State)
    Activity_State_depth.append(0)
    Not_Activity = []
    path=[]
    while len(Activity_State) >0:
        step=0
        depth = Activity_State_depth[len(Activity_State)-1]
        while(depth<=5):
            #最后一个元素生成子节点
            last=len(Activity_State)-1
            if last==-1:
                break
            Sub_State=Activity_State[last].generateSubmatrix()
            step+=1
            depth+=1
            Sub_State_depth=[]
            for i in range(len(Sub_State)):
                Sub_State_depth.append(depth)
            #深度+1
            for j in Sub_State:
                if (j.digital_matrix == Ans_State.digital_matrix).all():
                    print("找到了！此时的深度：",depth,"步数：",step)
                    path.append(j)
                    while j.parent != None:
                        path.append(j.parent)
                        j = j.parent
                    path.reverse()
                    return path
            Not_Activity.append(Activity_State.pop(last))
            Activity_State_depth.pop(last)
            if(depth<5):
                Sub_State.reverse()
                Activity_State.extend(Sub_State)
                Activity_State_depth.extend(Sub_State_depth)
            else:
                #此时的深度已经到底了，需要重新设置depth
                if len(Activity_State)-1>=0:
                    depth = Activity_State_depth[len(Activity_State)-1]
    print("深度为5无解")
        
    



if __name__ == '__main__':
    print("使用深度优先搜索")
    State.scale = 3
    Symbol_Empty = 0
    beginState = "283164705"
    ansState = "123804765"
    if Is_Solve(beginState, ansState, State.scale):
        print("可以找到答案")
    else:
        print("不可以找到答案")
    beginState = String_to_Array(beginState, State.scale)
    ansState = String_to_Array(ansState, State.scale)

    beginState = State(np.array(beginState))
    ansState = State(np.array(ansState))
    path = Solution(beginState, ansState)
    if path:
        print("打印路径如下：")
        for i in path:
            print("第",path.index(i),"层")
            i.showMatrix()











