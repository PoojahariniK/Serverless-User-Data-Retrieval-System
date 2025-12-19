# Serverless-User-Data-Retrieval-System
A serverless, cloud-native web application built using AWS managed services that allows users to retrieve stored user information (name and email) by entering a User ID. The system is designed using a three-tier architecture for scalability, security, and maintainability.

## 📑 Table of Contents
- [Architecture Diagram]
- [Project Overview]
- [Tech Stack]
- [End-to-End Workflow]
- [Implementation Steps]
- [Security Considerations]
- [Key Features]
- [Learning Outcomes]
- [Screenshots]
- [Author]

Architecture Diagram
<img width="760" height="510" alt="image" src="https://github.com/user-attachments/assets/bf2e4269-8750-49f8-a81b-9ec0b41c9f75" />


Project Overview

This project demonstrates how to build and deploy a fully serverless three-tier web application using AWS managed services.

1.The frontend is developed using HTML, CSS, and JavaScript, hosted in an Amazon S3 bucket, and delivered securely through Amazon CloudFront (Presentation Layer).

2.The application (logic) layer is implemented using AWS Lambda, which is invoked through Amazon API Gateway.

3.The data layer uses Amazon DynamoDB to store and retrieve user information.

Users interact with a simple web UI by entering a User ID.
The frontend sends a request to an API Gateway endpoint, which triggers a Lambda function to fetch user data from DynamoDB and return it to the UI.

Tech Stack

- **Frontend:** HTML, CSS, JavaScript  
- **Hosting:** AWS S3, CloudFront  
- **API:** AWS API Gateway  
- **Compute:** AWS Lambda (Python)  
- **Database:** AWS DynamoDB  
- **Security:** IAM Roles, OAC

End-to-End Workflow

1.User accesses the application using the CloudFront distribution URL
2.Static frontend files are served from S3 via CloudFront
3.User enters a User ID
4.Frontend JavaScript sends a GET request to API Gateway
5.API Gateway invokes the Lambda function
6.Lambda retrieves user data from DynamoDB
7.Response is returned and displayed on the UI

Step-by-Step Implementation

Step 1: Frontend Development

1.Created a simple HTML, CSS, and JavaScript interface for user interaction

2.Implemented an input field to accept User ID

3.Used JavaScript (script.js) to call the backend API and display results dynamically

<img width="862" height="879" alt="image" src="https://github.com/user-attachments/assets/abdea0ae-66e1-42bc-9d1a-a17d0477a189" />

Step 2: DynamoDB Setup (Data Layer)

Created a DynamoDB table named UserData

Table schema:

user_id (Partition Key – String)
name
email

Inserted sample records for testing

Sample Data:

user_id	name	email
101	Poojaharini K	pooja@gmail.com

102	Harini	harini@gmail.com

103	Vini	vini@gmail.com

<img width="940" height="390" alt="image" src="https://github.com/user-attachments/assets/18be1f4c-e89e-450f-9934-c28e7087fd3f" />

Step 3: AWS Lambda Function (Logic Layer)

1.Created a Lambda function using Python

2.Implemented logic to:

i.Read user_id from request parameters

ii.Fetch corresponding data from DynamoDB

iii.Return the response in JSON format

3.Tested the function using Lambda test events

<img width="940" height="378" alt="image" src="https://github.com/user-attachments/assets/76085e67-6642-44f9-b96d-a7663aa39ad6" />

<img width="611" height="124" alt="image" src="https://github.com/user-attachments/assets/6717b9f1-bf50-4b0a-bebd-34dfcde5cddb" />

<img width="940" height="353" alt="image" src="https://github.com/user-attachments/assets/4d72c46e-b08d-4935-ae2c-4f400a5d9d62" />

Step 4: IAM Role Configuration (Security)

1.Created a dedicated IAM role for the Lambda function

2.Attached read-only permissions for DynamoDB (GetItem)

3.Followed least-privilege access principles

<img width="940" height="367" alt="image" src="https://github.com/user-attachments/assets/8c5b5ed7-625c-42f0-b0e0-951068ba5834" />

Step 5: API Gateway Configuration

1.Created a REST API using Amazon API Gateway

2.Configured:

i.GET method

ii.Integration with Lambda

iii.Enabled CORS

3.Deployed the API to generate a public endpoint

<img width="940" height="371" alt="image" src="https://github.com/user-attachments/assets/965cfa87-2681-4906-b9e7-8263973e2b57" />

<img width="940" height="353" alt="image" src="https://github.com/user-attachments/assets/8b7adaae-2fe4-4c1e-99a1-acf6efbeb8bf" />

Step 6: Frontend–Backend Integration

1.Copied the deployed API Gateway URL

2.Integrated it into script.js

3.Verified successful communication between frontend and backend

Step 7: S3 Hosting & CloudFront Distribution (Presentation Layer)

1.Created an S3 bucket and uploaded frontend files

2.Configured bucket permissions for CloudFront access

3.Created a CloudFront distribution

4.Mapped CloudFront to the S3 bucket

5.Configured Origin Access Control (OAC) for secure access

6.Used CloudFront domain to access the application

<img width="940" height="367" alt="image" src="https://github.com/user-attachments/assets/b55abdda-7f40-410c-91f7-e9332196f778" />

<img width="940" height="377" alt="image" src="https://github.com/user-attachments/assets/395c1bbc-d86e-420a-a255-77394c836832" />

<img width="940" height="474" alt="image" src="https://github.com/user-attachments/assets/f0ad40e0-4a5a-421d-b99f-28b7ec31d8b9" />

<img width="940" height="428" alt="image" src="https://github.com/user-attachments/assets/7259d5a5-b114-4f0f-b5c8-fe29d3d616cb" />

Security Considerations

1.Lambda function uses a restricted IAM role

2.DynamoDB access limited to read-only

3.CloudFront OAC prevents direct S3 public access

4.Backend services are not directly exposed

Key Features

1.Fully serverless architecture

2.Three-tier design (Presentation, Logic, Data)

3.Secure data access using IAM

4.Low-latency content delivery via CloudFront

5.Scalable and cost-efficient solution

Learning Outcomes

1.Designed and implemented a serverless AWS architecture.

2.Built REST APIs using API Gateway & Lambda.

3.Worked with NoSQL data modeling (DynamoDB).

4.Applied IAM security best practices.

5.Created S3 bucket, uploaded files and managed ACL for the objects.

6.Hosted and delivered static web content using CloudFront.

Author

Poojaharini K
