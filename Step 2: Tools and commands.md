# Step 2:  FastAPI testing tool = postman 介紹

## 2.1 安裝 postman
* google plugin 
```
  https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop/related?hl=zh-TW
```
## 2.2 how to shutdown uvicorn
* shutdown uvicorn AGSI server
```
sudo lsof -t -i tcp:8000 | xargs kill -9
```
## 2.3 Some API examples
> /getAllUsers
> /getUser/1
> /createUser
> /updateUser/1
> /deleteUser/1

## 2.4 RestfulAPI examples (see code)
