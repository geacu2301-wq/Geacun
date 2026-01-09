import os

def main():
    
    if os.getenv("GITHUB_ACTIONS") == "true":
        
        name = "TestUser"
        year = "2000"
    else:
        name = input("Please type in name: ")
        year = input("Please type in year: ")

    print(f"{name} is a valiant knight, born in the year {year}.")
    print(f"One morning, {name} woke up to an awful racket.")
    print("A dragon was approaching the village.")

if __name__ == "__main__":
    main()





