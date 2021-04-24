# airflow_test

### flow 연습 

- 조건 1. venv 적용
- 조건 2. fileio 테스트
- 조건 3. 종료 후 메시지 (telegram)


### 참고 ref


### 확인 내용

 - 1. venv 환경에서 python 실행을 위해서는 쉘 내 venv & 파이썬 코드 같이 수행 
 -- airflow내 pythonVirtualenvOperator가 따로 있지만 해당 함수는 특정 env 수행이 아닌 subprocess느낌으로하는 내용인듯 ( https://stackoverflow.com/questions/49738173/how-to-run-airflow-pythonoperator-in-a-virtual-environment ) 해결책으로 python이 아닌 virtualenv 경로의 python을 사용하는듯
 
 여러가지 방법을 찾아봤지만 쉘 내에서 activate후 python 실행을 하는 파일을 생성후 bashoperator로 수행하는것밖에 해결방법을 못찾음
 
 - 2. bashoperator에서 sh 뒤에 space 한개필요.. https://cwiki.apache.org/confluence/pages/viewpage.action?pageId=62694614


경험치 블로그
https://monkeydev.tistory.com/2

