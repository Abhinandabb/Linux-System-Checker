# Linux System Health Reporter

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Bash](https://img.shields.io/badge/bash-%234EAA25.svg?style=for-the-badge&logo=gnu-bash&logoColor=white)
![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white)

A lightweight Python-based monitoring tool that tracks system resource usage and sends automated alerts via Webhooks when thresholds are exceeded.

## Features
- **Real-time Monitoring**: Tracks CPU, RAM, and Disk usage percentages.
- **Automated Alerts**: Sends instant Discord/Slack notifications if usage exceeds 80%.
- **Persistent Logging**: Maintains a timestamped history of system health in a log file.
- **Task Scheduling**: Uses Linux Cron for fully automated background execution.

## Installation
1. Clone this repository:
   `git clone https://github.com/Nawaf1208/health_reporter.git`
2. Install dependencies:
   `pip install psutil requests`
3. Update the `webhook_url` in `health_reporter.py` with your own link.

## Usage
To run the reporter manually:
`bash run_health_check.sh`
