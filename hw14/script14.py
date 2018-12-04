import pickle

from hw14.Employee import Employee


def serialization():
    employee = Employee("Mary", 5524231133, salary=100000)
    with open('employee', 'wb') as f:
        pickle.dump(employee, f)


# serialization()


def deserialization():
    with open('employee', 'rb') as f:
        print(pickle.load(f))


# deserialization()
