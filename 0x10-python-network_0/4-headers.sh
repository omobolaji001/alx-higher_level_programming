#!/bin/bash
# sends a GET request with HEADER variable to the given URL, and displays the reponse body
curl -sH "X-School-User-Id: 98" "$1"
