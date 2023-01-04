# realtime_with_druid
B1: Clone
B2: Run -> docker-compose rm -f && docker-compose build && docker-compose up
    Service	      URL	                    User/Password \n
    Druid Unified	http://localhost:8888/	None \n
    Druid Legacy	http://localhost:8081/	None \n
    Superset	    http://localhost:8088/	docker exec -it superset bash superset-init \n
    Airflow	      http://localhost:3000/	admin - app/standalone_admin_password.txt \n
