#!/bin/bash
# Set the end time for the script to run for 5 minutes
time=0
end_time=$((time + 30))
logfile=/tmp/log_`date +%d%m%Y`
 
rm -f $logfile
 
while [ $time -lt $end_time ]; do
    echo "$(date '+%Y-%m-%d %H:%M:%S') - The script is running..." >> $logfile
    sleep 5
    echo $time
    time=$((time + 5))
done
 
echo "Script completed successfully!"
