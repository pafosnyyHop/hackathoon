import json

file_path = '/home/hello/Рабочий стол/hakatoon/data.json'
id_file = '/home/hello/Рабочий стол/hakatoon/id.txt'

def get_data():
    with open(file_path) as file:
        return json.load(file)

def save_data(data):
    with open(file_path, 'w') as file:
        json.dump(data,file)

def listing():
    data = get_data()
    return f'Spisok tovarov v assortimente: {data}'

def retrieve():
    data = get_data()
    try:
        id = int(input('Vvedite id produkta: '))
        product = list(filter(lambda x: id == x['id'], data))
        return product[0]
    except:
        return 'Except id!'

def get_id():
    with open(id_file, 'r') as file:
        id = int(file.read())  
        id += 1
    with open(id_file, 'w') as file:
        file.write(str(id))
    return id  

def create():
    data = get_data()
    try:
        product = {
            'id': get_id(),
            'marka': input('Vvedite marku noutbuka: '),
            'model': input('Vvedite model noutbuka: '),
            'vipusk': int(input('Vvedite god vipuska: ')),
            'opisanie': input('Dobavte opisanie: '),
            'price': round(float(input('Price: ')), 2)

        }
    except:
        return 'Nevernie dannie!'
    data.append(product)
    save_data(data)

    return 'Tovar opublikovan!'


def update():
    data = get_data()
    try:
        id = int(input("Vvedite id tovara: "))
        tovar = list(filter(lambda x: x['id'] == id, data))[0]
    except:
        return 'Nevernii id!'

    data_idx = data.index(tovar)
    choice = input("Chto izmenit'?\n1 - marka\n2 - model\n3 - vipusk\n4 - opisanie\n5 - price\nVvod: ")
    if choice.strip() == '1':
        data[data_idx]['marka'] = input('Vvedite izmeneniya: ')
    elif choice.strip() == '2':
        data[data_idx]['model'] = input('Vvedite izmeneniya: ')
    elif choice.strip() == '3':
        try:
            data[data_idx]['vipusk'] = int(input('Vvedite izmeneniya: '))
        except:
            return 'Nevernoe znacheniya!'
    elif choice.strip() == '4':
        data[data_idx]['opisanie'] = input('Vvedite izmeneniya: ')
    elif choice.strip() == '5':
        try:
            data[data_idx]['price'] = round(float(input('Vvedite izmeneniya: '), 2))
        except:
            return 'Nevernoe znahcenie!'
    else:
        return 'Nevernoe znachenie' 
    
    save_data(data) 

    return 'Tovar obnovlen!'


def delete():
    data = get_data()
    try:
        id = int(input('vvedite id tovara: '))
        product = list(filter(lambda x: x['id'] == id, data))[0]
        print(f'Tovar dlya edaleniya {product["marka"]} {product["model"]}')
    except:
        return 'Неверный id!'
    
    choice = input("Ydalit' etot tovar(yes/no)?\n: ")
    if choice.lower().strip() != 'yes':
        return 'Tovar ne udalen!'
    else:
        data.remove(product)
        save_data(data)
        return 'Tovar ydalen!'  








