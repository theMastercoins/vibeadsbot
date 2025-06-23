from watchad import watch_ad
from textutils import *
from user_load import load_user_ids
from config import UserConfig
import random
import time

# Initialize configuration
config = UserConfig()
usertxt = input("Enter user list name: ")

USER_IDS = load_user_ids(usertxt)

# Initialize all users in config
for user_id in USER_IDS:
    config.initialize_user(user_id)

def run_watch_ads():
    available_users = config.get_available_users()
    if not available_users:
        type_writer(f"{Fore.YELLOW}All users have reached their daily view limits!")
        return False
    
    # Randomly select a user that hasn't reached their limit
    user_id = random.choice(available_users)
    stats = config.get_user_stats(user_id)
    
    print(f"Selected User ID: {user_id}")
    print(f"Views Today: {stats['daily_views']}/{stats['daily_limit']}")
    
    watch_ad(user_id=user_id)
    config.increment_view_count(user_id)
    
    # Random delay between requests (0.5 to 2 seconds)
    time.sleep(random.uniform(0.5, 2))
    return True

if __name__ == "__main__":
    print("Loaded user list: " + usertxt)
    print("Total users: " + str(len(USER_IDS)))
    while True:
        result = run_watch_ads()
        if not result:
            break
    


