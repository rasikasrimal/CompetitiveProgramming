def generate_names():
    names = input("Enter names separated by commas: ").split(',')
    formatted_names = []

    for name in names:
        formatted_name = ""
        for c in name.strip().upper():
            if 33 <= ord(c) <= 126:
                formatted_name += chr(0xFEE0 + ord(c))
            else:
                formatted_name += c
        formatted_names.append("★" + formatted_name + "★『sLc』")

    return formatted_names

if __name__ == "__main__":
    for name in generate_names():
        print(name)
