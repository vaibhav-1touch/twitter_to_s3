# twitter_to_s3

<b>Load the connector in confluent</b><br>
confluent local load tweets -- -d /path/to/file/s3connector.json<br>

<b>Curl is to check tweets connector is loaded</b>
<br>
curl localhost:8083/connectors
<br>

tweet.py will start the producer and upload to s3.
