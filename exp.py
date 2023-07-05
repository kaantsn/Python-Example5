import itertools

def brute_force(target_password, max_length):
    chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    attempts = 0
    for length in range(1, max_length+1):
        for guess in itertools.product(chars, repeat=length):
            attempts += 1
            guess = ''.join(guess)
            if guess == target_password:
                return guess, attempts
    return None, attempts

target_password = "1234"
max_length = 4
result, attempts = brute_force(target_password, max_length)

if result:
    print("Şifre çözüldü:", result)
    print("Deneme sayısı:", attempts)
else:
    print("Şifre çözülemedi.")
