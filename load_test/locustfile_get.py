from locust import HttpUser, task, between, TaskSet
import random as rd

class UserBehavior(TaskSet):
    # visit random post
    @task(80)
    def get_post(self):
        post_id = rd.randint(1, 300000)
        self.client.get(f'/sample-post-{post_id}')

    @task(20)
    def home(self):
        self.client.get('/')


class LocustUser(HttpUser):
    host = "<http://af81fb694637544fea72c19bc12e4b72-535310736.ap-northeast-2.elb.amazonaws.com>"
    tasks = [UserBehavior]
    wait_time = between(1, 4)

# from locust import HttpUser, task, between
# import random

# class WordPressUser(HttpUser):
#     wait_time = between(1, 5)  # 사용자 간 요청 간격 (1~5초)

#     # 테스트할 게시글 ID 범위 (300,000개)
#     post_id_range = range(1, 300001)

#     # 검색할 키워드 목록 (주제별로 설정)
#     search_keywords = ["WordPress", "Database", "Optimization", "Scaling", "Security", "Kubernetes", "AWS", "AI"]

#     # 카테고리 목록 (WordPress의 wp_terms 기반)
#     categories = ["technology", "performance", "ai", "cloud", "database", "wordpress"]

#     @task(40)  # 40% 확률로 개별 게시글 조회
#     def view_post(self):
#         post_id = random.choice(self.post_id_range)
#         self.client.get(f"/posts/{post_id}/", name="/posts/[id]")

#     @task(20)  # 20% 확률로 페이지네이션 요청
#     def list_posts(self):
#         page = random.randint(1, 1000)  # 1페이지당 10~30개 표시 가정 (최대 1000 페이지)
#         self.client.get(f"/posts?page={page}", name="/posts?page=[n]")

#     @task(15)  # 15% 확률로 검색 수행
#     def search_posts(self):
#         query = random.choice(self.search_keywords)
#         self.client.get(f"/search?query={query}", name="/search?query=[keyword]")

#     @task(15)  # 15% 확률로 카테고리별 게시글 조회
#     def view_category_posts(self):
#         category = random.choice(self.categories)
#         self.client.get(f"/category/{category}/", name="/category/[category]")

#     @task(10)  # 10% 확률로 홈페이지 방문
#     def view_homepage(self):
#         self.client.get("/", name="HomePage")