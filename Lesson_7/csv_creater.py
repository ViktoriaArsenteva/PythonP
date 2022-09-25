import User_interface

def create_csv(res):
    res = res.split()
    with open ('data2.csv','a') as file2:
        file2.write('{};{}'
                    .format(res[0],res[1]))