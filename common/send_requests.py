import requests

def post_request(cases,head):
    results = []
    for i in cases:
        url = i["url"]
        data = eval(i["data"])
        res = requests.post(url=url,json=data,headers= head).json()
        expected = eval(i["expected"])
        res_msg = res["msg"]
        expected_msg = expected["msg"]
        if res_msg ==expected_msg:
            result = "Passed"
        else:
            result = "Failed"
        results.append(result)
    return results