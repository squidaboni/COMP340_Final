
# tempSrcCode = "12 + 1 * 3"


def tokenize(temp_src_code):

    tempString = ""
    fromSC = []
    typeArray = []

    for character in temp_src_code:
        if character.isdigit():
            tempString += character

        elif character in ["+", "-", "*", "/", "(", ")"]:
            if tempString != "":
                fromSC.append(tempString)
                fromSC.append(character)
                tempString = ""
        else:
            continue
    if tempString != "":
        fromSC.append(tempString)


    print(fromSC)

    for index in fromSC:

        match index:
            case "+":
                typeArray.append("PLUS")
            case "-":
                typeArray.append("MINUS")
            case "*":
                typeArray.append("MULTI")
            case "/":
                typeArray.append("DIV")
            case "(":
                typeArray.append("LPAREN")
            case ")":
                typeArray.append("RPAREN")
            case _:
                typeArray.append("NUMB")

    return_list = []
    mydict = dict(zip(fromSC, typeArray))
    for key, value in mydict.items():
        return_list.append([key, value])

    return return_list
