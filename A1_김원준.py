#팀 구성원
#김원준 - 파일 입력 구현,주석 작성
#장호성 - 매트릭스 클래스 구현
#최영준 - 연산 반복문 구현
#이영빈 - 전체 반복, 종료문 구현
#안강준 - 결과값 출력 구현


#입력파일 r 모드로 오픈
f = open("input.txt", 'r')
#줄 단위로 분리
lines = f.readlines()
f.close()


#출력파일 w 모드로 오픈
f = open("output.txt", 'w')

#줄 구별하기 위한 전역변수
cursor = 0

#Matrix 클래스
class Matrix:
    #생성자 (이름, 행.열 수) 입력받고, 행렬 배열 생성 
    def __init__(self, name, row, col):
        self.name = name
        self.row = row
        self.col = col
        self.data = []
    
    #행렬 배열 _data 값으로 초기화
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
            #줄 단어 단위로 분리
            line =lines[cursor].strip().split()
            for j in range(self.col):
                _data = int(line[j])
                _col.append(_data)

            self.data.append(_col)
            cursor += 1

# 더하기 연산
def add(A, B):
    #합산을 위한 변수
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
    #매트릭스 개수 입력
    matrixNum = int(lines[cursor].strip().split()[2])
    #매트릭스 배열 변수
    matrices = []
    cursor += 2

    #반복하면서 데이터 입력
    for _ in range(matrixNum):
        #단어 단위로 분리
        line = lines[cursor].strip().split()
        #매트릭스 이름, 행, 열 수 입력
        matrix = Matrix(line[0], int(line[1]), int(line[2]))

        cursor += 1
        #매트릭스 데이터 입력
        matrix.inputData(cursor)
        #매트릭스 배열에 추가
        matrices.append(matrix)
        cursor += 4

    #결과 매트릭스 변수
    Results = []
    #연산자 입력횟수 입력
    operatorNum = int(lines[cursor].strip().split()[2])
    cursor += 2

    #반복하면서 연산
    for _ in range(operatorNum):
        line = lines[cursor].strip().split()
        
        #합 연산일 경우
        if line[0] == "Add":

            #첫 두 매트릭스 탐색
            for i in range(matrixNum):
                if matrices[i].name == line[2] :
                    A = matrices[i]

                elif matrices[i].name == line[3] :
                    B = matrices[i]

            #첫 두 매트릭스만 먼저 합산
            result = add(A, B)

            #추가적으로 합산하는 메트릭스가 있는 경우
            for i in range(int(line[1]) - 2):
                #탐색
                for j in range(matrixNum):
                    if matrices[j].name == line[4 + i] :
                        C = matrices[j]

                #추가 합산
                result = add(result, C)
            
            #이후 출력을 위해 매트릭스 이름에 현재 커서값 입력
            result.name = cursor
            #결과값 배열에 추가
            Results.append(result)

        #곱 연산일 경우
        elif line[0] == "Mul":
            #첫 두 매트릭스 탐색
            for i in range(matrixNum):
                if matrices[i].name == line[2] :
                    A = matrices[i]

                elif matrices[i].name == line[3] :
                    B = matrices[i]

            #첫 두 매트릭스만 곱
            result = mul(A, B)

            #추가적으로 곱하는 매트릭스가 있을 경우
            for i in range(int(line[1]) - 2):
                #탐색
                for j in range(matrixNum):
                    if matrices[j].name == line[4 + i] :
                        C = matrices[j]

                #추가 곱 연산
                result = mul(result, C)
            
            result.name = cursor
            Results.append(result)
        
        #Trace 연산일 경우
        elif line[0] == "Trace":
            #탐색
            for i in range(matrixNum):
                if matrices[i].name == line[1] :
                    A = matrices[i]
            
            #Trace 연산
            result = tr(A)

            result.name = cursor
            Results.append(result)

        cursor += 1


    #출력
    for i in Results:
        #매트릭스 이름 변수에 입력되어 있는 cursor 값을 이용해 해당 라인 입력
        line = lines[int(i.name)].strip().split()
        # 연산 종류 출력
        f.write(line[0])
        
        #합,곱 연산일 경우 해당 매트릭스 이름 출력
        if(line[0] != "Trace"):
            for j in range(int(line[1])):
                f.write(" ")
                f.write(line[2 + j])     
            f.write("\n")

        #Trace 연산일 경우 해당 매트릭스 이름 출력
        else:
            f.write(" ")
            f.write(line[1])
            f.write("\n")

        #결과값 출력
        for j in range(i.row):
            for k in range(i.col):
                f.write(str(i.data[j][k]))
                f.write(" ")
            f.write("\n")

        f.write("\n")

    #다음 출력문과 분리
    f.write("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n")
    f.write("\n")
    
    #end 판별위한 반복
    key = 0
    while(True):
        line = lines[cursor].strip().split()
        #end 판별 후 break
        if len(line) != 0 and line[0] == "end":
            key = 1
            break
        #다음 입력값이 있을 경우 cursor 조정
        elif len(line) != 0 and line[0] == 'Matrix':
            break
        else:
            cursor = cursor + 1
    
    #end 입력되었을 경우 전체 while문 종료
    if(key):
        break

#파일 닫기
f.close()