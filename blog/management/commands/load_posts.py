import json
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Post
from datetime import datetime

class Command(BaseCommand):
    help = 'Load posts from JSON file'

    def handle(self, *args, **kwargs):
        with open('posts.json', 'r') as file:
            posts_data = json.load(file)
            
            for post_data in posts_data:
                # Try different possible key names for author
                author_name = post_data.get('author') or post_data.get('user_id') or 'default_user'
                
                # Get or create the user
                user, created = User.objects.get_or_create(
                    username=author_name if isinstance(author_name, str) else f"user_{author_name}",
                    defaults={'email': f"{author_name}@example.com"}
                )
                
                # Get title and content with fallbacks
                title = post_data.get('title', 'Untitled Post')
                content = post_data.get('content', '')
                
                # Create the post
                Post.objects.create(
                    title=title,
                    content=content,
                    author=user
                )
                
        self.stdout.write(self.style.SUCCESS('Successfully loaded posts'))