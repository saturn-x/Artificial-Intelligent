import numpy as np
class State:
    # state（矩阵的数字）
    # directionflag（矩阵取去除的方向，即移动方向的反方向）
    # parent（上一个矩阵）
    def __init__(self,digital_matrix,directionflag=None,parent=None):
        self.digital_matrix=digital_matrix
        self.all_directions=["L","U","D","R"]# 左右上下
        if directionflag:
            self.all_directions.remove(directionflag)
        #设置双亲节点
        self.parent=parent
        #设置空位为0
        self.symbol=0
    #打印矩阵；无返回值
    def showMatrix(self):
        for i in self.digital_matrix:
            for j in i:
                print(j,'',end="")
            print("\n",end="")
        return
    #返回矩阵的方向
    def getDirection(self):
        return self.all_directions
    #生成该矩阵空点的位置；返回矩阵空点的行，列
    def getEmptyPos(self):
        postition=np.where(self.symbol==self.digital_matrix)
        return postition
    #根据存储的方向生成子状态矩阵，返回生成的矩阵
    def generateSubmatrix(self):
        SubState=[]
        row,col=self.getEmptyPos()
        cur_direction=self.getDirection()
        # print(cur_direction) 根据方向，模拟将该数字的移动
        for i in cur_direction:
            #往左移动需要判断是否已经是在第一列
            sub_state=None
            if i=='L'and col>0:
                tmp_target_digital=self.digital_matrix[row,col-1]
                tmp_matrix=self.digital_matrix.copy()
                tmp_matrix[row,col]=tmp_target_digital
                tmp_matrix[row,col-1]=0
                sub_state=State(tmp_matrix,directionflag='R',parent=self)
            elif i=='U'and row>0:
                tmp_target_digital=self.digital_matrix[row-1,col]
                tmp_matrix=self.digital_matrix.copy()
                tmp_matrix[row,col]=tmp_target_digital
                tmp_matrix[row-1,col]=0
                sub_state=State(tmp_matrix,directionflag='D',parent=self)
            elif i=='R'and col<self.scale-1:
                tmp_target_digital=self.digital_matrix[row,col+1]
                tmp_matrix=self.digital_matrix.copy()
                tmp_matrix[row,col]=tmp_target_digital
                tmp_matrix[row,col+1]=0
                sub_state=State(tmp_matrix,directionflag='L',parent=self)
            elif i=='D'and row<self.scale-1:
                tmp_target_digital=self.digital_matrix[row+1,col]
                tmp_matrix=self.digital_matrix.copy()
                tmp_matrix[row,col]=tmp_target_digital
                tmp_matrix[row+1,col]=0
                sub_state=State(tmp_matrix,directionflag='U',parent=self)
            if sub_state:
                # print(i)
                # sub_state.showMatrix()
                SubState.append(sub_state)
        return SubState





def String_to_Array(String,Scale):
    left=0
    matrix=[]
    for i in range(Scale):
        row=[]
        nums=String[left:left+Scale]
        for i in nums:
            #print(i)
            row.append(i)
        left+=Scale
        row = list(map(int, row))
        matrix.append(row)
    #print(matrix)

    return matrix
def Array_to_String(Array):
    res=''
    for i in Array:
        for j in i:
            res=res+(str(j))
    return res

def Is_Solve(BeginState,AnsState,Scale):
    res=0
    res2=0
    for i in range(1,Scale*Scale):
        for j in range(0,i):
            if BeginState[j]>BeginState[i] and BeginState[i]!='0':
                res+=1
    for i in range(1,Scale*Scale):
        for j in range(0,i):
            if AnsState[j]>AnsState[i] and AnsState[i]!='0':
                res2+=1
    #print(res,res2)
    if (res % 2) != (res2 % 2):  # 一个奇数一个偶数，不可达
        return False
    return True


