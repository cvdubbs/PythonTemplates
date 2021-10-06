i = 0
dfAccounts = pd.DataFrame(columns = ['first_name', 'last_name', 'full_name', 'username', 'password', 'email'])

while accNo > i:
    k =random.randint(0, maxNum-1)
    l =random.randint(0, maxNum-1)
    first_name = (random.choice(open("Fnames.txt").read().split()))
    last_name =  (random.choice(open("Lnames.txt").read().split()))
    full_name = (first_name + ' ' + last_name)
    username = (first_name + last_name + '.' + str(random.randint(1, 100)) + str(random.randint(1, 1000)))
    password = (open("password.txt").readline())
    email = (username + '@' + 'gmail.com')

    dfAccounts = dfAccounts.append({'first_name' : first_name, 'last_name' : last_name, 'full_name' : full_name. 'username' : username, 'password' : password, 'email' : email}, 
                ignore_index = True)
                
    i = i + 1
