### Auto Scaling

1. Auto Scaling이 필요한 이유와 역할 설명해보기

2. EC2 인스턴스 생성하기 (서울 리전, Bitnami Wordpress, t2.micro)

3. ALB 생성하기 (EC2 인스턴스와 같은 리전)

4. 생성한 EC2 인스턴스를 기반으로 AMI 생성하기

5. Auto Scaling Group(ASG) 생성하기
    - 시작 템플릿도 함께 생성하기
    - ALB와 연결하기

6. EC2 인스턴스에 ssh로 접속하고 stress를 사용하여 Auto Scaling 작동 테스트 하기

7. 모든 리소스(EC2, AMI, ASG, ALB 등) 정리하기