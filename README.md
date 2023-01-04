# realtime_with_druid
B1: Clone
B2: Run -> docker-compose rm -f && docker-compose build && docker-compose up
    Service	      URL	                    User/Password
    Druid Unified	http://localhost:8888/	None
    Druid Legacy	http://localhost:8081/	None
    Superset	    http://localhost:8088/	docker exec -it superset bash superset-init
    Airflow	      http://localhost:3000/	admin - app/standalone_admin_password.txt
