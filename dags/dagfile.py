from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

def tt1():
  print('a')

def tt2():
  print('b')

args = {'owner': 'geonho', 'start_date': days_ago(n=1)}

dag  = DAG(dag_id='dagfile',
           default_args=args,
           schedule_interval='@daily')

d1 = PythonOperator(task_id='task_111',
                    provide_context=True,
                    python_callable=tt1,
                    # op_kwargs={'fruit_name': 'apple'},
                    dag=dag)
d2 = PythonOperator(task_id='task_222',
                    provide_context=True,
                    python_callable=tt2,
                    # op_kwargs={'fruit_name': 'apple'},
                    dag=dag)

d1 >> d2
