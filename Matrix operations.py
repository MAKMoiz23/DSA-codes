class Array:
    def __init__(self,rows,cols):
        self.rows=rows
        self.columns=cols
        self.data=[0 for i in range(1,(self.rows*self.columns+1))]

    def setLocation(self,i,j):
        l=i*self.rows+j
        return l

    def setData(self,i,j,val):
        l=self.setLocation(i,j)
        self.data[l]=val

    def getValue(self,i,j):
        l=self.setLocation(i,j)
        return self.data[l]

    def printValue(self):
        for i in range(0,self.rows):
            for j in range(0,self.columns):
                print(self.getValue(i,j),end=' ')
            print('\n')

    def subValues(self,obj_1,obj_2):
        arr=[[0] * self.rows for i in range(self.columns)]

        for row in range(self.rows):
            for col in range(self.columns):
                arr[row][col]=obj_1[self.setLocation(row,col)]-obj_2[self.setLocation(row,col)]
                print(arr[row][col], end=' ')
            print('\n')

    def MultiValues(self,obj_1,obj_2):
        arr=[[0] * self.columns for i in range(self.rows)]
        for row in range(self.rows):
            for col in range(self.columns):
                for r_c in range(self.rows):
                    arr[row][col]+=obj_1[self.setLocation(row,r_c)]*obj_2[self.setLocation(r_c,col)]
                print(arr[row][col],end=' ')
            print('\n')

    def Transpose(self):
        for row in range(self.rows):
            for col in range(self.columns):
                    print(self.data[self.setLocation(col,row)],end=' ')
            print('\n')

#  0 1 2 3 4 5 6 7 8
# [0,0,0,
#  0,0,0,
#  0,0,0]
#  0 3 6 1 4 7 2 5 8
# [0,0,0,
#  0,0,0,
#  0,0,0]

x1=Array(3,3)
x2=Array(3,3)



for i in range(x1.rows):
    for j in range(x1.columns):
        print("Enter the value at position for 1st matrix ","Row",i,"column",j," :")
        x1.setData(i,j,int(input()))

for i in range(x2.rows):
    for j in range(x2.columns):
        print("Enter the value at position for 2nd matrix ","Row",i,"column",j," :")
        x2.setData(i,j,int(input()))

x1.printValue()

print("The values of matrix x1 are :\n")
x1.printValue()
print("The values of matrix x2  are :\n")
x2.printValue()

ob1=x1.data
ob2=x2.data

print(("Multiplying x1 and x2 :"))
x1.MultiValues(ob1,ob2)

#print(("Subtracting x2 from x1 :"))
#x1.subValues(ob1,ob2)

#print("The values after the transpose of x1 matrix are :\n")
#x1.Transpose()
