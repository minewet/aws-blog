import boto3
import time, datetime

dynamodb = boto3.resource('dynamodb', region_name='us-west-2') # 리전 설정 안하면 오류났음
s3 = boto3.client('s3')

# when submit post, upload contents to dynamoDB - if there is image, upload image s3 bucket and put the image url to database
def upload_post(file_name, title, text, BUCKET, TABLE):
    table = dynamodb.Table(TABLE) # dynamoDB table of for blog post
    time = datetime.datetime.now().strftime("%c") # get current date time

    if file_name is None :  
        img_url='<empty>'
    else : # if there is image, upload to s3 bucket.
        newname = time.replace(' ', '')+"."+file_name.split('.')[1] # set filename to datetime, and remove blanks - 공백 넣으면 url에 공백이 넣어지는데 그러면 html에서 파일을 이상하게 읽어옴
        s3.upload_file(file_name, BUCKET, newname) # upload image to s3bucket
        location = s3.get_bucket_location(Bucket=BUCKET)['LocationConstraint']
        img_url = f'https://{BUCKET}.s3.{location}.amazonaws.com/{newname}' # get image url

    item = {'id': time, 'date':time, 'title': title, 'text': text, 'picture': img_url} 
    table.put_item(Item=item) # put item(data) for new post to database
    return

# to show recorded posts, get all post datas from database(dynamoDB)
def get_items(TABLE):
    table = dynamodb.Table(TABLE)
    scaned = table.scan() # get all datas from database - return type is dictionary. on 'Item', there is all items as a type of dictionary of each attribute
    # get all datas of each attribute of all items
    dates = list(m['date'] for m in scaned['Items']) # date
    titles = list(m['title'] for m in scaned['Items']) # title
    urls = list(m['picture'] for m in scaned['Items']) # image(url)
    texts = list(m['text'] for m in scaned['Items']) # main text

    return dates, titles, urls, texts


# when press delete button, delete that item from database(dynamoDB) and delete image of post from s3 bucket
def delete_post(key, BUCKET, TABLE):
    table = dynamodb.Table(TABLE)

    img = table.get_item(Key={'id':key}, AttributesToGet=['picture'])['Item']['picture']
    if img != '<empty>': # if there was no image, pass
        img = img.replace(" ","").split('/')[-1]    # get image's s3 bucket key
        s3.delete_object(Bucket=BUCKET, Key=img)    # delete image from bucket

    table.delete_item(Key={'id': key})  # delete item of post
    return
