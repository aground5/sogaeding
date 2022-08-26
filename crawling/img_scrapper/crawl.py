from CygnusX1.cygnusx1.scraper import scrap_google_images
def img_url(keyword) :
    args = {
        "keywords": keyword,
        "workers": 1,
        "headless" : True,
        "use_suggestions" : False,
        "max": 3
    }
    img_src, _ = scrap_google_images(args, keyword)
    return img_src

print(img_url("윤석열 지지율"))