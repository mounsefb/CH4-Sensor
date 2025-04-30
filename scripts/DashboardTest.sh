Methane Sensor :

i=1
while true; do
  j=$(( RANDOM % 50+20))
  k=$(( RANDOM % 100 ))
  curl -v -X POST http://thingsboard.cloud/api/v1/Z9LSCp1BxSyucZzW1pIx/telemetry \
       --header "Content-Type: application/json" \
       --data "{\"methaneLevel\":$i; temperature:$j; humidity:$k}"
  sleep 5
  i=$((i + 1))
done


while true; do
  i=$(( RANDOM % 901 + 100 ))
  mosquitto_pub -d -q 1 -h mqtt.thingsboard.cloud -p 1883 -t v1/devices/me/telemetry -u "0dawhgomqi147fqq0qz2" -m "{methaneLevel:$i}"
  mosquitto_pub -d -q 1 -h mqtt.thingsboard.cloud -p 1883 -t v1/devices/me/telemetry -u "Z9LSCp1BxSyucZzW1pIx" -m "{methaneLevel:$((i+100))}"
  sleep 5
done

Battery Charger :

mosquitto_pub -d -q 1 -h mqtt.thingsboard.cloud -p 1883 -t v1/devices/me/telemetry -u "r0Ygrn0kN1URtF3e3VZ8" -m "{batteryLevel:25}"

curl -v -X POST http://thingsboard.cloud/api/v1/r0Ygrn0kN1URtF3e3VZ8/telemetry 
	--header Content-Type:application/json 
	--data "{batteryLevel:10}"
	
	
GPS :
mosquitto_pub -d -q 1 -h mqtt.thingsboard.cloud -p 1883 -t v1/devices/me/telemetry -u "19baFdrIApCGDnU95OwT" -m "{latitude:20; longitude:105}"
mosquitto_pub -d -q 1 -h mqtt.thingsboard.cloud -p 1883 -t v1/devices/me/telemetry -u "QC2IMzAvHT8pZJhgSUuk" -m "{latitude:20; longitude:105}"



temperature - humidity - time each 5 seconds



Figure 11 : Structure of a MQTT packet
Figure 12 : Connection routine and architecture of a MQTT network
Figure 13 : Example of a MQTT transmission
Figure 14 : User Interface
Figure 15 : Admin Interface
Figure 16 : Equipment and above sight of the box
Figure 17 : Isolation box
Figure 18 : Collected data



