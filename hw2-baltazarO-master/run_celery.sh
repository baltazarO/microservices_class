#!/bin/bash
if [ -z $1 ]
then
   export MIC_URL=fathomless-harbor-78697.herokuapp.com
elif [ $1 == "local" ]
then
   export MIC_URL=0.0.0.0:5001
else
   export MIC_URL=fathomless-harbor-78697.herokuapp.com
fi

celery worker -A app.cel -l info
