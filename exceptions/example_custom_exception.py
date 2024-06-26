class CustomException(Exception):
    def __init__(self):
        message = "The divisor cannot be zero"
        super().__init__(message)


a = 3
b = [1, 0, 2]
for elem in b:
    if elem == 0:
        raise CustomException()
    result = a / elem
    print(f"Result is: {result}")
