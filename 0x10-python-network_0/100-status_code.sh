#!/bin/bash
# displays only the status code of http response
curl -s -o /dev/null -w "%{http_code}" "$1"
