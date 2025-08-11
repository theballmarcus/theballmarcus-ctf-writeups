import time
import threading

# In-memory storage for user states
user_states = {}

def init_user_state(username):
    if username and username not in user_states:
        user_states[username] = {
            'grip': 0,
            'traveled': 0,
            'last_updated': time.time()
        }

def write_state(username, state):
    if username:
        user_states[username] = {
            **state,
            'last_updated': time.time()
        }

def read_state(username):
    if username in user_states:
        state = user_states[username].copy()
        state.pop('last_updated', None)
        return state
    return {}

def check_state(username):
    return username in user_states

def delete_user_state(username):
    if username in user_states:
        del user_states[username]

def cleanup_old_states(timeout=10):
    while True:
        now = time.time()
        to_delete = [user for user, state in user_states.items()
                     if now - state.get('last_updated', 0) > timeout]
        for user in to_delete:
            del user_states[user]
        time.sleep(1)

# Optional: run the cleanup thread if needed
# threading.Thread(target=cleanup_old_states, daemon=True).start()

# import time
# import os

# def get_state_file(username):
#     if not username:
#         return None
#     return f'state_{username}.txt'

# def init_user_state(username):
#     path = get_state_file(username)
#     if path and not os.path.exists(path):
#         with open(path, 'w') as f:
#             f.write('grip=0\ntraveled=0\n')
#         os.utime(path, None) 

# def write_state(username, state):
#     path = get_state_file(username)
#     with open(path, 'w') as f:
#         for k, v in state.items():
#             f.write(f'{k}={v}\n')
            
# def delete_user_state(username):
#     path = get_state_file(username)
#     if path and os.path.exists(path):
#         os.remove(path)

# def read_state(username):
#     path = get_state_file(username)
#     with open(path, 'r') as f:
#         lines = f.readlines()
#     state = {}
#     for line in lines:
#         k, v = line.strip().split('=')
#         state[k] = int(v)
#     return state

# def check_state(username):
#     path = get_state_file(username)
#     if not os.path.exists(path):
#         return False
#     return True

# def cleanup_old_states():
#     while True:
#         now = time.time()
#         for filename in os.listdir('.'):
#             if filename.startswith('state_') and filename.endswith('.txt'):
#                 try:
#                     file_mtime = os.path.getmtime(filename)
#                     if now - file_mtime > 10:
#                         os.remove(filename)
#                 except Exception as e:
#                     print(f"Error deleting file {filename}: {e}")
#         time.sleep(1)
