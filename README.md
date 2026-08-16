<img width="1185" height="645" alt="image" src="https://github.com/user-attachments/assets/419c94a4-8038-4bd1-80a8-ca72d166fb9c" /># Terraform-project6-serverless-api-lambda-dynamodb
Student Management Web Application

Project Overview
Here is a quick breakdown of your Serverless Student Data Management System:

1. What the Project Does
Student Record Entry: Users fill out a web form with details like Student ID, Name, Class, Age, Country, and State.

Serverless Data Storage: Submitting the form sends a POST HTTP request through API Gateway, triggering an AWS Lambda function to save the data directly into an AWS DynamoDB database.

Real-time Record Viewing: Clicking "View all Students" issues a GET request to scan DynamoDB and fetch all saved student entries, dynamically displaying them in an HTML table.

Automated Infrastructure: Infrastructure changes are automatically deployed and updated in AWS using Terraform whenever code is pushed to GitHub.

<img width="1028" height="847" alt="image" src="https://github.com/user-attachments/assets/b4cdf80b-8bf1-4b5c-b101-ae076f2689af" />






```text
📁 Project Structure
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Actions workflow
├── frontend/
│   └── index.html              # Frontend web app UI
├── modules/
│   ├── apigateway/             # Terraform API Gateway module
│   ├── dynamodb/               # Terraform DynamoDB module
│   └── lambda/                 # Terraform Lambda & IAM module
├── src/
│   └── lambda_function.py      # Python Lambda handler logic
├── main.tf                     # Root Terraform configuration
├── variables.tf                # Global input variables
├── outputs.tf                  # Global output variables
└── README.md                   # Project documentation



