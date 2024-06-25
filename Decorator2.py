# Create a decorator named requires_role that checks if a user has the required role to execute a function. If the user does not have the required role, print an error message and do not execute the function.
current_user_role = "user"

def requires_role(role):
    def decorator(func):
        def wrapper(*args):
            if current_user_role == role:
                return func(*args)
            else:
                print(f"Error: You need to have the '{role}' role to execute this function.")
        return wrapper
    return decorator

@requires_role("administrator")
def delete_user(user_id):
    print(f"User {user_id} deleted")

# Test the decorator
delete_user(123)  # Assume the current user does not have the "admin" role
