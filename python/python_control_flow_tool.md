1. for , while 구문 사용시 else 사용 가능
  - if, else의 활용이 아니라 다른 방식으로도 활용 가능함
    - try except의 except와 비슷함(?)
  ```py
  for dust in range(2):
        for number in range(10):
            if number * dust < 10:
                print('아직 작다.')
                break
  else:                 # 아직 작다. 아직 작다. 앤 5
      print('얜 5')   
  ```
  - break 가 있을 경우에는 출력이 되지 않는다.
  - 없을 경우 위 조건을 모두 만족한 것을 출력한 후, 출력됨
    - break가 걸렸는지 안 걸렸는지를 확인을 위한 활용 