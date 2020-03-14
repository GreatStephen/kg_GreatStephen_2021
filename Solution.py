import sys

if __name__ == "__main__":
    print(len(sys.argv))
    if(len(sys.argv)!=3):
        print("Please provide proper input!")
    s = sys.argv[1]
    t = sys.argv[2]
    if len(s)!=len(t):
        print("false")
        sys.exit(0)
    dict1 = {}
    dict2 = {}

    for i in range(len(s)):
        if not s[i] in dict1 and not t[i] in dict2:
            dict1[s[i]] = i+1
            dict2[t[i]] = i+1
        elif s[i] in dict1 and t[i] in dict2:
            if dict1[s[i]] != dict2[t[i]]:
                print("false")
                sys.exit(0)
        elif not s[i] in dict1 and t[i] in dict2:
            dict1[s[i]] = dict2[t[i]]
        else:
            print("false")
            sys.exit(0)
    
    # print(dict1)
    # print(dict2)
    print("true")
    