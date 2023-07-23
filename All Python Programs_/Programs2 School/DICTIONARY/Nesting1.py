employee = {'Mohan':{'age':29, 'salary':55000,'depart':'Director'},
            'Vinod':{'age':55, 'salary':80000,'depart':'CEO'}}
for key in employee:
    print('-----------------')
    print('Name: ',key)
    print('Age: ',employee[key]['age'])
    print('Salary: ',employee[key]['salary'])
    print('Department: ',employee[key]['depart'])
