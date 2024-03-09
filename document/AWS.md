
### AWS 

#### DevOps 방식 및 도구
- CI/CD
- 관찰가능성(Observability)
- 인프라의 코드화
- Source/Artifact 관리
- 복원력 및 보안

<br/>

#### AWS CodeCommit 
: 프라이빗 Git repo를 호스팅하는 안전하고 확장성이 뛰어난 관리형 소스 제어 서비스

GitHub, GitLab, PERFORCE, SVN 등과 같은 소스 제어 시스템을 사용하여 코드를 저장, 관리 및 협업할 수 있음

- 완전 관리형 소스제어 서비스
- Git 스탠다드 지원 : Git 명령어 다 사용가능
- IAM과 통합하여 repo에 대한 사용자별 액세스 가능
- HTTPS, SSH 지원

<br/>

#### AWS CodeBuild
: 완전 관리형 빌드 서비스로, 소스 코드를 컴파일, 테스트 및 배포 가능

- 완전 관리형 빌드 서비스
- 사용한 만큼 지불
- 빌드 요청에 따라 확장 가능
- CI/CD 활성화
- 보안

<br/>

#### AWS CodeDeploy
: 다양한 컴퓨팅 서비스에 대한 SW 배포를 자동화하는 완전관리형 배포 서비스

- 모든 인스턴스에 대한 코드 배포 자동화
- 빠르고 안전한 배포
- 배포 중 다운타임 방지
- 실패가 감지되면 자동으로 롤백


<br/>

#### AWS CodePipeline
: CI/CD를 위한 완전 관리형 지속적 통합 및 지속적 배포 서비스,  
릴리스 파이프라인을 자동화를 위한 완전관리형 지속적 전달 서비스

<br/>

---
<br/>

- 롤링업데이트 : 배포 중 다운타임이 없도록 하기 위해, 기존 인스턴스를 새로운 인스턴스로 교체하는 방식

- 블루그린 배포 : 새로운 인스턴스를 추가하여 트래픽을 점진적으로 이동시키는 방식

- 카나리아 배포 : 새로운 버전을 일부 사용자에게 노출시키고, 문제가 없을 경우 모든 사용자에게 노출시키는 방식

