from stack_class import ArrayStack



def test_brackets():
    tests = [
        "{A[(i+1)]=0;}", # True}
        "if ((x<0) && (y<3)", # False
        "while (n < 8)) {n++;}",    # False
        "arr[(i+1])=0;", # False 
    ]
    for t in tests:
        print(t, "->", checkBrackets(t))
    

if __name__ == "__main__":
    test_brackets()


