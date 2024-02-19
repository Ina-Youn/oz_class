### ELB

1. 로드밸런싱이 필요한 이유와 역할 설명해보기
- 로드밸런싱이란 Load Balancing 알고리즘에 따라서 요청들을 분산시키고, 각 서버에서 처리하는 것
- 성능 향상, 안정성 향상, 서버 장애 예방, 고가용성(고장이 잘 나지 않음), 성능 향상 기반 제공

2. EC2 인스턴스 생성하기 (서울 리전, Bitnami Wordpress, t2.micro)

3. ALB 생성하기 (EC2 인스턴스와 같은 리전)
    - 대상 그룹도 함께 생성하고 EC2 인스턴스를 대상 그룹에 포함시키기
<img width="908" alt="스크린샷 2024-02-19 오후 5 08 12" src="https://github.com/Ina-Youn/oz_class/assets/155051602/810617ee-423e-409d-8171-8b844c441844">

4. ALB의 주소를 통해 EC2 인스턴스에 접속하기
<img width="262" alt="스크린샷 2024-02-19 오후 5 13 17" src="https://github.com/Ina-Youn/oz_class/assets/155051602/00aaab7b-99a9-454f-95fa-7ad89d379132">

<img width="856" alt="스크린샷 2024-02-19 오후 5 13 27" src="https://github.com/Ina-Youn/oz_class/assets/155051602/fabc6c24-d9d0-47e7-9734-eb077939db38">

5. EC2 인스턴스 종료하기
