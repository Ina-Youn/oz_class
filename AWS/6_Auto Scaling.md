### Auto Scaling

1. Auto Scaling이 필요한 이유와 역할 설명해보기
    - 트래픽에 따라서 자동으로 서버/EC2 인스턴스 의 개수를 조절해주는 기능
    - 안정적이며 효율적인 서버 운영 가능

2. EC2 인스턴스 생성하기 (서울 리전, Bitnami Wordpress, t2.micro)

3. ALB 생성하기 (EC2 인스턴스와 같은 리전)

4. 생성한 EC2 인스턴스를 기반으로 AMI 생성하기

5. Auto Scaling Group(ASG) 생성하기
    - 시작 템플릿도 함께 생성하기
    - ALB와 연결하기
<img width="620" alt="스크린샷 2024-02-20 오전 10 56 51" src="https://github.com/Ina-Youn/oz_class/assets/155051602/3cd137f6-7dee-4dc8-abe0-f4e55e83c001">


6. EC2 인스턴스에 ssh로 접속하고 stress를 사용하여 Auto Scaling 작동 테스트 하기
    <img width="501" alt="스크린샷 2024-02-20 오전 11 04 49" src="https://github.com/Ina-Youn/oz_class/assets/155051602/10479d4f-983b-4435-b1f0-3ff773c55d96">
   <img width="1413" alt="스크린샷 2024-02-20 오전 11 14 19" src="https://github.com/Ina-Youn/oz_class/assets/155051602/e8fa1ae5-be6f-4977-a236-310b642531da">


8. 모든 리소스(EC2, AMI, ASG, ALB 등) 정리하기
