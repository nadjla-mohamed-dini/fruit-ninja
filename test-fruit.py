def save_score():
    try:
        name = input("your Name : ")
        score = int(input("Your Score : "))

        with open(r"C:\Users\fatyl\pendu\fruit_scores.txt", "a") as fichier:
            fichier.write(f"{name}: {score}\n")
        print(f"Score save, {name}!")
    except Exception as e:
        print(f"Error : {e}")

save_score()
