
try:
    while True:
        a = input().strip().upper()
        #rows = 0
        if a.isdigit() == True:
            X = int(a) # 縦横X
            if X % 2 == 0 :
                # 偶数
                print("invalid")
            else:
                # 奇数 
                for i in range(X):
                    output = ""
                    for j in range(X):
                        c = X//2    # 中間
                        if i <= c:
                            if j == i or j == X - i -1:
                                output += "y"
                            else:
                                output += "."
                        else:
                            if j == c:
                                output += "y"
                            else:
                                output += "."
                    print(output)
        else:
            print("invalid")
except EOFError:
    pass

