import os

def main():
    name = os.getenv("USERNAME")
    print(f"Hello, {name} desde GitHub!")

if __name__ == "__main__":
    main()
