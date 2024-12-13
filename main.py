from scripts.os.openapp import openapp
def main():
        message, success = openapp("Google Chrome")
        print(message)
        print(success)

if __name__ == "__main__":
    main()