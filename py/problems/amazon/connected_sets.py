matrices = [[raw_input().split(' ') for i in range(int(raw_input()))] for j in range(int(raw_input()))]
def toggle(matrix,i,j,n):
    q={(i,j)}
    while q:
        i,j = q.pop()
        matrix[i][j]=0
        for k in range(max(0,i-1),min(n,i+2)):
            for l in range(max(0,j-1),min(n,j+2)):
                if matrix[k][l]=='1':
                    q.add((k,l))
                
for matrix in matrices:
    n = len(matrix)
    cnt = 0
    for i in range(n):
        for j in range(n):
           if matrix[i][j]=='1':
                cnt += 1
                toggle(matrix,i,j,n)
    print cnt