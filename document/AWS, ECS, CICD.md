# Next.js와 AWS ECS, CI/CD 구성방법


### 셋팅환경  
Node.js v18  
TS  
yarn v1  
Next.js


#### Github Actions가 동작하는 조건
- branches : 대상 브랜치에 push가 발생하면 동작
- pull_request : 조건을 만족하는 브랜치를 base로 하는 PR에서 동작


#### node_modules 캐싱
- actions/cache: 빌드마다 node_modules 설치를 피하기 위해 캐시하는 모듈
- 18버전과 20버전의 빌드가 각 각 돌고 있는데 캐시는 yarn.lock의 해시 기준으로 되는가?


github 액션을 통해 자체적으로 빌드를 돌리고 배포까지 할 수 있게 된 상태
=> CI연동 완료

2. AWS ECR&ECS 설정
- ECR : Elastic Container Registry  
  AWS에서 제공하는 도커 이미지 저장소, Docker Hub와 유사한 서비스
- ECS : Elastic Container Service,
  컨테이너 관리 서비스

AWS ECS는 서비스와 테스트 라는 가상의 단위로 관리된다.
서비스는 서비스 정의와 테스크 정의를 기반으로 구성되어 있다.

2-1. VPC 생성  
VPC는 AWS 클라우드 내의 가상 네트워크
VPC and more 선택, 대부분은 기본값을 사용
컨테이너는 Private으로 띄울 것이므로 NAT gateway를 생성해야 한다.


3. AWS ECS 생성
- ECS 클러스터는 컨테이너 인스턴스를 실행하는 가상 클러스터


  
<br/>
AWS CodeCommit
- 완전 관리형 소스제어 서비스
    - GitHub, GitLab 등

AWS Pipeline
-   