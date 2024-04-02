def howmany(file_path):
    pythons=["if","else","not","for","while","class","print","with","def","in","open","as","read","input","str"]
    with open(file_path, 'r') as file:
            content = file.read()
            dict={}
            for i in pythons:
                  key=i
                  value=str(content).count(i)
                  if value==0:
                    pass
                  else:
                    dict[key]=value
            return dict
file_path = 'ret.txt'
print(howmany(file_path))
