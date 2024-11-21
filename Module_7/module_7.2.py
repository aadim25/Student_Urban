strings = ['111','223','333']
file_name = 'temp7-2.txt'
file_seek=[int]
def custom_write(file_name, strings:list):
    file = open (file_name, 'w')
    for i in strings:
        file.writelines(f'{i}\n')
        file_seek.append(file.tell())
    file.close()
    
def my_dict(file_name):
    file = open(file_name, 'r', encoding='utf-8')
    # print(file.read())

    # print(file.seek(5))
    x=0
    n=0
    text=''
    result=[{(int,int):str}]
    # print(result)
    my_bool = True
    # file.seek(0)
    while my_bool:
        if (file.readline()) !="":
            text = (file.readline())
            n=file.tell()
            result.append({(x + 1, n): text})

            print('n ',n,'txt ',text, 'x ',x)
            x += 1
        else:
            my_bool=False
    print(result)
        #print(file.tell())
        #print(file.readline)
    print(result)
    file.close()

custom_write(file_name, strings)
my_dict(file_name)
#strings_positions
