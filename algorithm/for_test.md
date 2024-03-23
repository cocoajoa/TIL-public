# 쓸만한 것들 다 집어넣기
## 함수
### collections 
1. deque() : 스택할 떄 쓰는 유용한 함수
   1. popleft() : 맨 앞 값 빼서 반환, pop(0)보다 훨씬 좋음 

2. Counter() : 리스트나 str과 같은 iterable한 애들 내 원소들 개수를 세서 counter class내 dictionary 형태로 저장
   1. most_common(n) : 가장 많은 순서부터 tuple 형태로 (어떤 원소가, 몇 번 나왔는지) 나옴. n만큼 나오니 젤 큰것만 보려면 n을 1로 

3. defaultdict() : dictionary에 값이 없는 것들에 대해 처음에 일일이 다 원하는 키 = 원하는 value 처리 안해도됨 
   1. (str) or (int) : += str or int로 원하는 키에 value를 계속 문자열을 추가 혹은 덧셈이 가능함
   2. (list) : .append(원하는 값) 으로 원하는 키에 list 형태로 값 보관 가능,<br> 예) {'wanted': ['first', 'second']}

### itertools
1. accumulate([a, b, c, ...]) : 숫자 계속 더한 값 출력, 어딘가 쓸일 있을지도
   - 결과 : a, a+b, a+b+c, ....
2. product(쓸 자료, repeat= 순열 길이) : 중복 가능한 순열
3. permutation(쓸 자료, 순열 길이) : 중복 안되는 순열 
4. combination(쓸 자료, 순열 길이) : 조합
5. combinations_with_replacement(쓸 자료, 순열 길이) : 중복 조합

### math

### sys
1. sys.stadin: input 받을 때 씀
   1. sys.stadin.read ... etc: 한번에 받거나 따로따로 받을때
   2. input = sys.stadin.readline : input 쓰는 것과 동일하게 사용가능
      1. input.strip() : 문자열 받을때 쓰는 방법


## 알고리즘

1. BFS:
   ```python
   from collections import deque

   def bfs(start):
      visited = [0] * length         # 방문 여부 표시할 배열 혹은 리스트
      stack = deque()                # bfs를 시행시 사용할 스택
      stack.append([start, memo])    # 시작지점 stack에 넣기 / memoization을 사용이 필요한 경우 리스트로 감싸서 메모할 것 같이 넣기, 간단한 거면 visited에 넣기
      visited[start] = 1             # 첫 시작은 방문했으니 넣기
      while stack:
         point, new_memo = stack.popleft()  # BFS는 선입선출 구조로 진행한다.
         new_point = point + direction      # 방향에 맞게 이동할 위치 설정
         if visited[new_point]: continue    # 이미 방문했던 위치라면 패스
         visited[new_point] = 1 or visited[point] + value # 방문 표시만 할꺼면 1, 이전 값에서 현재 값을 더할거면 후자처럼
         new_memo += value                  # 메모이제이션 할 것 수정
         stack.append([new_point, new_memo])# 방문한 곳 스택에 넣기

      return visited                # 원하는 위치나 값 반환  
   ```

3. 이분탐색:
   ```python
   want_value = 100
   start = 0
   end = int(1e9)
   while True:
      mid = (start + end) // 2
      if mid == want_value:
         break
      elif mid > want_value:
         end = mid
      elif mid < want_value:
         start = mid
   ```