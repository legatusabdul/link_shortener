"""
Service to interact with Student artifacts and business logic
"""
import string
import random

from models.db import UrlDBModel


class UrlService:
    
    def generate_short_url():
        
        letters = string.ascii_lowercase + string.ascii_uppercase + string.digits        
        
        while True:
            
            short_url = ''.join(random.choice(letters) for i in range(6))
            url = UrlDBModel.query.filter_by(short_url=short_url).first()
            
            if not url:
                return short_url
        