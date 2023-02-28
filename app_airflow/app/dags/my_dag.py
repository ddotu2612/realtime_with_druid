from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

######################### Config DAG
default_args = {'owner': 'airflow',
                'start_date': datetime(2023, 2, 28),
                }

dag = DAG("trigger_producer",
            schedule_interval=None,
            default_args=default_args,
            is_paused_upon_creation=False, ## Dag auto active
            )

with dag:
	task_start = BashOperator(task_id='start', bash_command='date')
	task_Trigger_py = BashOperator(task_id='trigger_producer', bash_command='python /airflow/test/load.py')


	task_start >> task_Trigger_py