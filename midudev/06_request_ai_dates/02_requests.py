# API requests in python

import urllib.request
import json

api_posts = "https://jsonplaceholder.typicode.com/posts"

try:
    response = urllib.request.urlopen(api_posts)
    data = response.read()
    data = json.loads(data.decode('utf-8'))
except Exception as e:
    print(f"Error in the request: {e}")

# data = json.loads(response.read())

print(data)
response.close()

import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
data = response.json()
print("--------------------------------")
print(data)
print("--------------------------------")

# get the first 10 posts
posts = data[:10]

# print the title of the first 10 posts
for post in posts:
    print(post['title'])


# 3. Un POST
print("\nPOST:")

url = "https://jsonplaceholder.typicode.com/posts"

post_data = {
    "title": "Gustavo's post",
    "body": "This is the body of my first post",
    "userId": 619
}

headers = {
    "Content-Type": "application/json"
}
try:
    response = requests.post(url, headers=headers, json=post_data)
    print(response.status_code)
    print(response.json())
except Exception as e:
    print(f"Error in the request: {e}")


# 4. Un PUT
url = "https://jsonplaceholder.typicode.com/posts/1"

post_data = {
    "title": "Gustavo's post",
    "body": "This is the body of my first post",
    "userId": 619
}
try:
    response = requests.put(url, json=post_data)
    print(response.status_code)
    print(response.json())
except Exception as e:
    print(f"Error in the request: {e}")

# 5. Un DELETE
url = "https://jsonplaceholder.typicode.com/posts/1"


# using the OpenAI API
# Ref: https://platform.openai.com/docs/api-reference/making-requests
OPENAI_KEY = "sk-XXXXXXXX"

import json

def call_openai_gpt(api_key, prompt):
  url = "https://api.openai.com/v1/chat/completions"
  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
  }
  data = {
    "model": "gpt-4o-mini",
    "messages": [{"role": "user", "content": prompt}]
  }

  response = requests.post(url, json=data, headers=headers)
  return response.json()

api_response = call_openai_gpt(OPENAI_KEY, "Escribe un breve poema sobre la programación")

# Llamar a la API de DEEPSEEK

import json
DEEPSEEK_API_KEY = "xxx"
def call_deepseek(api_key, prompt):
  url = "https://api.deepseek.com/chat/completions"
  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
  }
  data = {
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": prompt}]
  }

  response = requests.post(url, json=data, headers=headers)
  print(response.json())
  return response.json()

api_response = call_deepseek(DEEPSEEK_API_KEY, "Escribe un breve poema sobre la programación")

# print(json.dumps(api_response, indent=2))

print(api_response["choices"][0]["message"]["content"])