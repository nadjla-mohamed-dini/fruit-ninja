def save_score():
    try:
        name = input("Your name: ")
        score = int(input("Your score: "))
        try:
            with open(r"C:\Users\fatyl\pendu\fruit_scores.txt", "r") as file:
                scores = file.readlines()
        except FileNotFoundError:
            scores = []  
        scores.append(f"{name}: {score}\n")
        scores = sorted(scores, key=lambda x: int(x.split(": ")[1]), reverse=True)
        top_scores = scores[:5]
        with open(r"C:\Users\fatyl\pendu\fruit_scores.txt", "w") as file:
            file.writelines(top_scores)
        
        print(f"Score saved, {name}!")
        print("Top scores:")
        for score in top_scores:
            print(score.strip())
    
    except Exception as e:
        print(f"Error: {e}")

save_score()
