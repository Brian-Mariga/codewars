def check_alive(health):
    if (-10 <= health <= 10) and isinstance(health, int):
        if health <= 0:
            return False
        else:
            return True
    else:
        print("Health must be a whole number between -10 and 10.")
