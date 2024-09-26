import math


# 파일 읽기
inputFile = open("input.txt", "r") # 읽기 모드
# 줄 단위로 분리
lines = inputFile.readlines()


# 파일로부터 Matrix 정보를 가져와 반환하는 함수
def makeMatrix(lines):
    # 줄 구별 변수
    cursor = 0
    # print(lines)

    # Matrix 정보 가져오기 (딕셔너리 사용 / 이름, 값)
    matrixNum = int(lines[cursor][-2]) # Matrix 수: n 
    cursor = 2 # Maxtrix 정보 시작 줄로 이동

    Matrix = {} # 각 행렬을 담는 배열 Matrix
    for N in range(matrixNum):
        eachMatrixInfo = lines[cursor].strip().split() # 각 Matrix 정보 배열 ex) A 3 3
        name = eachMatrixInfo[0] # 행렬 이름
        row = int(eachMatrixInfo[1]) # 행
        col = int(eachMatrixInfo[2]) # 열

        cursor = cursor + 1

        eachMatrix = []
        for i in range(row):
            eachMcol = []
            l = lines[cursor].strip().split()
            
            for j in l:
                eachMcol.append(int(j))
            
            eachMatrix.append(eachMcol)
            cursor = cursor + 1
        # print(eachMatrix)
        cursor = cursor + 1
        Matrix[name] = eachMatrix  
    
    return Matrix, cursor

# 연산 정보를 가져오는 함수
def CAL(M, c):
    # 줄 구별 변수
    cursor = c
    
    # 연산 정보 가져오기
    calNum = int(lines[cursor][-2]) # calNum 수: n 
    cursor = cursor + 2 # Maxtrix 정보 시작 줄로 이동

    cal = [] # 각 행렬을 담는 배열 Matrix
    for N in range(calNum):
        cal.append(lines[cursor].strip().split())
        cursor = cursor + 1

    return cal
        
M, c = makeMatrix(lines)
C = CAL(M, c)
# C[-1][-1] = C[-1][-1][0] # ??

print(C)

# def ADD(A, B):
