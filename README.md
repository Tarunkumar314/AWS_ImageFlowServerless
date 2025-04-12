# **Serverless Image Upload and Processing System on AWS**

This project implements a serverless image upload and processing system on AWS. It enables users to upload images via an API endpoint, processes these images (resizes them), and stores metadata in a DynamoDB table. The processed images are saved back to the S3 bucket in a separate directory.

---

## **Features**

- **AWS S3**: Stores uploaded and processed images.
- **AWS Lambda**: Processes images (e.g., resizing) using a Lambda function triggered upon image upload.
- **AWS API Gateway**: Provides an API endpoint to upload images to S3.
- **AWS DynamoDB**: Stores metadata about each uploaded image, such as URL, size, and upload time.

---

## **Architecture**

The system operates in a serverless architecture using AWS Free Tier services:

- **API Gateway** exposes an endpoint for uploading images.
- **S3 Bucket** receives the images.
- **Lambda Function** resizes and processes images when they are uploaded to S3.
- **DynamoDB** stores metadata (URL, size, timestamp) for each image.

---

## **Setup Instructions**

### **_Prerequisites_**

- **AWS Free Tier account** with access to S3, Lambda, API Gateway, and DynamoDB.
- _Basic knowledge of AWS services and AWS Management Console._
- **Python or Node.js environment** for writing Lambda function code.

---

### **Steps to Set Up**

#### **Step 1: Create the S3 Bucket**

1. Go to the **S3 Console** and create a bucket named `my-image-processing-bucket`.
2. _Enable versioning and set lifecycle rules as needed for cost optimization._

---

#### **Step 2: Create the Lambda Function for Image Processing**

1. Go to **Lambda Console** and create a function named `ImageProcessingFunction`.
2. Choose **Python 3.8** (or **Node.js 14.x**) as the runtime.
3. **Write your Lambda function code accordingly.**

---

#### **Step 3: Set Up API Gateway for Image Uploads**

1. Go to **API Gateway Console** and create a new REST API named `ImageUploadAPI`.
2. Add a **POST method** under a resource (e.g., `/upload`) to handle image uploads.
3. **Integrate this method with S3 PutObject** and specify the bucket’s ARN.

---

#### **Step 4: Create DynamoDB Table for Metadata Storage**

1. Go to **DynamoDB Console** and create a table named `ImageMetadata`.
2. Set `ImageID` as the partition key of type `String`.

---

#### **Step 5: Assign IAM Roles and Permissions**

1. Attach the **AmazonS3FullAccess** policy to your Lambda function's role.
2. Attach the **AmazonDynamoDBFullAccess** policy to allow DynamoDB interactions.
3. Grant **API Gateway** permission to upload files to S3.

---

#### **Step 6: Deploy and Test the System**

1. Deploy your API in **API Gateway** and obtain the **Invoke URL**.
2. Use a REST client (e.g., Postman) to upload an image via the API endpoint.
3. Check the S3 bucket for the uploaded and processed images and verify DynamoDB entries for metadata.

---

## **Repository Structure**

```plaintext
|-- lambda_function.py          # Lambda function code
|-- api_gateway_config.json     # API Gateway configuration (optional)
|-- cloudformation_template.yaml # CloudFormation template to set up the architecture (optional)

```
---

## **Usage**

- **Upload an Image**: Send a `POST` request with an image file to the API Gateway endpoint.
- **Check Processed Image**: Processed images will appear in the `processed/` folder in the S3 bucket.
- **View Metadata**: Check the DynamoDB table for metadata on uploaded images.

---
