#Create a lambda function to sort the name list according to their surname.
#name = ["jay A kumar",'deepak N sharma','rohit N yadav','mithilesh singh','payal vasave','Fahad Momin']

name = ["jay A kumar",'deepak N sharma','rohit N yadav','mithilesh singh','payal vasave','Fahad Momin']
#['jay A kumar', 'Fahad Momin', 'deepak N sharma', 'mithilesh singh', 'payal vasave', 'rohit N yadav']
name.sort(key=lambda name:name.lower().split()[-1])
print(name)
