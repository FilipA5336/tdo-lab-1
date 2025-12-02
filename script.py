import os
name = os.getenv("GREETING_USER", "Nick")
print(f"Witaj, {name}.)
