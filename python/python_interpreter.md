# intepreter

1. intepreter 실행 및 끄기
  - 실행
    - terminal 환경에서 python 입력, window는 창에서 py 검색 후 실행
      - 단점은 한번에 한 명령어씩 밖에 입력 불가능
    - .py 확장자 파일로 열기
  
  - 종료
    - quit() 
    - window py로 켰을시 ctrl+z
    - mac(유닉스) zsh로 켰을시 ctrl+D, **command+D가 아님** 

2. .py 파일 실행시 인자도 같이 입력해서 출력하기

  - .py 이후 인자 받을 것들 입력 시, 파일제목.py와 함께 인자를 리스트로 저장하고 있음 
    - ex) test.py 3 4 를 terminal에 입력시 어딘가에는 ['test.py', '3', '4'] 라는 리스트가 생김 
  - sys라는 모듈로 인자를 원하는 곳에 삽입 가능
    - import sys #sys 모듈을 갖고온다.
    - print(sys.argv) #위 리스트가 나오니 원하는 인자를 갖고와서 쓰면됨





#### 2024-01-25
- new learned
1. 종료 시키는 법(quit() or ctrl+Z)를 알게 되었다.
가끔 vscode terminal에서 .py 파일 실행을 위해 타자 치다가 python만 치면<br>
python intepreter로 넘어갔는데 되돌리는 법을 몰라 그냥 껏다가 켰는데 잘 됬다.

2. python document 자습서를 혼자서 처음부터 봤으면 import가 뭔데하고 이해가 하나도 안됬을 뻔..
- missed one
- correction