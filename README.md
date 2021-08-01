# Welcome! 

> 해당 README는 [단국대 알고리즘 스터디](https://github.com/DKU-STUDY/Algorithm)를 참고했습니다.

## 알고리즘 유의사항
코드리뷰의 가독성을 위해, 변수명과 로직을 명확하게 하도록 노력합시다.  
현업에서 내가 짠 코드를 나 혹은 다른 사람이 이해할 수 있게 짜는, 배려가 중요합니다.  
주석을 달지 않아도 이해할 수 있을 정도의 코드를 짜봅시다.  

## 참여 방법
1. 본 repo를 fork
2. fork 한 repo에서 upstream으로 원본 repo 등록
    - `git remote add upstream https://github.com/whalesta/algorithm.git`
    - 원본 repo에 변경사항이 생길 때 마다 
        - `git fetch upstream`
        - `git merge upstream/master`
3. 알고리즘 풀이 후 본인의 repo에 push
4. Pull Request (PR) 생성
5. 코드 리뷰 완료 후 merge
- [참고](https://codingpracticing.tistory.com/91)

## repo 관리 방법

### 폴더 구조
> 알고리즘출처/문제번호_제목/사용자이름.py

예시
- BOJ/10828_스택/4923.py

### PR 규칙
1. PR 제목
    > [알고리즘분류] 알고리즘 제목, label : 문제 푼 곳, 언어, 난이도 (옵션)

2. PR 본문
풀이 아이디어, 어려웠던 점, 리뷰를 원하는 내용을 적어주시면 됩니다.  
구체적인 코드 로직은 주석으로 작성하셔도 무관합니다.


- Merge 기준
    - 리뷰가 완료되었을 때 본인이 merge

### Code Review 방법
다른 사람의 코드를 보고 느낀 점이나 잘 했다고 생각하는 점 또는 보완이 필요한 점을 자유롭게 적어주시면 됩니다.

### 사용중인 Online Judge
- [BOJ](https://www.acmicpc.net/)
- [Programmers](https://programmers.co.kr)