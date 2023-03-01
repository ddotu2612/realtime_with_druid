from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime
from airflow.utils import timezone

######################### Config DAG
default_args = {'owner': 'airflow',
                'start_date': timezone.datetime(2023, 2, 28, 16, 30),
                }

dag = DAG("trigger_producer",
            schedule_interval='30 16 * * *',
            default_args=default_args,
            is_paused_upon_creation=False, ## Dag auto active
            )


task_start = BashOperator(task_id='start', bash_command='date', dag=dag)
task_submit = BashOperator(task_id='trigger_submit', bash_command='python /airflow/test/submitSupervisor.py', dag=dag)
task_Trigger_py = BashOperator(task_id='trigger_producer', bash_command='python /airflow/test/load.py', dag=dag)

task_start >> task_submit >> task_Trigger_py 