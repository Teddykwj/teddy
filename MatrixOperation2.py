#파일 입력
f = open("input.txt", 'r')
#줄 단위로 분리
lines = f.readlines()

f.close()

f = open("output.txt", 'w')

#줄 구별하기 위한 변수
cursor = -1

#Matrix 클래스
class Matrix:
    def __init__(self, name, row, col):
        self.name = name
        self.row = row
        self.col = col
        self.data = []
    
    #행렬 데이터 초기화
    def initData(self, _data):
        for i in range(self.row):
            _col = []
            for j in range(self.col):
                _col.append(_data)

            self.data.append(_col)

    #파일에 있는 데이터 값 입력
    def inputData(self, cursor):
        for i in range(self.row):
            _col = []
            line =lines[cursor].strip().split()
            for j in range(self.col):
                _data = int(line[j])
                _col.append(_data)

            self.data.append(_col)
            cursor += 1

# 더하기 연산
def add(A, B):
    _sum = Matrix(0, A.row, A.col)
    _sum.initData(0)

    for i in range(A.row):
        for j in range(A.col):
            _sum.data[i][j] = A.data[i][j] + B.data[i][j]
    
    return _sum

# 곱하기 연산
def mul(A, B):
    _result = Matrix(0, A.row, B.col)
    _result.initData(0)

    for i in range(A.row):
        for j in range(B.col):
            for k in range(B.row):
                _result.data[i][j] += A.data[i][k] * B.data[k][j]

    return _result

# trace 연산
def tr(A):
    _result = Matrix(0,1,1)
    _result.initData(0)

    for i in range(A.row):
        _result.data[0][0] += A.data[i][i]

    return _result

#행렬 입력횟수
while(True):
    while(True):
        line = lines[cursor].strip().split()
        cursor += 1
        if len(line) != 0:
            if line[0] == "Matrix":
                break
    
    matrixNum = int(line[2])
    matrices = []
    cursor += 2

    #반복하면서 데이터 입력
    for _ in range(matrixNum):
        line = lines[cursor].strip().split()
        matrix = Matrix(line[0], int(line[1]), int(line[2]))

        cursor += 1
        matrix.inputData(cursor)

        matrices.append(matrix)
        cursor += 4

    #연산자 입력횟수
    Results = []
    operatorNum = int(lines[cursor].strip().split()[2])
    cursor += 2

    #반복하면서 연산
    for _ in range(operatorNum):
        line = lines[cursor].strip().split()
        
        if line[0] == "Add":
            for i in range(matrixNum):
                if matrices[i].name == line[2] :
                    A = matrices[i]

                elif matrices[i].name == line[3] :
                    B = matrices[i]

            result = add(A, B)

            for i in range(int(line[1]) - 2):
                for j in range(matrixNum):
                    if matrices[j].name == line[4 + i] :
                        C = matrices[j]

                result = add(result, C)
            
            result.name = cursor
            Results.append(result)


        elif line[0] == "Mul":
            for i in range(matrixNum):
                if matrices[i].name == line[2] :
                    A = matrices[i]

                elif matrices[i].name == line[3] :
                    B = matrices[i]

            result = mul(A, B)

            for i in range(int(line[1]) - 2):
                for j in range(matrixNum):
                    if matrices[j].name == line[4 + i] :
                        C = matrices[j]

                result = mul(result, C)
            
            result.name = cursor
            Results.append(result)
        
        elif line[0] == "Trace":
            for i in range(matrixNum):
                if matrices[i].name == line[1] :
                    A = matrices[i]

            result = tr(A)

            result.name = cursor
            Results.append(result)

        cursor += 1


    #출력
    for i in Results:
        line = lines[int(i.name)].strip().split()
        f.write(line[0])
        
        if(line[0] != "Trace"):
            for j in range(int(line[1])):
                f.write(" ")
                f.write(line[2 + j])     
            f.write("\n")

        else:
            f.write(" ")
            f.write(line[1])
            f.write("\n")

        for j in range(i.row):
            for k in range(i.col):
                f.write(str(i.data[j][k]))
                f.write(" ")
            f.write("\n")

        f.write("\n")

    line = lines[cursor].strip().split()

    if len(line) != 0:
        if line[0] == "end":
            break

f.close()