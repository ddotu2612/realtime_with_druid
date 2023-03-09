# realtime_with_druid 
B1: Clone <br>
B2: Run -> docker-compose rm -f && docker-compose build && docker-compose up <br>
| Service               | URL                              | User/Password                                 |
| :-------------------: | :------------------------------: | :-------------------------------------------: |
| Druid Unified Console | http://localhost:8888/           | None                                          |
| Druid Legacy Console  | http://localhost:8081/           | None                                          |
| Superset              | http://localhost:8088/           | docker exec -it superset bash superset-init   |
| Airflow               | http://localhost:3000/           | a-airflow/app/standalone_admin_password.txt   |

# He thong alert
B1: cd > chat_bot <br>
B2: python botTelte.py -> run chatbot <br>
B3: python push_notification_bot.py -> run alert stock system <br>

# Danh gia hieu nang
B1: cd > druid <br>
    helm install druid . --namespace druid --create-namespace -> Tạo một cụm druid từ file values.yaml <br>
    Để update: thay install -> upgrade <br>
    Để forward druid: kubectl port-forward service/druid-router 8888:8888 -n druid <br>
B2: cd > kafka <br>
    helm install kafka bitnami/kafka --values=./kafka-values.yaml <br>
B3: Druid Operator install <br>
    kubectl create namespace druid-operator <br>
    git clone https://github.com/druid-io/druid-operator.git <br>
    cd druid-operator/ <br>
    helm -n druid-operator install cluster-druid-operator ./chart <br>
    
B4: Installing Kube Prometheus Stack <br>
    kubectl create ns monitoring <br>
    helm -n monitoring install kube-prometheus-stack prometheus-community/kube-prometheus-stack <br>
    Để forward Prometheus: kubectl -n monitoring port-forward svc/kube-prometheus-stack-prometheus 9090:9090 <br>
    Để forward Grafana: kubectl -n monitoring port-forward svc/kube-prometheus-stack-grafana 8080:80 <br>

B5: Running Druid Exporter <br>
    git clone https://github.com/opstree/druid-exporter.git <br>
    cd druid-exporter/ <br>
    helm -n monitoring install druid-exporter ./helm/ --set druidURL="http://druid-router.druid.svc.cluster.local:8888" --set druidExporterPort="8080" --set logLevel="debug" --set logFormat="text" --set serviceMonitor.enabled=true --set serviceMonitor.namespace="monitoring" <br>

B6: Chạy chương trình producer kafka in K8s <br>
    cd > app <br>
    kubectl apply -f pod.yaml <br>
B6: Xem dịch vụ và giá trị metric: <br>
    sum(druid_emitted_metrics) by (exported_service, metric_name) trên localhost:9090 của Prometheus <br>




    
    


