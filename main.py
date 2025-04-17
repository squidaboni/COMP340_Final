from lexer import tokenize


def main():
    sourceCode = "12+1-3"
    print(tokenize(sourceCode))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
