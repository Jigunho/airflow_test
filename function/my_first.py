from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

import first
import second
import third1
import third2

def tt1():
  print('a')

def tt2():
  print('b')

args = {'owner': 'geonho', 'start_date': days_ago(n=1)}

dag  = DAG(dag_id='geonho_dagg',
           default_args=args,
           schedule_interval='@daily')

# t1 = BashOperator(task_id='print_date',
#                   bash_command='date',
#                   dag=dag)

# t2 = BashOperator(task_id='sleep',
#                   bash_command='sleep 3',
#                   dag=dag)

# t3 = BashOperator(task_id='print_whoami',
#                   bash_command='whoami',
#                   dag=dag)


d1 = PythonOperator(task_id='task_11',
                    provide_context=True,
                    python_callable=first.main,
                    # op_kwargs={'fruit_name': 'apple'},
                    dag=dag)

d2 = PythonOperator(task_id='task_22',
                    provide_context=True,
                    python_callable=second.main,
                    # op_kwargs={'fruit_name': 'apple'},
                    dag=dag)

d3 = PythonOperator(task_id='task_33',
                    provide_context=True,
                    python_callable=third1.main,
                    # op_kwargs={'fruit_name': 'apple'},
                    dag=dag)

d1 >> d2 >> d3
# t1 >> t2 >> t3
