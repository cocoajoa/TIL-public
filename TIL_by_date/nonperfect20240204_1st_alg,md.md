# 2024-02-03

- [x] 보충 필요
- [ ] 완성


TIL을 일자별로 나누는 걸로 시도하는 첫날 ~~말 그대로 Today_I_learned이니...~~

알고리즘 문제 풀이 위주로 혹사당해 요즘 python 문제나 복습이 더뎌지고 있다...<br>
천천히 해봐야지


## 궁금한 점

1. 알고리즘 문제풀 시 함수 생성 관련? 과연 옳게 하고 있었던 것인가?

- 알고리즘 문제를 풀고 해답을 받을 때를 보면 가끔 바로 푸는 것이 아니라<br>
  def로 함수를 만들어 놓고 하단에 인자와 함께 넣어 풀기도 한다.

    - 이전 파이썬에서 배우고 조금씩 읽고 있는 클린코드 3.함수에서는<br>
      함수를 만들시 여러 기능을 다 하는 것보다는 최대한 단순하게<br>
      만드는 것을 권장한다.

      - def로 따로 만드는 이유가 단순히 읽기 쉽게라면,<br>
        과연 원하고자 하는 방향대로 이루어졌는가?<br>
        -> 주석을 달아도 No같음..

      - 해결 방법은?<br>
        -> 1. 함수를 안 만들기 / 가시성 악화..<br>
        -> 2. 배운대로 함수는 단일기능만 하게해서 여러 개 만들기<br>
      
        - <mark>2안 선택해서 진행해 보기로
   
     - 취업을 위해서는 알고리즘 문제를 잘 푸는 것에 집중하는 것이 맞지만<br>
        더 중요한 건 기본이라고 생각한다.
        
<br />
2. [마크다운] 관련 많이 거슬렸던 2개 우선 해결해보기[^1] 

   - 놀랍게도 찾아보려던 1가지는 공식 문서에 나오지 않는다. 1개는 보니 알았다.

   1. &nbsp;&nbsp; 2-1, 2-2. 사용법? (**없음**) 
      - 1), 2)도 되긴하는데 공식문서에서 쓰지 말라고 &nbsp*; 한다. 
      - 어떻게든 만들 수 있겠지만 다른 사람과 상호 작용하지 않은 설정을 추가할 생각은 없다.


   2. \&nbsp; <- 잘쓰고 있으나 가운데 정렬은 없나? (있음) 
      - 아래 배운대로 <>를 이용한 \<center>를 해보니 된다!<br>
        근데 center 색이 <font color = 'red'>빨갛다.</font> 
        - 근데 font도 마찬가지긴함
        - 빨간 색은 일반적으로 지원하지 않은 방식을 의미한다고 한다. 
      - 실제 사용하는 방법은 다음과 같다. [stackoverflow_출처]
      ```markdown
      <center>centered text</center> 내가 찾아낸 어거지
      <p style="text-align: center;">Centered text</p> 정석
      <div style="text-align: center"> your-text-here </div> HTML 지원시
      ```
      - 여기서 div만 우측 정렬이 된다. 
      - HTML 지원되지 않은 환경은 없으면 div 쓰는데, 모르겠다.


## 새로 배운 점

1. [마크다운] 새로운 문법 / 유용하다고 생각한 것만 익힘

   - 주소 나누기(?) ~~주석(footnotes)~~
    
      ~~이동 전 문장[^원하는_글씨] + [^원하는_글씨]:이동 후 문장~~~
      ```markdown
     [원하는_사이트_이름]   하단 [원하는_사이트_이름]:사이트_주소
     ```
     - 이전부터 쓰던 \[원하는_이름](주소)이 많을 경우, 하단에 한번만 적어놓으면<br>
       여러번 재활용 가능하다.
       - 다만 내가 바라고 찾은건 각주인데 삭선 처리한대로 하면 안됨..
       - 혹시 vscode에서는 적용 안되나 git hub에서는 될 수 있으니 <mark>실험해보기[^실험]


   - 강조 표시(<mark>highlight</mark>)
     ```markdown
     <mark>강조할 곳</mark>   한문장 전체로 할시 뒤는 없어도 됨
     ```
     - markdown 공식 문서에는 ==강조== 로도 가능한 곳이 있다는데..
       - 일단 preview에서 작동 안됨 + github table에서도 안된다더라<br>
         [stackoverflow_카더라]
         
     - <>를 사용하는 문법은 끝맺고 싶을때 </>를 쓰는 것 같다. 
   
   - 색깔놀이
      ```markdown
      <span style = "color:red">쓸 글씨</span> 기본 사용법
      <font color = 'red'>빨갈뿐</font> HTML을 지원할 경우
      ```

   - 예쁜 체크처리? (Task list)
     ```markdown
     - [x] 체크는 x
     - [ ] []안에 빈 공간 만들기
     ```
  

   - HTML과 같이 확장 syntax로 이루어진 것들이라 적용이 되는 것도 안되는 것도 있다..
  



#### 고민

1. 마크다운말고 다른데에 적을까.. 고민
   1. 그림 사이즈 조절이 안된다..
   2. 은근 안되는 것도 많다. 쥬피터노트북처럼 python 바로 실행 같은 것들






[마크다운]:https://www.markdownguide.org/cheat-sheet/

[stackoverflow_출처]:https://stackoverflow.com/questions/35077507/how-to-right-align-and-justify-align-in-markdown

[stackoverflow_카더라]:(https://stackoverflow.com/questions/25104738/text-highlight-in-markdown)

[^실험]:today