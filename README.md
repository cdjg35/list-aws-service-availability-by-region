[![Build Status](https://img.shields.io/travis/AntiPhotonltd/list-aws-service-availability-by-region/master.svg)](https://travis-ci.org/AntiPhotonltd/list-aws-service-availability-by-region)
[![Software License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE.md)
[![Release](https://img.shields.io/github/release/AntiPhotonltd/list-aws-service-availability-by-region.svg)](https://github.com/AntiPhotonltd/list-aws-service-availability-by-region/releases/latest)
[![Github commits (since latest release)](https://img.shields.io/github/commits-since/AntiPhotonltd/list-aws-service-availability-by-region/latest.svg)](https://github.com/AntiPhotonltd/list-aws-service-availability-by-region/commits)
[![GitHub repo size in bytes](https://img.shields.io/github/repo-size/AntiPhotonltd/list-aws-service-availability-by-region.svg)](https://github.com/AntiPhotonltd/list-aws-service-availability-by-region)
[![GitHub contributors](https://img.shields.io/github/contributors/AntiPhotonltd/list-aws-service-availability-by-region.svg)](https://github.com/AntiPhotonltd/list-aws-service-availability-by-region)

List AWS Service Availability by Region
=========

A python script to get a list of all services and theie availability per region.

## Simple Usage

```
./list-aws-service-availability-by-region.py
```

## Command Line Options

```

usage: list-aws-service-availability-by-region.py [-h] [-e EXCLUDE_REGION]
                                                  [-n] [-s SEARCH_REGION]

List AWS Service Availability by Region

optional arguments:
  -h, --help            show this help message and exit
  -e EXCLUDE_REGION, --exclude-region EXCLUDE_REGION
                        The region to exclude from the results
  -n, --no-results      Do not show the final table of results
  -s SEARCH_REGION, --search-region SEARCH_REGION
                        The region to search the results for

```

## Example output

This is an example of the first 5 regions.

```
+-------------------------------------------------------+------+--------+---------------------+----------+
|                   Northern Virginia                   | Ohio | Oregon | Northern California | Montreal |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                   Alexa for Business                  |  Y   |   N    |          N          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                   Amazon API Gateway                  |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                  Amazon AppStream 2.0                 |  Y   |   N    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                     Amazon Athena                     |  Y   |   Y    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|            Amazon Aurora - MySQL-compatible           |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|         Amazon Aurora - PostgreSQL-compatible         |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                      Amazon Chime                     |  Y   |   N    |          N          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                 Amazon Cloud Directory                |  Y   |   Y    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                   Amazon CloudSearch                  |  Y   |   N    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                   Amazon CloudWatch                   |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                Amazon CloudWatch Events               |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                 Amazon CloudWatch Logs                |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                     Amazon Cognito                    |  Y   |   Y    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                   Amazon Comprehend                   |  Y   |   Y    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|               Amazon Comprehend Medical               |  Y   |   Y    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                     Amazon Connect                    |  Y   |   N    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                    Amazon DeepLens                    |  Y   |   N    |          N          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                    Amazon DynamoDB                    |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                Amazon EC2 Auto Scaling                |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|        Amazon Elastic Container Registry (ECR)        |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|         Amazon Elastic Container Service (ECS)        |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
| Amazon Elastic Container Service for Kubernetes (EKS) |  Y   |   Y    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                   Amazon ElastiCache                  |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|            Amazon Elastic Block Store (EBS)           |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|           Amazon Elastic Compute Cloud (EC2)          |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|    Amazon Elastic Compute Cloud (EC2) A1 Instances    |  Y   |   Y    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|    Amazon Elastic Compute Cloud (EC2) C5n Instances   |  Y   |   Y    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|            Amazon Elastic File System (EFS)           |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                Amazon Elastic Graphics                |  Y   |   Y    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                Amazon Elastic Inference               |  Y   |   Y    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                Amazon Elastic MapReduce               |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|              Amazon Elasticsearch Service             |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|               Amazon Elastic Transcoder               |  Y   |   N    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                    Amazon FreeRTOS                    |  Y   |   Y    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                       Amazon FSx                      |  Y   |   Y    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                    Amazon GameLift                    |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                     Amazon Glacier                    |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                    Amazon GuardDuty                   |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                    Amazon Inspector                   |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|             Amazon Kinesis Data Analytics             |  Y   |   Y    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|              Amazon Kinesis Data Firehose             |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|              Amazon Kinesis Data Streams              |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|              Amazon Kinesis Video Streams             |  Y   |   N    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                       Amazon Lex                      |  Y   |   N    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                    Amazon Lightsail                   |  Y   |   Y    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                Amazon Machine Learning                |  Y   |   N    |          N          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                      Amazon Macie                     |  Y   |   N    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|               Amazon Managed Blockchain               |  Y   |   N    |          N          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                Amazon Mobile Analytics                |  Y   |   N    |          N          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                       Amazon MQ                       |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                     Amazon Neptune                    |  Y   |   Y    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                    Amazon Pinpoint                    |  Y   |   N    |          N          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                      Amazon Polly                     |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                   Amazon QuickSight                   |  Y   |   Y    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                    Amazon Redshift                    |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                Amazon Rekognition Image               |  Y   |   Y    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                Amazon Rekognition Video               |  Y   |   Y    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|        Amazon Relational Database Service (RDS)       |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                    Amazon SageMaker                   |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|             Amazon SageMaker Ground Truth             |  Y   |   Y    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                  Amazon SageMaker Neo                 |  Y   |   Y    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                    Amazon SimpleDB                    |  Y   |   N    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|           Amazon Simple Email Service (SES)           |  Y   |   N    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|        Amazon Simple Notification Service (SNS)       |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|           Amazon Simple Queue Service (SQS)           |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|           Amazon Simple Storage Service (S3)          |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|          Amazon Simple Workflow Service (SWF)         |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                    Amazon Sumerian                    |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                   Amazon Transcribe                   |  Y   |   Y    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                    Amazon Translate                   |  Y   |   Y    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|           Amazon Virtual Private Cloud (VPC)          |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                    Amazon WorkDocs                    |  Y   |   N    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                    Amazon WorkMail                    |  Y   |   N    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                   Amazon WorkSpaces                   |  Y   |   N    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|         Amazon WorkSpaces Application Manager         |  Y   |   N    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|           AWS Application Discovery Service           |  N   |   N    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                      AWS AppSync                      |  Y   |   Y    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                    AWS Auto Scaling                   |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                       AWS Batch                       |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                AWS Certificate Manager                |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                     AWS Cloud Map                     |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                   AWS CloudFormation                  |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                       AWS Cloud9                      |  Y   |   Y    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                      AWS CloudHSM                     |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                  AWS CloudHSM Classic                 |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                     AWS CloudTrail                    |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                     AWS CodeBuild                     |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                     AWS CodeCommit                    |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                     AWS CodeDeploy                    |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                    AWS CodePipeline                   |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                      AWS CodeStar                     |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                       AWS Config                      |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|             AWS Database Migration Service            |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                   AWS Data Pipeline                   |  Y   |   N    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                      AWS DataSync                     |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                     AWS DeepRacer                     |  Y   |   N    |          N          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                    AWS Device Farm                    |  N   |   N    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                   AWS Direct Connect                  |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                 AWS Directory Service                 |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                 AWS Elastic Beanstalk                 |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|               AWS Elemental MediaConnect              |  Y   |   N    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|               AWS Elemental MediaConvert              |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                AWS Elemental MediaLive                |  Y   |   N    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|               AWS Elemental MediaPackage              |  Y   |   N    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                AWS Elemental MediaStore               |  Y   |   N    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|               AWS Elemental MediaTailor               |  Y   |   N    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                      AWS Fargate                      |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                  AWS Firewall Manager                 |  Y   |   N    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                 AWS Global Accelerator                |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                        AWS Glue                       |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                     AWS Greengrass                    |  Y   |   N    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                    AWS IoT 1-Click                    |  Y   |   Y    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                   AWS IoT Analytics                   |  Y   |   Y    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                      AWS IoT Core                     |  Y   |   Y    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                AWS IoT Device Defender                |  Y   |   Y    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|               AWS IoT Device Management               |  Y   |   Y    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|               AWS Key Management Service              |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                       AWS Lambda                      |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                  AWS Managed Services                 |  Y   |   N    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                    AWS Marketplace                    |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                   AWS Migration Hub                   |  N   |   N    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                     AWS Mobile Hub                    |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                  AWS OpsWorks Stacks                  |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|             AWS OpsWorks for Chef Automate            |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|           AWS OpsWorks for Puppet Enterprise          |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|             AWS Personal Health Dashboard             |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                     AWS RoboMaker                     |  Y   |   N    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                  AWS Secrets Manager                  |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                    AWS Security Hub                   |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|         AWS Serverless Application Repository         |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|              AWS Server Migration Service             |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                  AWS Service Catalog                  |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                  AWS Shield Standard                  |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                  AWS Shield Advanced                  |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                   AWS Single Sign-On                  |  Y   |   N    |          N          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                      AWS Snowball                     |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                   AWS Snowball Edge                   |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                     AWS Snowmobile                    |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                   AWS Step Functions                  |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                  AWS Storage Gateway                  |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                      AWS Support                      |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                  AWS Systems Manager                  |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                  AWS Transit Gateway                  |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                  AWS Trusted Advisor                  |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                        AWS WAF                        |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|               AWS Well-Architected Tool               |  Y   |   Y    |          Y          |    N     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                       AWS X-Ray                       |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                 Elastic Load Balancing                |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
|                    VM Import/Export                   |  Y   |   Y    |          Y          |    Y     |
+-------------------------------------------------------+------+--------+---------------------+----------+
```

## ToDo

- [ ] Search by region
- [ ] Exclude by region
- [ ] Search by service
- [ ] Exclude by service
- [ ] Make search and exclude accept comma separted lists.