
![44 230 170 14_5000_](https://user-images.githubusercontent.com/71055964/197862792-98751a65-09df-41dd-9ab2-92d4b62338a9.png)

📝<br><i>
just a simple aws exercise using ec2, s3, dynamodb, flask <br>
blog webpage (list,upload,delete)</i>

## How to Run
- create EC2 instance (region: us-west-2 / custom TCP port 5000), associate with Elastic IP
- create s3 bucket <i>*name : "1971036-blogbucket"</i>

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
            "Resource": "arn:aws:s3:::1971036-blogbucket/*"
        }
    ]
}
```
- create dynamo db table <i>*name : "blogTable"</i>
- connect server, download files
- on EC2 run command (nohup) flask run --host=0.0.0.0
- go to url: elastic ip:5000
