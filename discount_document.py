import requests, json, env

def Discount_Document(request):
  url = env.ENVIROMENT + env.DISCOUNT_DOCUMENT

  payload = json.dumps({
    "company": request.session['company_pk']
  })
  headers = {
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.text)
