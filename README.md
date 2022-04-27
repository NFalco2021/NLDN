# NLDN
This project automates the collection of NLDN data using Vaisala's Lightning Exporter API.

## Running the script
This script is designed to be ran automatically as a cronjob. You can run the script manually, as is done in the run.py script, by calling ```python path/to/vaisala.py```.

### Requirement
You will need access to Vaisala's Lightning Exporter API in order for this script to work.

You will also need to update config.py to fit your specific system (i.e. updating the location to write the data for your specific system) 


### API Documentation
[Vaisala's Lightning Integrator](https://ltg.vaisala.com/realtime/merge/webjars/swagger-ui/index.html)

## Notes
### Date Ranges
Start:  02/08/2022
Stop:   05/08/2022

### Coverage Area
Using two coordinates (WGS84) in decimal degrees we define the bounded area
Lower Latitude:     24
Lower Longitude:    -126
Upper Latitude:     50
Upper Longitude:    -65

### Queryable Values

#### A Sample API Call
```jsonpath
https://ltg.vaisala.com/realtime/merge/api/v1/ltgs/bbox?start=2022-03-03T10%3A00%3A00Z&end=2022-03-03T16%3A00%3A00Z&left=-126&bottom=24&right=-65&top=50&amplitudeRanges=15..80&cloud=false&inclEllipse=80&fields=analysis&fields=research&fields=ldi_sdp&page=0&size=10
```

#### API Call Broken Down
The url of the API front-end:
```jsonpath
https://ltg.vaisala.com/realtime/merge/api/v1/ltgs/bbox?
```

The '?' at the end signifies that what follows will be key/value pairs.
The '&' after the values indicate a new key will follow.

Not every key/value pair is necessary to execute an API call. Refer to the APIs documentation to learn more.
[For a more through explanation, please visit Vaisala's API Documentation](https://ltg.vaisala.com/realtime/merge/webjars/swagger-ui/index.html)

<table>
 <tr>
    <td><b style="font-size:15px">Keys/Encoded Values</b></td>
    <td><b style="font-size:15px">Decoded Values</b></td>
 </tr>
 <tr>
    <td>
<pre>
start=2022-03-03T10%3A00%3A00Z& 
end=2022-03-03T16%3A00%3A00Z&
left=-126&
bottom=24&
right=-65&
top=50&
amplitudeRanges=15..80&
cloud=false&
inclEllipse=80&
fields=analysis&
fields=research&
fields=ldi_sdp&
page=0&
size=10
</pre>
    </td>
    <td>
<pre>
2022-03-03T10:00:00Z 
2022-03-03T16:00:00Z
-126
24
-65
50
15..80
false
80
analysis
research
ldi_sdp
0
10
</pre>
    </td>

 </tr>
</table>



Note that URL encoding (Percent encoding) is used for some characters.
[Learn more here.](https://en.wikipedia.org/wiki/Percent-encoding)



