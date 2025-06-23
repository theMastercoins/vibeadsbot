def load_user_ids(usertxt):
    try:
        with open(f'userslist/{usertxt}.txt', 'r') as file:
            # Read all lines and remove whitespace
            user_ids = [line.strip() for line in file.readlines()]
            # Remove empty lines
            user_ids = [uid for uid in user_ids if uid]
            return user_ids
    except FileNotFoundError:
        print("Error: user_ids.txt file not found")
        return []
    except Exception as e:
        print(f"Error loading user IDs: {str(e)}")
        return []


