# 쓸 수 있는 방식 다 넣기

## flex box
.container {
    display: flex; 
    flex-direction: row or column or -reverse;
    
    justify-content: flex-start;  # 분배 위치 설정
    
    flex-wrap: wrap;  # 한 행에 들어가지 않으면 아래로 내려갈지 말지
    align-content: flex-start;    # 여러 행 있을시 교차 축에 따라 분배 위치 설정
    alin-items: center;           # 교차 축을 따라 flex item 행을 정렬
} 

.item1 {
  align-self: flex-start;         # 교차 축을 따라 개별 flex item을 정렬
  flex-grow: 1;                   # 비율로
  flex-basis: 600px;              # px단위 절대값으로/ grow보다 더 기준이 됨
}

## 반응형 웹
1. Container
   1. row
      - row에서 gutter 조절, g-3,gx-0,gy-1
      - row나 col에서 break point 조절 가능, row-cols-sm-1
        - xs : < 576px, sm : >= 768px, md >= 768px, lg >= 992px, xl >= 1200px, xxl >=1400px 
      1. col
        - col은 영역을 12개로 나눌 수 있음
        - offset을 쓰면 빈 공간을 앞에 넣을 수 있음
  