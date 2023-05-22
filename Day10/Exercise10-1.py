
def format_name(f_name,l_name):
    name=f_name.title()+" "+l_name.title()
    
    return name
    
f_name= input("First name: ")
l_name= input("Last name: ")

full_name= format_name(f_name,l_name)
print(full_name)