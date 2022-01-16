import numpy as np

# LU 분해(pivoting 추가)
# 결과는 mat 그 자체에 덮어 쓰고 반환값으로 pivot table(벡터 p)를 돌려준다.
#
# 결과는,
# A' = L U (A'는 A의 행을 바꾼 것, L는 상삼각, U는 하삼각)인 분해.
# A'의  i번째 행은 원래 행렬 A의 p[i]번째 행.
# p_ref(mat, i, j, p)으로, L (i>j) 또는 U (i<=j)인 i,j 성분이 구해진다.
def plu_decomp(mat):
  rows, cols = np.shape(mat)
  # pivot table을 준비하여,
  # pivot 된 행렬의 각 행이 원래 행렬의 모든 행에 대응하고 있는지를 기록한다.
  # mat [i, j]에 직접 접근은 피하고 반드시 함수 p_ref (값 참조) p_set (값 변경)를 통해 lu_decomp 코드를 유용 할 수 있다.
  # "pivot 된 행렬"에 접속하여,
  # lu_decomp의 코드를 준비할 수 있다.
  p = np.array(rows)
  for i in range(1,rows):
    p[i] = i  # pivot table의 초기화. 초기값은 "i행은 i"
  # 행 수(rows)와 열 수(cols)에서 짧은 쪽을 s로 둔다.
  if (rows < cols):
    s = rows
  else:
    s = cols

  # 여기부터가 핵심
  for k in range(1,s):
    # 먼저 pivoting을 해두고
    p_update(mat, k, rows, p)
    # 여기서부터는, lu_decomp을 이렇게 대체하면
    #   mat[i,j] → p_ref(mat, i, j, p)
    #   mat[i,j] = y → p_set(mat, i, j, p, y)
    # 【아】 U의 제 k 행은, 이 단계에서 잔차 자체 → 아무것도 하지 않아도 된다
    # 【이】 L의 제 k 행을 계산
    x = 1.0 / p_ref(mat, k, k, p)
    for i in range((k+1),rows):
      y = p_ref(mat, i, k, p) * x
      p_set(mat, i, k, p, y)

    # 【우】 잔차를 갱신
    for i in range((k+1),rows):
      x = p_ref(mat, i, k, p)
      for j in range((k+1),cols):
        y = p_ref(mat, i, j, p) - x * p_ref(mat, k, j, p)
        p_set(mat, i, j, p, y)
  # pivot table를 반환값으로 한다
  return(p)


# pivoting을 시행한다.
# 구체적으로는 k 열 번째 처리되지 않은 부분 중 절대값이 가장 큰 성분을 k 번째 줄로 가져온다.
def p_update(mat, k, rows, p):
  # 후보 (k번째 열의 미처리 부분) 중에서 챔피언(절대 값이 가장 큰 성분)을 찾는다.
  max_val = -777  # 최약의 초대 챔피언. 누구한테도 진다.
  max_index = 0
  for i in range(k,rows):
    x = abs(p_ref(mat, i, k, p))
    if (x > max_val):  # 챔피언을 쓰러 뜨리면
      max_val = x
      max_index = i
  # 현재 행 (k)와 챔피언 행 (max_index)를 교체
  pk = p[k]
  p[k] = p[max_index]
  p[max_index] = pk

# pivot된 행렬의 (i,j) 성분값을 돌려준다.
def p_ref(mat, i, j, p):
  return(mat[p[i], j])

# pivoting된 행렬의 (i,j) 성분값을 val로 변경
def p_set(mat, i, j, p, val):
  mat[p[i], j] = val