#!/bin/bash

array=($(echo $1 | tr ',' '\n'))

for i in "${array[@]}"; do
    ssh $i 'test $(awk 'print tolower($0)' <<< $(nodetool netstats | grep Mode)) = "normal" && nohup $(nodetool cleanup) > /dev/null 2>&1 &'
done
