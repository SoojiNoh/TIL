



# Git 기초

## Git 초기 설정

> 최초 한번만 설정
>
> 매번 git을 사용할 때마다 설정할 필요 X
>
> ex) 오프라인 시행 시 멀캠 교육장 처음 갔을 때 또는 컴퓨터를 새로 샀을 때
>
> 1. 커밋 작성자 정보 등록
>
>    `$ git config --global user.email "깃헙에서_사용할_이메일"`
>
>    `$ git config --global user.name "깃헙_닉네임"`
>
> 2. 커밋 작성자 정보 확인
>
>    `$ git config --global -l`
>
>    또는
>
>    `$ git config --global -list`
>
> 3. 커밋 작성자 정보 변경
>
>    `$ git config --global user.email`
>
>    `$ git config --global user.name`



# Git 기초 명령어

## 1.로컬 저장소

* working directory : 사용자의 일반적인 작업이 이뤄지는 곳
* staging area : 커밋을 위한 파일 및 폴더의 변경사항들이 (임시로) 저장되는 곳
* repository (commits): staging area에 있던 파일 및 폴더의 변경사항들이 커밋으로 저장되는 곳
* Git은 working directory(WD) →  staging area → repository의 과정으로 버전 관리를 수행합니다.



## 2. git init

: 현재 작업 중인 디렉토리(폴더)를 Git으로 관리하겠다는 명령어

* .git이라는 숨김 폴더를 생성하고, 터미널에는 `(master)`라고 표기됩니다.

​	! 주의 사항 🚫

​	1. 이미 Git 저장소인 폴더 내에 또 다른 Git 저장소를 만들지 않습니다. (중첩 금지)











## 3. git status

: working directory와 stageing area에 있는 파일의 변경사항을 알려주는 명령어

* 어떤 작업을 시행하기 전에 수시로 status를 확인 합니다.

* 상태의 종류

  1. `untracked` : Git이 관리하지 않는 파일 (한 번도 add를 한 적 없는 파일)

     * ex) 처음 생성한 파일

  2. `tracked` : Git이 관리하는 파일 (이전에 한 번이라도 add를 한 적 있는 파일)

     * `unmodified` : 최신 상태 (이전 버전에 비해 변경사항이 없는 상태)
     * `modified` : 수정되었지만 아직 staging area에 올라가지 않은 상태
     * `staged` : staging area에 올라간 상태

     

  * 파일 라이프 사이클 예시

    ![img](https://media.vlpt.us/images/soyi47/post/380d5d65-c1a9-4c28-83ef-9a920c43196d/lifecycle.png)



## 4. git add

* working directory에 있는 파일을 staging area에 올리는 명령어
* git이 해당 파일을 추적(관리)할 수 있도록 만듭니다.
* `untracked, modified `⇨` staged` 로 상태를 변경합니다.

* 예시

​		`# a.txt만 staging area에 올리는 명령어입니다.`

​		`$ git add a.txt`



​		``# a.txt만 staging area에 올리는 명령어입니다.`
​		`$ git add a.txt`



​		`# 현재 디렉토리의 모든 파일을 staging area에 올리는 명령어입니다.`

​		`$ git add .`

## 5. git commit

*  staging area에 올라온 파일의 변경 사항을 하나의 버전(커밋)으로 저장하는 명령어
* **커밋 메세지** 는 현재 변경 사항들을 잘 나타낼 수 있도록 `의미있게` 작성하는 것을 권장합니다.
* 각각의 커밋은 `sha-1 알고리즘`에 의해 **반환된 고유의 해시 값을 ID**로 가집니다.





## 6. git log

* 커밋의 내역(commit ID, 작성자, 작성 시간, 커밋 메시지 등)을 조회할 수 있는 명령어
* 옵션
  * --online : 커밋 메시지를 한 줄로 축약해서 보여줍니다.
  * --graph : 브랜치와 머지 내역을 그래프로 보여줍니다.
  * --all : 현재 브랜치를 포함한 모든 브랜치의 내역을 보여줍니다.
  * --reverse : 커밋 내역의 순서를 반대로 보여줍니다. (최신 커밋이 아래로 가도록 설정)
  * -p : 파일의 변경 내용도 같이 보여줍니다.
  * -2 : 원하는 개수 만큼의 커밋 내역을 보여줍니다.
    * 2말고 다른 숫자 가능





## 7. git remote

* 로컬 저장소에 원격 저장소를 `등록, 조회, 삭제` 할 수 있는 명령어

1. 원격 저장소 등록

   `git remote add <이름> <주소>` 형식으로 작성합니다.

   

![image-20220113150957491](Git 기초.assets/image-20220113150957491.png)

![image-20220113151145402](Git 기초.assets/image-20220113151145402.png)





## 8. git push

* 로컬 저장소의 커밋을 원격 저장소에 업로드하는 명령어
* `git push <저장소 이름> <브랜치 이름>` 형식으로 작성합니다.



```python
$ git push origin master

[풀이]
git 명령어를 작성할건데, origin이라는 이름의 원격 저장소에 Master 브랜치의 commit들을 Push(올린다).
```







# 기타 스크린샷.

## git add, commit, push

![image-20220113113405283](Git 기초.assets/image-20220113113405283.png)





![IMG_7829](Git 기초.assets/IMG_7829.jpg)

![IMG_7830](Git 기초.assets/IMG_7830.jpg)

![IMG_7831](Git 기초.assets/IMG_7831.jpg)

![IMG_7832](Git 기초.assets/IMG_7832.jpg)

![IMG_7833](Git 기초.assets/IMG_7833.jpg)

![IMG_7834](Git 기초.assets/IMG_7834.jpg)

![IMG_7835](Git 기초.assets/IMG_7835.jpg)

![IMG_7837](Git 기초.assets/IMG_7837.jpg)

![IMG_7838](Git 기초.assets/IMG_7838.jpg)

![IMG_7839](Git 기초.assets/IMG_7839.jpg)

![IMG_7840](Git 기초.assets/IMG_7840.jpg)

![IMG_7842](Git 기초.assets/IMG_7842.jpg)

![IMG_7843](Git 기초.assets/IMG_7843.jpg)

![IMG_7844](Git 기초.assets/IMG_7844.jpg)



## Git Pull



![image-20220113152139911](Git 기초.assets/image-20220113152139911.png)

![image-20220113152211504](Git 기초.assets/image-20220113152211504.png) 



![image-20220113153508462](Git 기초.assets/image-20220113153508462.png)



![image-20220113153614989](Git 기초.assets/image-20220113153614989.png)









## GitLab

![image-20220113170613977](Git 기초.assets/image-20220113170613977.png)

![image-20220113170719362](Git 기초.assets/image-20220113170719362.png)



![image-20220113170744095](Git 기초.assets/image-20220113170744095.png)