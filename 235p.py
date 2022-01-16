import numpy as np

#행렬식(원래 행렬은 없어진다)
def det(mat):
  rows, cols = np.shape(mat)
  if (rows != cols):
    raise 'Not square!' #에러발생
  

#여기서부터 중심내용
lu_decomp(mat)
# U의 대각성분의 곱을 답한다.
  x=1
  for i in range(1,rows):
    x = x*mat[i,i]
return x