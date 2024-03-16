# vscode extension을 만드는 법은? 
chatGPT와 vscode 공식 doucmention을 주로 참고하여 만들어보자
  
1. node.js 와 Git 준비 필요함
   - git은 준비됬지만 node는 준비가 안되어있다.
  
   - 자바스크립트를 아직 배운 적이 없지만 그냥 보고 따라해보기
     - LTS 버전으로 깜
       - **문제 발생!** 설치했는데 인식을 못함
         - 다시 설치하고 시스템 환경 변수에서 path가 잘못 설정된건가 찾아봤는데 정상
         - 결국 껐다키니 인식됨, 만능이다.
<br /><br />

2. Yeoman 및 VSCode Extension Generator 설치
   - Yeoman은 프로젝트 생성을 자동화하는 도구이고, VSCode Extension Generator는 Yeoman 제너레이터 중 하나로, VSCode 확장 프로그램을 빠르게 시작할 수 있도록 도와준다고 한다.
     - 사실 따라하는 입장에서는 그런게 있다 정도로 받아들여진다. 
  
   - bash에서 아래와 같이 입력하여 설치
     - npm install -g yo generator-code
<br /><br />

3. -yo code로 만들 것 설정하기?  
   - 실행 시 yeoman을 통해 다양한 방식의 기본 extenstion을 고를 수 있다.
     - New Extension (TypeScript or JavaScrpit) 등등 
   - 내가 원하는 건 자동으로 한국어 맞춤법가 표시되는 것인데 무엇을 선택해야할까?
     - 제일 그럴듯해보이는 건 언어이기에 New Language Support와 New Language Pack (Localization)
       - New Language Support는 언어팩을 의미하는 것일 수도 있기에 그냥 New extension이 맞을 수도 있지 않을까?
     - 내가 참고하려던 Code Spell Checker extension 중 '나라 언어- Code Spell Checker'를 참고해보자. [가즈아](https://github.com/streetsidesoftware/vscode-cspell-dict-extensions)
       - 친절히도 아래와 같이 만드는 법 링크를 read.me 에 써주었다.
         - https://github.com/streetsidesoftware/vscode-cspell-dict-extensions/blob/main/CONTRIBUTING.md#how-to-create-a-new-extension
<br /><br />
------
# Code Spell Checker 깃헙에서 안내한대로 만들어보기

1. 포크하기
   - 오픈 소스 프로젝트를 클론하는 것을 의미, 우 상단 fork버튼을 통해 진행함

2. yo cspell-dict-extensions Korean 진행하기
   -  Yeoman을 사용하여 cspell-dict-extensions 제너레이터를 실행하고 새로운 언어의 확장 프로그램을 생성하라는 것을 의미한다고 한다.
      -  error가 떠서 잘 보니 generator가 설치 안되어있다고 경고가 뜬다. 하라는대로 받음 npm run create:extension
         -  잘 안풀리는게 있으면 문서를 잘 살펴보자.
            -  위대로 쳐도 에러 나오고, 에러 나온것을 살펴보고 하라는대로 안되었는데 문서 하단에 적혀있던 npm install와 npm run build 시행하니 됨

3. 쓰라는대로 내용 입력 - **문제 봉착함**
   - 간단히 언어와 만들어질 이름을 적으라는대는 문제가 없었으나 아래와 같이 소스 사전을 연결해야하는데 한국어가 없다. 
      ```
      Source Dictionary	This is the NPM install name of the source eg. dictionary @cspell/dict-sv (@ is needed). Available dictionaries could be found here https://github.com/streetsidesoftware/cspell-dicts#all-dictionaries
      ```
     - 들어간 cspell-dicts의 언어 중 하나를 참고하여 만들어보기 or 한국어 맞춤법 교정하는 extension을 만든 곳의 github를 들어가서 베끼기 중 무엇이 나을까 고민
       - 기존 규격에 맞게 해야지 오류가 나지 않을 것 같아 전자를 선택, 독일어 버전을 참고해서 하기로 결정함

4. 언어 소스 사전 만들기?
- csspell-dicts 중 독일어 read.me를 읽었는데 이 사전의 resource는 아래 깃헙이라고 한다. 근데 들어가보니 한국어 사전도 있다!! 
- https://github.com/wooorm/dictionaries/tree/main#readme
  - 독일어로 설정된 부분을 모두 한국어로 바꾸면 작동하지 않을까?
    - 일단 이것도 포크해서 내 깃헙에서 다뤄보자
    - https://github.com/wooorm/dictionaries/tree/main?tab=readme-ov-file#readme 
      - 독일어의 경우 hunspell이 있는데 비슷한게 여기 있어서 일단 한국어 버전걸로 복붙   
    1. 새로운 문제 봉착 trie.gz는 어디서 얻지?
      - 따라 수정하고 있는데 나라언어.trie.gz 란 파일이 안보인다. 다른 곳에서 찾아봐도 안 나옴..
        - 어쩔 수 없이 https://github.com/streetsidesoftware/cspell-dicts에 나온 새로운 dictionary를 만드는 법을 참고해서 만들어보자. 
 
### 새로운 dictionary 만들기
1. Pnpm 설치 / npm install -g pnpm
  - npm 과는 다르다하니 설치   