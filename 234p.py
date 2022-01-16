import numpy as np

#LU분해 (피보팅없음)
# 결과는 mat 자신에 기록(왼쪽 아래 부분이L, 오른쪽 위 부분이 U)
def lu_decomp(mat):
  rows, cols = np.shape(mat)
# 행과 열 중 짧은쪽을 s 로 둔다
  if (rows < cols):
    s = rows
  else:
    s = cols

  for k in range(1,s):
    x = 1.0/mat[k,k]
    for i in range((k+1),rows):
      mat[i,k] = mat[i,k]* x
    for i in range((k+1),rows):
      for j in range((k+1),cols):
        mat[i,j] = mat[i,j] - mat[i,k] * mat[k,j]