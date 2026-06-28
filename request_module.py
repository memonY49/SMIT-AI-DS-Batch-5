import requests as rs
import json

# url = "https://en.wikipedia.org/wiki/Salman_Khan"
# header = {"User-Agent":"Mozilla/5.0"}
# try:
#     response = rs.get(url, headers=header)

#     print(response.text)
#     print(response.status_code)
# except:
#     print("Something went wrong!!!")

# api = "https://httpbin.org/get"

# param = {"name":"Ali", "age":23}


# response = rs.get(api,params = param)
# print(response.json())

news_api = "https://newsapi.org/v2/everything"

response = rs.post(news_api, params={"apiKey": "ae1965e099324bce83e76f8ff2612fa9","q":"tesla"})

print(response.status_code)
# response_dict = json.loads(response.json())
# print(type(response_dict))
articles = response.json()["articles"]

for index, art in enumerate(articles):
    image = art['urlToImage']
    if image != None:
        image_res = rs.get(image)
        if response.status_code == 200:
            with open(f"images/image{index}.jpg","wb") as file:
                file.write(response.content)
            print(f"{image} is downloaded")
    

# image_url = "https://platform.theverge.com/wp-content/uploads/sites/2/chorus/uploads/chorus_asset/file/25488453/2154480997.jpg?quality=90&strip=all&crop=0%2C10.737892056687%2C100%2C78.524215886627&w=1200"

# response = rs.get(image_url)

# if response.status_code == 200:
#     with open("image.jpg","wb") as file:
#         file.write(response.content)
#     print("image is downloaded")


