from math_function import add, exponential


def main():
    operator = input("masukkan operator :")
    if operator == "+":
        data_1 = int(input("masukkan input 1 :"))
        data_2 = int(input("masukkan input 2 :"))
        result = add(data_1, data_2)
        print("{} {} {} = {} ".format(data_1, operator, data_2, result))
<<<<<<< HEAD

    if operator == "exponential" :
        data_1 = int(input("masukkan input 1:"))
        result = exponential(data_1)
=======
    
    if operator == "root" :
        data_1 = int(input("masukkan input 1 :"))
        result = root(data_1)
        
        print(result)
>>>>>>> 4ce10cd02bab038734c13194be691a8e88afde26

        print(result)

if __name__ == "__main__":
    print("Hello Main !")
    main()
