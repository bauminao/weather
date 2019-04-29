# Dummy-Sensor

* Small server that simulates a hardware sensor.

If called it returns data as json.

Later it will expect to get an answer and to resend updated data until wokrflow is finished completely.

Basically it return data as following scheme: 

  * sensorid -- the raw id of a sensor; should be unique in network.
  * sensortype -- defines which kind of data is supplied {"temp"}
  * databuffer -- contains the data values. I defined it as array to have less "online time"
  *  * ID 
  *  * * "T" : &lt;temperature&gt;
  *  * * "state" : {P,S,N}

  N : New Value <br>
  S : **S**ending this dataset now <br>
  P : Sent and **P**rocessed data value. <br>


