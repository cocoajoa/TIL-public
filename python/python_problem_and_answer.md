# 2024-01-15

1. python slice 역순 거꾸로
- 실패

        문자열[-숫자:-숫자]
        -> 되긴 하는데 내가 원하는 n번째 부터 m까지의 글자를 역순으로 프린트하려면 
        글자 숫자부터 len으로 확인해서 이것 저것 해야됨.. 다른 방법을 시도해봄   


- 성공 

        문자열[큰 숫자:작은 숫자:-1]
        -> sample = 'top' 라고 정의하면 각 알파벳은 0,1,2로 인덱싱된다.
         
        [숫자a:숫자b:숫자c] 는 a번호서 부터 b미만까지 c의 간격이라는 의미
        작은 숫자를 뒤에 넣게된다면 a번호 초과 b이하의 값이 출력됨  

2. 문자열[3:-1:-1]이 안되는 이유?
- 실패 
        
        물론 [3::-1] 을 하면 첫번째 단어부터 역순으로 출력이 되나
        꼭 생략이 되어야하는 이유가 있을까?
- 성공

        생각해보면 너무나 당연한 일이다. python에서는 문자열 맨뒤에서부터 -1,-2...로 
        indexing하니까 호환이 안되는 index 간의 함수라 아무것도 출력이 되지 않는 것이겠지..

3. f'{py:.3}' 의 정체 와 사용법
- 실패?

        파이(3.14)를 소수 둘째짜리 나오게 만들고 싶어 아무거나 두드리다가 .2에서 뭔가 
        작동하길래 알게됨

- 성공?

    ```python 
      찾아보니 일반적으로는 round(원하는 숫자나 숫자변수,원하는 소수점자리)를 
      사용하는 것을 알 수 있었다.
      f-string을 배우다가 얻어걸린거라 나중에 배울것 같다.

      참고로 f'{py:.3f}'와 같이 f를 넣는게 일반적이라고 한다.
      차이점은 그냥 숫자만 넣은건 해당 자리에서 반올림 여부를 확인하는 거고 
      f를 추가하면 해당자리까지 표시할거고 나머지 뒷자리 반올림 여부를 확인한다.
      
      간단히 말하자면 
      f'{변수:.3} = f'{변수:.2f} = 
      소수점 셋째짜리에서 반올림하여 소수점 둘째자리까지 표시 
      ```


4. 아래 코드 좀더 깔끔하게 만드는 법 노가다 말고..

    ```python 
    string = '문자'
    integer = 5
    floating_point = 3.14
    a_list = [1, 2, 3, 4, 5]
    dictionary = {'name': 'jang', 'age': 20}
    a_set = {1, 2, 3, 4, 5}
    a_range = range(15)
    a_tuple = (1, 2, 3, 4)
    boolean = True


    print(f'{type(string)} \n{type(integer)}\n{type(floating_point)}\n{type(a_list)}\
      \n{type(dictionary)}\n{type(a_set)}\n{type(a_range)}\n{type(a_tuple)}\n{type(boolean)}')
      ``` 
- 실패
    ```python
    print(f'{type(string, integer)}')
    -> TypeError: type() takes 1 or 3 arguments
    type이라는 구문은 한번에 다 물어 볼 수 는 없나보다.

    뭔가 반복 구문을 어떻게 사용하면 될 것 같은데...
    ```
- 성공
  ```python
  할 수 있는 방법은 찾았는데 나중에 배우는거라 후순위로..
  ```
![이미지](bird.jpg)

- print enter 줄간격 마다 \ 자동으로 인식하는 방법이 뭘까

- ctrl / 하면 주석 온 오프, 그러면 ''나 () 만드는 법이 있지 않을까  

- 
  ```python
  my_dict = {'apple': 12, 'list': [1, 2, 3]}
  print(my_dict['apple'])
  ```
왜 대괄호?

- 
  ```python 
  my_dict_3 = {'apple': 12, 'list': [1, 2, 3], 'apple':100}
  print(my_dict_1) # 1{'apple': 100, 'list': [1, 2, 3]}
  ```
순서가 존재하지 않은데 왜 나중에 있는걸로 나오는거지?
