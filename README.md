# CipherScan

## Overview
CipherScan Scanner is a Python-based application designed to scan AWS S3 buckets for security vulnerabilities, such as:

- Detecting sensitive data (e.g., credit card numbers)
- Identifying unencrypted files
- Analyzing IAM policies for misconfigurations

This tool is equipped with a Tkinter-based graphical user interface (GUI) for ease of use and supports email alerts for critical issues.

---

## Features

### S3 Bucket Scanning
Scans specific S3 buckets for sensitive data and unencrypted files.  
Supports the following buckets:
- gendatavaultbucket (General Data)
- logsvaultbucket (Logs)
- sensitivevaultbucket (Sensitive Data)

### IAM Policy Analysis
Detects insecure policies, such as:
- Wildcard permissions (s3:*)
- Overly broad resource access

### Alerts
Sends alerts via email for sensitive issues detected in `sensitivevaultbucket`.

### Reports
Saves all findings into a SQLite database (`compliance_reports.db`) for audit and review.

### User-Friendly GUI
- Dropdown to select specific buckets for scanning
- Displays detailed results in a scrollable output box

---

## File Structure
```
DATAVAULT/
│
├── alerts.py              # Handles console and email alerts
├── gui.py                 # Manages the Tkinter GUI
├── iam_policy_analyzer.py # Contains IAM policy analyzer logic
├── main.py                # Entry point to launch the application
├── reports.py             # Manages storing results in SQLite
├── s3_scanner.py          # Scans S3 buckets for issues
└── README.md              # Project documentation
```

---

## Requirements

### System Requirements
- Python 3.8 or higher
- AWS CLI configured with credentials

### Python Dependencies
Install the required Python packages using pip:
```bash
pip install boto3
pip install tk
```

---

## Setup

### Step 1: Configure AWS CLI
Ensure that you have AWS credentials configured.  
Run the following command and provide your Access Key, Secret Key, and Region:
```bash
aws configure
```

### Step 2: Clone the Repository
Clone this project to your local system:
```bash
git clone https://github.com/Afi223/CipherScan.git
cd CipherScan
```

### Step 3: Install Dependencies
Install the necessary Python libraries:
```bash
pip install -r requirements.txt
```

### Step 4: Update Email Configuration
Edit `alerts.py` and set the following parameters:
```python
email_sender: Your email address
email_password: Your email password or app-specific password
email_receiver: Recipient email address
```

---

## Usage

### Run the Application
To start the GUI application, execute the following command:
```bash
python main.py
```

### S3 Bucket Scanning
- Select a bucket from the dropdown menu:
  - General Data: Scans gendatavaultbucket
  - Logs: Scans logsvaultbucket
  - Sensitive Data: Scans sensitivevaultbucket
- Click "Scan Bucket" to begin scanning
- Results will be displayed in the output box

### Analyze IAM Policy
- Click "Analyze IAM Policy" to upload a JSON file containing your IAM policy
- Results will display any detected issues, such as wildcard permissions

### Alerts
- Alerts are sent via email for issues detected in `sensitivevaultbucket`

---

## How It Works

### S3 Scanner
- Uses boto3 to connect to AWS S3 and list objects in the bucket
- Reads file contents and uses Regex to detect sensitive patterns (e.g., credit card numbers)
- Checks for the absence of encryption metadata

### IAM Policy Analyzer
- Parses a JSON policy file
- Detects insecure configurations like wildcard permissions and overly broad resource access

### Report Storage
- Results are stored in `compliance_reports.db` under a `reports` table

### Alerts
- Prints alerts to the console
- Sends email notifications for critical issues

---

## Examples

### S3 Scanner Output
For `sensitivevaultbucket`:
```
Scanning sensitivevaultbucket...
Sensitive data found in file: user_data_01.txt
Unencrypted file detected: user_logs_02.txt
```

### IAM Policy Analysis Output
For a policy file:
```
Policy Issues Found:
Wildcard permission detected: s3:*
Overly broad resource access detected
```

---

## Contributing
Feel free to fork this project and submit pull requests.  
If you encounter issues, report them via GitHub Issues.
