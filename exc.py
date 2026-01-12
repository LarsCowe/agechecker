def categoriseer_leeftijd():
    try:
        leeftijd = int(input("Voer je leeftijd in: "))

        if leeftijd >= 18 and leeftijd < 65:
            print("Je bent een volwassene.")
        elif leeftijd >= 65:
            print("Je bent een senior.")
            
    except ValueError:
        print("Dat is geen geldig nummer.")

if __name__ == "__main__":
    categoriseer_leeftijd()
