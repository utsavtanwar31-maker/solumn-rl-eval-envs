import os
import json

ROLES_PATH = os.path.join(os.path.dirname(__file__), "..", "config", "roles.json")

def load_roles():
    with open(ROLES_PATH, "r") as f:
        return json.load(f)

def can_perform_action(role, action):
    roles = load_roles()
    perms = roles.get(role, [])
    return action in perms
