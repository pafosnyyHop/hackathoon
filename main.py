from views import listing, create, retrieve, delete, update

def main():
    print('Privet! tebe dostupno: \n\tLIST-1\n\tDETAIL-2\n\tCREATE-3\n\tUPDATE-4\n\tDELETE-5')
    choice = input('Vvedite deistvie(1,2,3,4,5): ')
    if choice.strip() == '1':
        print(listing())
    elif choice.strip() == '2':
        print(retrieve())
    elif choice.strip() == '3':
        print(create())
    elif choice.strip() == '4':
        print(update())
    elif choice.strip() == '5':
        print(delete())
    else:
        print('Nevernii vibor!')

    answer = input("Hotite prodolzit'?(yes/no): ")
    if answer.lower().strip() == 'yes':
        main()
    else:
        print('Good bay!')


main()