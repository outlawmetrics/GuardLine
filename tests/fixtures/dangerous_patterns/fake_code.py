cursor.execute("SELECT * FROM users WHERE id = " + user_id)

user_input = "__import__('os').system('rm -rf /')"
result = eval(user_input)  # deletes everything on the system