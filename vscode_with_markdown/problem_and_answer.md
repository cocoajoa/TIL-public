# 2023-01-12
1. vscode에서 빈칸 간격 있는 파일 만들기
- 실패

        touch problem and answer
        -> problem, and, answer 파일 생성됨..
            여러 파일 생성시 touch A B C 원리

        touch github keys and manual(learned)
        -> break
            ()가 무슨 함수인줄암..파이썬 처럼 /같은 것을 넣으면 될 줄 알았는데 안됨
        
- 해결

        touch 'problem and answer'
        -> problem and answer라는 하나의 파일 생성
            다만 파일 유형 빼먹으면 안됨...

2. vscode에서 start 사용 시 cmd가 왜 켜짐??
- 실패

        start problem\ and\ answer.md 
        -> cmd가 켜짐
            README.md는 vscode에서 켜지는 데 왜일까?

- 성공

        mv problem\ and\ answer.md 'problem_and_answer'.md
        -> 파일 간 공백을 디렉토리로 인식하는 문제가 발생할 수 있어 
        스페이스바 대신 _ 사용을 권한다는 내용 확인, 수정 후 잘 돌아감^^ 

# 2024-01-14
1. 빈 폴더는 업로드 불가능?
- 실패

        mkdir python
        -> python 공부 들어가기에 앞서 만들어둔 폴더가 github에는 올라가지 않은 점 확인
        web 검색을 통하여 확인한 바로는 파일 단위로 변경 이력을 확인하기 때문이라고 함 
        git status 로 확인 시 이 점 확인 가능하였다.  

- 성공

        .gitkeep or .keep 이라는 더미 파일을 빈 폴더에 보관하기(관행) 
        mkdir python
        touch python/.gitkeep
        
        ㄴ / 이걸 써서 굳이 아래처럼 파일을 생성안해도 되는 점을 추가로 배웠다!
    
        cd pyhton
        touch .gitkeep

        그런데 결국 .gitkeep이라는 신경쓰이는 무언가가 남는 것 아닌가? 관행이라고는 하나.. 
        .gitignore에다가 아래 두 개를 입력해도 안되니 어쩔수 없을 것 같다..
        python/.gitkeep #python 폴더 내 .gitkeep은 추적 예외
        !python         #python 폴더는 추적하도록



        아래처럼 .gitignore 활용하기도 있다는데 sample folder로 시도해서 
        git status 확인해도 안됨.. 골치 아프니 관행을 따르는 걸로.. 
        
        .gitignore에 !폴더이름/* 추가?

        !는 예외 설정 /*는 해당 다이렉토리 내 파일을 의미하는 것으로 보이는데.. 
        



    자동으로 빈 다이렉터리에 .gitkeep을 만들어주는 코드라는데.. find empty 말고는 아직 이해를 못하겠으니 **나중에 확인!**
         

        find . -type d -empty -exec touch {}/.gitkeep \;

![이미지](TIL-public\image.bird.jpg) 

# 2024-01-15

1.  -만 표시 되게하는 법
- 실패 

        '-, ~- 
- 성공 

        \-
        오늘 배운 역슬래쉬가 답이었다. 왠만한 문법 탈출은 이제부터 \로 해보기 
        
# 2024-01-16

1. 마크다운 표 만드는 법
- 실패?
  
  |  김  |  밥  |  만  |
  |:---: |:---: |:---: |
  |  순  |  대  |  도  |
  | 뭐가 |다른데|   응? |

  분명 jupyter에 있는 걸 따라 만들어봤는데 많이 다르다.. 
  
  칸 사이 세로축도 없고, 위랑 아래랑 선 선명도가 다름 왜??  
  

stack overflow에 markdown no bodrders 관한 질문은 있는데 보통 없애는 걸 물어보는 거다. 왜 난 없지?




2. 마크다운 글 간 간격 늘리기
- 실패

        첫번째 글

        두번째 글


        세번째 글

  첫번째 글 

  두번째 글
    

  세번째 글

  같은 간격이지만 코드 블럭이 아니면 두번째랑 세번째가 똑같음
  
  <br />
  
  빈 공간에다가 아무거나 눌러보다가 화면 확대 축소 기능이나 알게되었다 깜짝 놀랐네 ㅎ..(ctrl + '+' or '-')

- 성공

   ```html
        첫번째 글
        두번째 글
        <br />
        <br />
        세번째 글
   ```
  stack overflow에서 가장 추천수가 많은 2가지를 보면 보통 \<br />와 \&nbsp;를 언급한다.
  
  \<br />는 html를 지원하는 markdown 환경에서만 가능하다는데 html의 개념을 배울 예정이라 지금은 일단 그렇다는 정도로 이해 해야겠다. 
  <br />
  <br />
  ASCII character라는 \&nbsp; 는.. 아직 잘 모르겠다. 줄 한칸 띄워쓰기 **보다는** &nbsp;&nbsp;&nbsp; **이런** 식으로 쓰는 것 같은데...
  
  강조 표시한 정도로 단어 간 띄우려면 \&nbsp;\&nbsp;\&nbsp; 정도는 써야된다..

  아래에 더 공부하고 싶은 가운데 정렬 같은 느낌으로 만들고 싶으면 \&nbsp;만 75번 눌러야되는 문제가......
  뭔가 다른 게 있을 것 같음 
  


-------------------------



- 2-1. 이런거는 마크다운에서 1. 과 - 처럼 사용 못하나??
 
- 마크다운 글자를 중간에 위치하게 만드는 법
- 탭키 연타 사용시 생기는 코드블럭의 정체???

- git에서 관리하는 폴더 내에서 이미지 갖고오는법?
   ![이미지](TIL-public\image.bird.jpg) 


- cd .. 위쪽 다이렉토리 2단 뛰기 같은거 어케하지?
- 파일 삭제 말고 닫기
-   
눌러보다가 추가로 뭔가 쓸모없는 느낌이 드는 기능 2개 더 찾음

 ctrl + I  
  
   *기울이기* 를 해주긴 하는데 ctrl + / 처럼 그 라인 전체 적용하는 것도 안되고 전체 선택을 하면 이상하게 묶여서 정확히 원하는 부분을 드래그해서 사용해야됨. 
   
   기울임 말고 강조표시는 어케하는 거지? 

 ctrl + \ 
  
  파일이 하나 더 열림..뭐할 때 쓰는거지?