import json
import random
from datetime import datetime, timedelta
from pathlib import Path

class UserConfig:
    def __init__(self):
        self.config_file = 'user_config.json'
        self.load_config()

    def load_config(self):
        if Path(self.config_file).exists():
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
        else:
            self.config = {
                'users': {},
                'last_reset_date': datetime.now().strftime('%Y-%m-%d')
            }
            self.save_config()

    def save_config(self):
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=4)

    def reset_daily_counts_if_needed(self):
        last_reset = datetime.strptime(self.config['last_reset_date'], '%Y-%m-%d')
        if datetime.now().date() > last_reset.date():
            for user in self.config['users'].values():
                user['daily_views'] = 0
            self.config['last_reset_date'] = datetime.now().strftime('%Y-%m-%d')
            self.save_config()

    def initialize_user(self, user_id):
        if user_id not in self.config['users']:
            self.config['users'][user_id] = {
                'id': len(self.config['users']) + 1,
                'daily_limit': random.randint(20, 50),
                'daily_views': 0
            }
            self.save_config()

    def can_watch_ad(self, user_id):
        self.reset_daily_counts_if_needed()
        self.initialize_user(user_id)
        user = self.config['users'][user_id]
        return user['daily_views'] < user['daily_limit']

    def increment_view_count(self, user_id):
        if user_id in self.config['users']:
            self.config['users'][user_id]['daily_views'] += 1
            self.save_config()

    def get_available_users(self):
        self.reset_daily_counts_if_needed()
        return [user_id for user_id, data in self.config['users'].items()
                if data['daily_views'] < data['daily_limit']]

    def get_user_stats(self, user_id):
        if user_id in self.config['users']:
            return self.config['users'][user_id]
        return None