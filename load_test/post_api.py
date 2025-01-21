import requests
from requests.auth import HTTPBasicAuth

# WordPress 사이트 정보
# site_url = ['http://localhost:8000/wp-json/wp/v2/posts']('http://localhost:8000/wp-json/wp/v2/posts')
site_url = 'http://localhost:8000/wp-json/wp/v2/posts'
username = 'rest_user'
application_password = 'rest1234'

# 포스트 데이터
post_data = {
    'title': 'Sample Post Title',
    'content': 'This is the content of the post.',
    'status': 'publish'  # 'draft'로 설정하면 초안으로 저장됩니다.
}

# HTTP 요청 보내기
response = requests.post(
    site_url,
    auth=HTTPBasicAuth(username, application_password),
    json=post_data
)

# 응답 확인
if response.status_code == 201:
    print('Post created successfully.')
    print('Post ID:', response.json().get('id'))
else:
    print('Failed to create post.')
    print('Response:', response.content)
