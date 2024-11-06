import http.client

conn = http.client.HTTPSConnection("v1.hockey.api-sports.io")

headers = {
    'x-rapidapi-host': "v1.hockey.api-sports.io",
    'x-rapidapi-key': "5c3a2b9d58739b48a329f4707c362671"
    }

conn.request("GET", "/leagues", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))