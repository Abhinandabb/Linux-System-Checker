#!/bin/bash

cd ~/health_reporter

/usr/bin/python3 health_reporter.py >> health_logs.txt 2>&1

