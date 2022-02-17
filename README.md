# NLDN
This project automates the collection of NLDN data using Vaisala's Lightning Exporter API.

## Running the script
This script is designed to be ran automatically as a cronjob. You can run the script manually, as is done in the run.py script, by calling ```python path/to/vaisala.py```.

### Requirement
You will need access to Vaisala's Lightning Exporter API in order for this script to work.

You will also need to update config.py to fit your specific system (i.e. updating the location to write the data for your specific system) 

#### Example API call
https://ltg.vaisala.com/realtime/merge/api/v1/ltgs/radius?start=2021-06-03T20%3A32%3A18Z&end=2021-06-03T21%3A48%3A04Z&longitude=-94.2&latitude=34.6&radius=10000&amplitudeRanges=15..80&cloud=true&inclEllipse=99&fields=analysis&fields=research&fields=ldi_sdp&page=0&size=20

#### API Documentation
https://ltg.vaisala.com/realtime/merge/webjars/swagger-ui/index.html?configUrl=/realtime/merge/v3/api-docs/swagger-config