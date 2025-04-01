class Agreement():
    def main():
        print("The Agreeing Bot ")
        fav_Animal = input("What is your Favourite Animal? ")
        reply = f"My favourite Animal is also \033[1;3;4m{fav_Animal}!\033[0m "
        print(reply)

if __name__ == '__main__':
    obj = Agreement()
    Agreement.main()