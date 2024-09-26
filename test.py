f = open("input.txt", 'r', encoding='UTF8')
line = f.readline()
matrix_num = int(line[len(line)-2])
matrix = {}
f.readline()
line = f.readline()
for i in range(matrix_num):
    matrix_name = line.split()[0]
    matrix[matrix_name] = []
    for j in range(int(line.split()[1])):
        line = f.readline()
        matrix[matrix_name].append(line.split())
    f.readline()
    line = f.readline()

calculation_num = int(line[-2])
f.readline()

w = open("output.txt", 'w')

for i in range(calculation_num):
    line = f.readline()
    
    if(line.split()[0] == 'Add'):
        w.write(line.split()[0] + ' ')
    
        tmp_matrix = [[0 for _ in range(len(matrix[line.split()[2]][0]))] for _ in range(len(matrix[line.split()[2]]))]
        for i in range(int(line.split()[1])):
            w.write(line.split()[2+i] + ' ')
            for j in range(len(matrix[line.split()[2+i]])):             
                for k in range(len(matrix[line.split()[2+i]][0])):
                    tmp_matrix[j][k] += int(matrix[line.split()[2+i]][j][k])
        w.write('\n')
        for i in range(len(tmp_matrix)):
            for j in range(len(tmp_matrix[0])):
                w.write(str(tmp_matrix[i][j]) + ' ')
            w.write('\n')
        w.write('\n')

    elif(line.split()[0] == 'Mul'):
        w.write(line.split()[0] + ' ')

        result_matrix = matrix[line.split()[2]]
        w.write(line.split()[2] + ' ')
        for mat_idx in range(3, int(line.split()[1])+2):
            next_matrix = matrix[line.split()[mat_idx]]
            w.write(line.split()[mat_idx] + ' ')

            rows_result = len(result_matrix)
            cols_result = len(next_matrix[0])
            cols_first = len(result_matrix[0])
            
            tmp_matrix = [[0 for _ in range(cols_result)] for _ in range(rows_result)]
            
            for i in range(rows_result):
                for j in range(cols_result):
                    for k in range(cols_first):
                        tmp_matrix[i][j] += int(result_matrix[i][k]) * int(next_matrix[k][j])
                        
            result_matrix = tmp_matrix        
        w.write('\n')
        for i in range(len(result_matrix)):
            for j in range(len(result_matrix[0])):
                w.write(str(result_matrix[i][j]) + ' ')
            w.write('\n')
        w.write('\n')

    elif(line.split()[0] == 'Trace'):
        w.write(line.split()[0] + ' ' +  line.split()[1] + '\n')
        sum = 0
        result_matrix = matrix[line.split()[1]]
        for i in range(len(result_matrix)):
            sum += int(result_matrix[i][i])
        w.write(str(sum) + '\n')
        w.write('\n')
