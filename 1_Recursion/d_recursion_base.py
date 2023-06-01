def recursiveMethod(n):
    if n<1:
        print("n is less than 1")
    else:
        recursiveMethod(n-1)
        print(n)

recursiveMethod(5)

'''
recursiveMethod(5)
└── recursiveMethod(4)
    └── recursiveMethod(3)
        └── recursiveMethod(2)
            └── recursiveMethod(1)
                └── n is less than 1
            └── print(2)
        └── print(3)
    └── print(4)
└── print(5)
'''