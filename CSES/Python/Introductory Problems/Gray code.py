n = int(input())

def generate_gray_code(n):
    if n == 1:
        return ["0", "1"]
    
    lower_gray_code = generate_gray_code(n - 1)
    gray_code = []
    for code in lower_gray_code:
        gray_code.append("0" + code)
    for code in reversed(lower_gray_code):
        gray_code.append("1" + code)
    return gray_code

gray_code = generate_gray_code(n)

for code in gray_code:
    print(code)
