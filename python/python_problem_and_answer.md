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

      py = 3.14131231241224 #대충 파이를 넣은 객체라는 뜻
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
  # for 구문 사용
  # 위 구성 요소들을 담는 list 하나를 만든다.
  all_list = [string, integer, floating_point, a_list, dictionary, a_set, a_range, a_tuple, boolean]
  # for 구문을 사용하여 안의 요소를 반복해서 꺼내 type으로 print
  for i in all_list:
    print(type(i))
  

  ```

# 2024-01-16
1. ctrl / 하면 주석 온 오프, 그러면 ''나 () 만드는 법이 있지 않을까? 
 <br />
 <br />
   없는 듯하다... 영어로도 찾아보고, gpt로도 찾아봤는데 아무도 이런 생각을 하지 않은듯.. 
   
   너무 많은 걸 원하는 걸까나.. 대신 마크다운에서도 쓸만한 기능을 하나 발견함!

   ctrl + shift + R 원하는 걸 선택 후 몇 가지로 감쌀 수 있음 ~~이렇게~~

----------------------------
# 2024-01-23

1. ~~print enter 줄간격 마다 \ 자동으로 인식하는 방법이 뭘까~~
<- 쓸 일이 많이 없다는 걸 알게 되었다.
<br />
<br />

2.  아래 순서가 존재하지 않은데 왜 나중에 있는걸로 나오는거지?
  ```python 
  my_dict = {'apple': 12, 'list': [1, 2, 3], 'apple':100}
  print(my_dict) # 1{'apple': 100, 'list': [1, 2, 3]}
  ```
- 이해<br /> 
  pyhton 3.7서부터는 dictionary는 삽입순서를 기억한다.<br />
  그래서 key 값 기준으로 나열되고, value는 뒤에 동일한 key가 나오면 값이 덮어쓰기되는 듯 
  - python document 
    - Changed in version 3.7: Dictionaries did not preserve insertion order in versions of Python before 3.6. In CPython 3.6, insertion order was preserved, but it was considered an implementation detail at that time rather than a language guarantee.
  
  - stackoverflow
    - 삽입순서를 기억하기에 .popitem()으로 마지막 값을 반환할 수 있다. LIFO(후입선출) 
      - 그럼 맨 앞을 반환하는 법은 없나?
        - 그런 건 없없다. .popitme(Last=False)된다는 사람도 있다는데 안됨.  
      - 삽입 순서 기억하는 이유?
        - 3.6 까지는 개발자가 입력한 key와 dictionary가 hash 문자열 처럼 random하게 나와 불편한 점이 있었다고 한다. dictionary가 nonsequence로 순서가 없는 것은 이전과 동일하지만 key의 삽입 순서는 기억하게 만든건 개발 편의성을 위함 

# 2024-01-24

1. ~~str이 아니라 정수나 실수는 print() 안에서 \이나 \n 이용 못하나?~~
- code는 깔끔히 짜야되므로 괜한 생각
<br />
<br />
2. ~~pprint가 뭐지~~
- pretty print의 줄임말, 애매하면 help로 찾아보기

Help on function pprint in module pprint:

pprint(object, stream=None, indent=1, width=80, depth=None, *, compact=False, sort_dicts=True)
    Pretty-print a Python object to a stream [default is sys.stdout].
<br />
<br />

3. import한 모듈 빼버리는 법

- 실패 
      
      from pprint import pprint as print
      ㄴ 실습 때 이거 따라하다가 그냥 print가 안먹어서 껐다 켜버림.. 
      
      export pprint 라는 건 없나보다.

- 성공

      how to export module in python 이라고 구글링이 안되서 강사님께 물어봄,
      이전에는 비슷한 궁금증을 갖고 있는 글들을 좀 보이기라도 했는데 다들 궁금 안한가보다..

      del print
      를 쓰면 print가 원래의 print로 돌아온다.

      덤으로 import math로 math 모듈을 import 해온 것도
      del math 하면 모듈이 사라진다. 

      근데 모듈을 썼다 지웠다 하면 더러우니까 del를 안쓰도록 
      from 모듈 import 모듈 안 함수 as 명칭을 쓸 때는 명칭을 내장함수와 겹치지 않게 만드는 것이 중요할듯   

4. .capitalize()를 활용시 문자열에 '.'이 있으면 그 다음 글자도 대문자로 만들 수 없나?<br />
   \+ ?도 있을때 같이, 

   - example_sentence = "hello. my name is kim. how are you? i'm fine. thank you." 

   - wanted_output = "Hello. My name is kim. How are you? I'm fine. Thank you."

- 실패 
      
```python
# 1. .capitalize('.')는 안됨. split 처럼 되는 줄 알았는데 흠..

# 2. 원하는 seperater로 나눠서 capitalize하는 함수 2번 써서 .과 ? 뒤 대문자로 만들기
def capital_with(word_list, seperater):
    
  capital_split = word_list.split(seperater)

  capital_word = []

  for i in capital_split:
      capital_word.append(i.capitalize())
    
      capital_result = seperater.join(capital_word)

  return capital_result  


example_sentence = capital_with(example_sentence,'. ')
example_sentence = capital_with(example_sentence,'? ')

print(example_sentence) # Hello. my name is kim. how are you? I'm fine. thank you.

