docker login code.exaas.bosch.com:6000

docker pull alpine
docker tag alpine code.exaas.bosch.com:6000/xelerator/projects/api/tools/traffic-simulator
docker push code.exaas.bosch.com:6000/xelerator/projects/api/tools/traffic-simulator