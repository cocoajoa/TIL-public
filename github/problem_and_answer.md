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