# 3. 처음부터 .과 ?로 split 한 다음 join 시키기, 
# 다만 join시 원하는 자리에 .과 ?를 구분하여 넣을 수 있나? 그냥 봐도 불가능할듯... 
```
- 성공일지는 모르겠지만 시도해볼 관점을 강사님께 하나 받았다.

단어로 쪼개서 하는게 아니라 문자열 하나하나로 쪼개서 하는 법 
문자열은 sequence라 for 구문을 사용할 수 있다는 점을 활용하는 것이라고 한다.

아직 for 구문과 sequence, iterable이라는 걔념들이 완전히 머릿속에 박히지 않아서 생각도 안남  

# 2024-01-25

1. 어제의 4. 여러 문장을 받을때 ?,!,.을 받으면 그 다음 문자를 대문자화하는 법

- 두번째 실패

``` python

example = "hello. my name is kim. how are you? i'm fine. thank you." 
# 최종 결과를 담을 문장 객체
result = ''

# 맨 앞자리 대문자로 만들어 미리 넣어 놓기
result = example[0].capitalize() 

# 맨 뒷자리 '.'으로 인해 아래 순환에 방해되지 않게 미리 잘라 놓기
example_sliced = example[:-1] # hello. my name is kim. how are you? i'm fine. thank you

# 순환시킬 문자열의 index 값을 count해주는 counter, 
# 1인 이유는 첫번째 단어는 이미 최종문장에 넣어놓았기에 
# 순환은 0이 아니라 1부터 시작할 예정 
sentence_index = 1

# 첫 단어는 이미 넣어놨으니 두번째 문자부터 순환
for char in example_sliced[1::]:
   
    # punctuation, ?, !를 만나면
    if char == '.' or char == '?' or char == '!' :
        # 순환하는 문자 이후 2번째 순서에 있는 단어를 대문자화
        print(char)
        example_sliced[sentence_index + 2].capitalize()    
    
    #인자를 최종 문장에 넣고 index counter를 증가시킨다.
    result = result + char 
    sentence_index += 1  

print(result) #Hello. my name is kim. how are you? i'm fine. thank you
```
실패한 이유는 **example_sliced[sentence_index + 2].capitalize()**가 안돌아간다.<br>
문자열은 불변이라는 점을 망각해서 발생함

- 첫번째 방법(feat.gpt)
```py
example = "hello. my name is kim. how are you? i'm fine. thank you." 
# 최종 결과를 담을 문장 객체
result = ''

# 맨 앞자리 대문자로 만들어 미리 넣어 놓기
result = example[0].capitalize()

# 아래 사용할 스위치
capital_boolean = False

# 첫 단어는 이미 넣어놨으니 두번째 부터 순환
for char in example[1::]:
    
    # 스위치가 True일때이고 해당 인자가 알파벳이면
    if capital_boolean and char.isalpha():
        
        # 대문자로 바꾸어서 최종 문장에 넣는다
        result += char.capitalize() 
        
        # 스위치는 끈다.
        capital_boolean = False

    else:
        #아니면 그대로 인자를 최종 문장에 넣는다.
        result += char 

    # punctuation이나 ? !를 만나면
    # if char == '.' or char == '?' or char == '!': 좀더 축약해보자
    if char in ('.', '?', '!'):
        #스위치를 켠다.
        capital_boolean = True
      

print(result) #Hello. My name is kim. How are you? I'm fine. Thank you.
```
GPT가 도와준 다른 걔념, index로 문자열에 개입하려는 방법이 아니라 스위치를 이용하는 방법<br> 

꺼둔 스위치가 ?,!,.을 만나게 된다면 켜지고, 순환하는 문자가 알파벳이면 대문자로 만들고 스위치를 끄는 걸 반복한다.

- 두번째 방법
[stackoverflow에 올린 질문에 올라간 답들](https://stackoverflow.com/questions/77871590/how-to-capitalize-sentences-consisting-of-and-punctuation-at-once?noredirect=1#comment137283745_77871590)

      import re를 사용하는 두가지 방법인데 아직 안익숙한 lamda 함수랑 모듈에 대해서 나중에 공부해서 오기
![앵무](bird.jpg)



2. python에서 한줄은 79자로 제한이 관행이면 79자인지 아닌지는 느낌으로?
[python 코드 스타일 가이드](https://peps.python.org/pep-0008/)
- 안 사실

      내가 생각한 편리한 기능은 없다. 다만 79자로 제한하는 것은 생각보다 중요한 것을 알게되었다.
      stackoverflow에서 관련된 글을 보았는데 
      80자 이상으로 넘어가면 기능을 못하게 되는 것들도 더러 있다고 한다.. 










-----------------------------------------------
- list안의 정수 개수나 문자열 개수 확인하는 법은??
```python
my_list = [1, 2, 2, '3', 3, 3]
count = my_list.count(int) #(int)는 작동 안함
print(count) # 

```

- .count() 함수에 'a'를 넣으면 대문자 A도 같이 count하게 만드는 법
  isdecimal과 같은 것이 있을지도


- for 구문 돌떄 in 다음에 있는 부분의 길이를 조작하면 안됨 꼬임
내용 옮기기

- .super() 쓸때 상위 클래스 중 우측것이 필요할때는?