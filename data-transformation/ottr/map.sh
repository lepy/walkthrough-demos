#!/bin/bash
# Usage:
# - run in the directory where this script is located
# - supply the ottr data and template files
# e.g. sh map.sh tensile-template.stottr tensile-data.stottr

TEMPLATE_FILE=$1
DATA_FILE=$2

if [ ! -f lutra-v0.6.20.jar ]; then
    wget "https://ottr.xyz/downloads/lutra/lutra-v0.6.20.jar"
fi

java -jar lutra-v0.6.20.jar --mode expand --library ${TEMPLATE_FILE} --libraryFormat stottr --fetchMissing --inputFormat stottr ${DATA_FILE} 
