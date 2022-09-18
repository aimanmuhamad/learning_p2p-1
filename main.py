from math_function import add, root, modulo


def main():
    operator = input("masukkan operator :")
    if operator == "+":
        data_1 = int(input("masukkan input 1 :"))
        data_2 = int(input("masukkan input 2 :"))
        result = add(data_1, data_2)
        print("{} {} {} = {} ".format(data_1, operator, data_2, result))
    
    if operator == "root" :
        data_1 = int(input("masukkan input 1 :"))
        result = root(data_1)
        
    elif operator == "%" :
        data_1 = int(input("masukkan input 1 :"))
        data_2 = int(input("masukkan input 2 :"))
        result = modulo(data_1, data_2)
        print("{} {} {} = {} ".format(data_1, operator, data_2, result))
        
        print(result)
    
if __name__ == "__main__":
    print("Hello Main !")
    main()