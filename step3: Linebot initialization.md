## Step 3:  First Linebot Initialization

### 3.1 About LineBots
* Line Reply/Push Messages
* Reply is free
* Push needs fees
* Rich Picture and Tex
* 互動按鈕

### 3.2 About Line Message API
<img src="img/linebot 1.jpeg">


### 3.3 LineBot Front End Framework
### 3.4 LineBot to cloud
### 3.5 LineBOt 串接第三方API


# handler - Message Event

```python
@handler.add(event=MessageEvent, message=TextMessage)
def handle_message(event):
    msg_request = MessageRequest()
    msg_request.intent = event.message.text
    msg_request.message = event.message.text
    msg_request.user_id = event.source.user_id
    
    func = get_message(msg_request)
    line_bot_api.reply_message(event.reply_token, func)
```

https://developers.line.biz/en/reference/messaging-api/#message-event



