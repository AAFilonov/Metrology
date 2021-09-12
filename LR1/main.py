# Составить и протестировать функцию для замены
# cимволов «:» на «.» в заданной строке, начиная с указанной позиции.
# Sanya:have:done:some:programming

def replaceСolons(str, position):
    return str[:position] + str[position:].replace(":", ".")


if __name__ == '__main__':
    argument = input("Input your string: ")
    position = int(input("Input position: "))
    result = replaceСolons(argument, position)
    print("String with replaced colons - " + result)
