import json
from employee import details, employee_name, age, title

def  create_dict(name:str, age:int, title:str):
    dict = {"First_name":name, "Age":int(age), "Title":title}
    return dict

def write_json_to_file(json_obj, file):
    with open(file, "w") as file:
        file.write(json_obj)


def main():
    details()
    # Create employee dictionary
    emp_dict =create_dict(employee_name, age,title)
    print("Employee_Dict : " + str(emp_dict))
    ''' 
    Use a function called dumps from the json module to convert employee_dict
    into a json string and store it in a variable called json_object.
    '''
    json_obj = json.dumps(emp_dict)
    print("json_object: " + str(json_obj))

    write_json_to_file(json_obj, "employee.json")

if __name__ == "__main__":
    main()