import requests

import requests

for i in range(20,459):  # 예시로 10개의 이미지를 다운로드하는 코드
    page_num="{:03d}".format(i)
    img_url = "http://online.fliphtml5.com/lciv/ohwq/files/page/{}.jpg".format(i)
    response = requests.get(img_url)

    with open("./images/page{}.jpg".format(page_num), "wb") as f:
        f.write(response.content)
