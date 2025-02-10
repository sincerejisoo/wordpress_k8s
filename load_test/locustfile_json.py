from locust import HttpUser, task, between
import random
import json

class WordPressUser(HttpUser):
    wait_time = between(1, 3)  # 요청 간 대기 시간 (1~3초)

    def on_start(self):
        """테스트 시작 시, 블로그 글 ID 목록을 가져옴"""
        self.post_ids = self.get_post_ids()
    
    def get_post_ids(self):
        """WordPress API를 사용하여 게시글 목록 가져오기"""
        response = self.client.get("/wp-json/wp/v2/posts")
        if response.status_code == 200:
            return [post["id"] for post in response.json()]
        return []

    @task(5)
    def view_blog_post(self):
        """블로그 글 조회 (읽기 부하)"""
        if self.post_ids:
            post_id = random.choice(self.post_ids)
            self.client.get(f"/blog/{post_id}", name="/blog/[post_id]")

    @task(2)
    def write_comment(self):
        """댓글 작성 (쓰기 부하)"""
        if self.post_ids:
            post_id = random.choice(self.post_ids)
            comment_data = {
                "comment_post_ID": post_id,
                "comment_author": "LocustUser",
                "comment_author_email": "locust@example.com",
                "comment_content": "This is a test comment from Locust",
                "comment_parent": 0,
                "submit": "Post Comment"
            }
            self.client.post("/wp-comments-post.php", data=comment_data, name="/wp-comments-post")

    @task(1)
    def access_admin_dashboard(self):
        """관리자 페이지 접근"""
        admin_creds = {"log": "jskim02", "pwd": "cicd1234", "wp-submit": "Log In"}
        with self.client.post("/wp-login.php", data=admin_creds, name="/wp-login", catch_response=True) as response:
            if "dashboard" in response.text:
                self.client.get("/wp-admin/", name="/wp-admin")

    @task(2)
    def visit_random_page(self):
        """랜덤한 페이지 방문"""
        pages = ["/", "/about", "/contact", "/blog", "/faq"]
        self.client.get(random.choice(pages), name="/random_page")
