📝<br><i>
just a simple aws exercise using ec2, s3, dynamodb, flask <br>
blog webpage (list,upload,delete)</i>

## step
- create EC2 instance (region: us-west-2 / custom TCP port 5000), associate with Elastic IP
- create s3 bucket 

*bucket should be public => edit bucket policy
```
{
    "Version": "2008-10-17",
    "Id": "Policy1397632521960",
    "Statement": [
        {
            "Sid": "Stmt1397633323327",
            "Effect": "Allow",
            "Principal": {
                "AWS": "*"
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::bucketname/*"
        }
    ]
}
```
- create dynamo db table 
- connect server, download files
- on EC2 run command (nohup) flask run --host=0.0.0.0
- go to url: elastic ip:5000

