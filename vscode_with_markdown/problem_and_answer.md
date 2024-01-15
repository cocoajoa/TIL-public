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
실패 

        '-, ~- 
성공 

        \-
        오늘배운 역슬래쉬가 답이었다. 왠만한 문법 탈출은 이제부터 \로 해보기 
        
1. 

- 마크다운 표만드는 법
- 마크다운 글 간 간격 늘리기
- 마크다운 글자를 중간에 위치하게 만드는 법
- 탭키 연타 사용시 생기는 코드블럭의 정체???

- git에서 관리하는 폴더 내에서 이미지 갖고오는법?
   ![이미지](TIL-public\image.bird.jpg) 