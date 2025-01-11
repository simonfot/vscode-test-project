def greet(name):
    """
    Simple greeting function
    """
    return f"Hello, {name}! Welcome to VS Code testing."

def main():
    user_name = "Developer"
    message = greet(user_name)
    print(message)

if __name__ == "__main__":
    main()