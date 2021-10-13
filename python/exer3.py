print("-----F L A M E S-----")
name1 = input('Enter your name: ').lower()
name2 = input('Enter your partner\'s name: ').lower()

def flames(name1, name2):
    n1 = sum(letter in name2 for letter in name1)
    n2 = sum(letter in name1 for letter in name2)
    results = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
    sum_n = n1 + n2
    print("Total: ",n1," + ",n2," = ",sum_n)
    index = sum_n % len(results) - 1
    return results[index]

print('Your Relationship is', flames(name1, name2))