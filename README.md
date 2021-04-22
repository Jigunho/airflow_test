# airflow_test

### flow 연습 

- 조건 1. venv 적용
- 조건 2. fileio 테스트
- 조건 3. 종료 후 메시지 (telegram)


### 참고 ref


### 확인 내용

 - 1. venv 환경에서 python 실행을 위해서는 쉘 내 venv & 파이썬 코드 같이 수행 
 -- airflow내 pythonVirtualenvOperator가 따로 있지만 해당 함수는 특정 env 수행이 아닌 subprocess느낌으로하는 내용인듯
 - 2. bashoperator에서 sh 뒤에 space 한개필요.. https://cwiki.apache.org/confluence/pages/viewpage.action?pageId=62694614
