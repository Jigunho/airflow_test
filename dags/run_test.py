from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
import sys
sys.path.insert(0,'..')
# from function.make_pdf import pdf_main
# from function.first import main

def tt1(param, **kwargs):
  print('tt1', param)
  # main()

def tt2(param, **kwargs):
  print('tt2', param)

args = {'owner': 'geonho', 'start_date': days_ago(n=1)}

dag  = DAG(dag_id='test_20210422',
           default_args=args,
           schedule_interval='@daily')

d1 = PythonOperator(task_id='task1',
                    provide_context=True,
                    python_callable=tt1,
                    op_kwargs={'param': 'apple'},
                    dag=dag)
d2 = PythonOperator(task_id='task2',
                    provide_context=True,
                    python_callable=tt2,
                    op_kwargs={'param': 'apple'},
                    dag=dag)

d3  = BashOperator(task_id='task3',
                    bash_command='source /Users/jigeonho/airflow/venv/bin/activate',
                    dag=dag)

d5  = BashOperator(task_id='task5',
                    bash_command='/bin/bash /Users/jigeonho/airflow/function/runvenv.sh ',
                    dag=dag)

# d4  = PythonOperator(task_id='task4',
#                     provide_context=True,
#                     python_callable=pdf_main,
#                     # op_kwargs={'param': 'apple'},
#                     dag=dag)

d1 >> d2 >> d3
