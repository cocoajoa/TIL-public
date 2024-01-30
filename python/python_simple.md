# 파이썬 간략 정리
1. _ 의 정의
- 대화형 인프린터에서 _의 의미는 이전 결과 값을 의미함
  - 1 + 1 -> 2 이후 2 + _ 는 2 + 2를 의미한다.  
  - _에 직접적인 의미를 부여하면 내장함수쪽에서 에러가 생길 수 있음

- 인터프린터에서 _가 앞에 붙어있을 경우 단순한 읽기 or 참고용이라고 본다고 한다. 
- ex) _counter 

2. \ 사용
- 예외 처리 또는 특별한 사용 \n = 띄워쓰기
```python
print('first \nsecond') # first
                        # second                        
```
- r-string을 앞에 넣으면 \를 무력화 시킬 수 있음(raw string)
```python
print(r'first \nsecond') # first \nsecond               
```

3. """""" 사용
- \n과 n을 안쓰고 문자열에 자유로움을 부여 가능
```python
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")  
#Usage: thingy [OPTIONS]
#     -h                        Display this usage message
#     -H hostname               Hostname to connect to
```

4. 긴 문자열 쪼개기
- '가' '능' -> '가능' 과 같이 둘이 붙일 수 있음
```python
print('I\'m' 
    ' Kim') # I'm Kim              
```

5. 다중 대입
- 아래와 같이 다중 대입이 가능함
```python
a, b = 1, 0 # a = 1, b = 0

```

#### 2024-01-25
- new learned
1. f-string이랑 비슷한 r-string의 존재, 별로 쓸 일은 많은 것 같지 않다. 

2. 문자열 쪼갤 시 '' '' 사용 가능한 점, \만 사용 가능 한 줄 알았다. 

3. 다중대입을 사용하면 clean code가 될까? 
- missed one
- correction