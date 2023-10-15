# GenericAPI

### BUILD CMAKE ###
mkdir build && cd build && cmake .. && cmake --build . --target generate_models

docker compose
docker jenkins
docker service
docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=YourPasswordHere" -p 1433:1433 --name sqlserver-container -d mcr.microsoft.com/mssql/server:2019-latest
sudo docker run --cap-add SYS_PTRACE -e 'ACCEPT_EULA=1' -e 'MSSQL_SA_PASSWORD=password@1234' -p 1433:1433 --name test -d mcr.microsoft.com/azure-sql-edge


docker run --platform=linux/arm/v7 --rm -it -p 15672:15672 -p 5672:5672 rabbitmq:3-management

docker run -d -p 3100:3100 --name loki -v /path/to/loki-config:/etc/loki grafana/loki:latest -config.file=/etc/loki/local-config.yaml
docker run -d -p 3100:3100 --name loki grafana/loki:latest

docker run -d -p 3000:3000 --name grafana -e "GF_AUTH_ANONYMOUS_ENABLED=true" -e "GF_AUTH_ANONYMOUS_ORG_NAME=MainOrg" -e "GF_USERS_ALLOW_SIGN_UP=false" -e "GF_SECURITY_ADMIN_USER=admin" -e "GF_SECURITY_ADMIN_PASSWORD=admin_password" --link loki:loki grafana/grafana:latest
docker run -d -p 3000:3000 --name grafana -e "GF_AUTH_ANONYMOUS_ENABLED=true" -e "GF_AUTH_ANONYMOUS_ORG_NAME=MainOrg" grafana/grafana:latest
