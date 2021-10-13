print("-----F L A M E S-----")
name1 = input('Enter your name: ').lower().replace(" ","").replace(".","")
name2 = input('Enter your partner\'s name: ').lower().replace(" ","").replace(".","")

def flames(name1, name2):
    n1 = sum(letter in name2 for letter in name1)
    n2 = sum(letter in name1 for letter in name2)

    results = ["FRIENDS", "LOVE", "ACQUAINTANCES", "MARRIAGE", "ENEMY", "SIBLINGS"]

    print(name1, "---->", n1, " = " , results[n1%len(results)-1])
    print(name2, "----> ", n2, " = " , results[n2%len(results)-1])
    
    counter = n1 + n2
    print("Total: ",n1," + ",n2," = ",counter)
    index = counter % len(results) - 1
    return results[index]

print('Your Relationship is', flames(name1, name2))