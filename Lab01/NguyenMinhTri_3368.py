#Biến
x=10 #Biến x lưu trữ giá trị số nguyên 10
name = "Alice" #Biến name lưu chữ chuỗi "Alice"
is_valid = True #Biến is_valid lưu trữ giá trị boolean True if = 5 #Lỗi! "if" là từ khoá, không thể sử dụng làm tên biến 

#Cộng (+)
a= 5
b = 3
result = a + b #Kết quả: 8
#Trừ (-)
a = 8
b = 4
result = a-b  #Kết quả: 4
#Nhân (*)
a=6
b=7
result = a * b #Kết quả: 42
#Chia(/)
a= 20
b= 5
result = a/b #Kết quả: 4.0
#Chia lấy phần nguyên 
a= 20
b= 3
result = a//b #Kết quả: 6
#Chia lấy dư
a= 20
b= 7
remainder = a%b #Kết quả: 6
#Luỹ Thừa
a= 2
b= 3
result = a**b #Kết quả: 8 (2^3=8)

#Các toán từ logic
#AND
x = 5
y = 3
result = (x > 2) and (y < 4) #Kết quả: True
#OR
x = 5
y = 3
result = (x > 2) or (y > 4) #Kết quả: True
#NOT
x = 5
result = not (x == 5) #Kết quả: False
#==
x= 5 
result = ( x == 5) #Kết quả: True
#!=
x= 5 
result = ( x != 3) #Kết quả: True
#SS (>),(<)
x= 5 
result1 = ( x > 3) #Kết quả: True
result2 = ( x < 3) #Kết quả: False
#SS ()>=),(<=)
x= 5 
result1 = ( x >= 3) #Kết quả: True
result2 = ( x <= 3) #Kết quả: False

#Input,Print
name = input ("Pham Hong Le Vu")
print("Xin chào,",name)

age=25
print("Tuổi của bạn là :",age)

print("python", "là", "ngôn", "ngữ", "lập", "trình",sep="-")
print("Xin chào",end=" ")
print("Các bạn!")#

#Các cấu trúc điều khiển

#Câu lệnh điều kiện(Conditional Statements)
x =10
if x > 5:
    print("x lớn hơn 5")
elif x == 5:
    print("x bằng 5")
else:
    print("x nhỏ hơn 5")
#Vòng lặp (Loops):
#for
fruits = ["Apple","banana","cherry"]
for fruit in fruits:
    print(fruit)
#while
count = 0
while count < 5:
    print(count)
    count += 1

#Câu lệnh nhảy(Jump Statements)
#break(Tìm số chia hết cho 5 đầu tiên trong khoảng từ 1 đến 100)
for i in range(1,101):
    if i%5 == 0:
        print("Số chia hết cho 5 đầu tiên là:",i)
        break
#countiue (In ra các số chẵn từ 1 đến 10 và bỏ qua các số lẻ)
for i in range(1,11):
    if i%2 !=0:
        continue
    print(i)
#pass (Kiểm tra điều kiện, nếu đúng thực hiện, nếu sai thì không làm gì)
x=5
if x >10:
    print("x lớn hơn 10")
else:
    pass

#Chuỗi
#Khai báo chuỗi
#Sử dụng dấu ngoặc đơn
string_single_quotes = 'Đây là một chuỗi sử dụng dấu ngoặc đơn.'
#Sử dụng dấu ngoặc kép
string_double_quotes = "Đây là một chuỗi sử dụng dấU ngoặc kép"
#Sử dụng dấu ngoặc ba
string_triple_quotes = '''Đây là một chuỗi 
sử dụng dấU ngoặc ba,
có thể trải dài qua nhiều dòng'''
#Truy cập ký tự chuỗi
my_string = "Hello,world!"
print(my_string[0])#Kết quả :'H'
print(my_string[7])#Kết quả :'W'
#Các phép xử lý chuỗi trong python
my_string = "Hello,world!"
print(my_string[7:])#Lấy từ ký tự thứ 7 đến hết : Kết quả :'World'
print(my_string[:5])#Lấy từ đầu thứ 7 đến ký tự thứ 4 : Kết quả :'Hello'
print(my_string[3:8])#Lấy từ ký tự thứ 3 đến ký tự thứ 7 : Kết quả :'lo, W'
#Ghép chuỗi
string1= "Hello"
string2 = "World"
concatenated_string = string1 + " " +string2 #Kết quả :'Hello World'
#Đọ dài chuỗi "len()"
my_string = "Hello, World!"
length = len(my_string) #Kết quả: 13

#Hàm xử lý chuỗi
my_string = "    Hello, World!    "
print(my_string.strip()) # Loại bỏ khoảng trắng: Kết quả: 'Hello, World!'
my_string = "Hello, World!"
print(my_string.split(",")) # Phân tách chuỗi: Kết quả: ['Hello', ' World!']
my_string = "Hello, World!"
print(my_string.replace("Hello", "Hi")) # Thay thế chuỗi: Kết quả: 'Hi, World!'

#Hàm
#Khai báo hàm
def my_function(parameter1, parameter2):
    # Khối mã của hàm
    # Thực hiện các hoạt động dựa trên tham số được truyền vào
    result = parameter1 + parameter2
    return result
#Phân loại hàm
result = my_function(10, 20)  # Gọi hàm và lưu kết quả vào biến result
print(result)  # In kết quả của hàm
# Định nghĩa hàm tính tổng
def calculate_sum(a, b):
    result = a + b
    return result
# Gọi hàm và lưu kết quả vào biến
sum_result = calculate_sum(10, 20)
# In kết quả
print("Tổng hai số là:", sum_result)
# Hàm không trả về giá trị, chỉ in ra thông báo
def greet(name):
    print("Xin chào,", name)
# Gọi hàm
greet("Alice")

#Mảng Array
from array import array
# Khai báo một mảng số nguyên
int_array = array('i', [1, 2, 3, 4, 5])
# Khai báo một mảng số thực
float_array = array('f', [3.14, 2.5, 6.7])
#Kiểu dữ liệu (Typecodes)
print(int_array[0])  # Truy cập phần tử đầu tiên của mảng số nguyên
print(float_array[2])  # Truy cập phần tử thứ ba của mảng số thực
# Cập nhật giá trị của phần tử trong mảng:
int_array[2] = 10
# Cập nhật giá trị của phần tử thứ ba trong mảng số nguyên
#Module"array" cung cấp phương thức
int_array.append(6)  # Thêm phần tử 6 vào cuối mảng số nguyên
float_array.remove(6.7)  # Xóa phần tử 6.7 khỏi mảng số thực


#List
# Khai báo danh sách (List)
my_list = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
mixed_list = [10, "hello", 3.14, True]

# Truy cập vào phần tử trong danh sách
print(my_list[0])  # Kết quả: 1
print(names[2])  # Kết quả: 'Charlie'

# Cập nhật giá trị của phần tử trong danh sách
my_list[1] = 20
print(my_list)  # Kết quả: [1, 20, 3, 4, 5]

# Thêm phần tử vào danh sách
names.append("David")
print(names)  # Kết quả: ['Alice', 'Bob', 'Charlie', 'David']

# Xóa phần tử khỏi danh sách
del my_list[2]
print(my_list)  # Kết quả: [1, 20, 4, 5]
# Duyệt qua từng phần tử trong danh sách
for element in names:
    print(element)  # In từng phần tử trong danh sách

#Kiểu tuple
# Khai báo Tuple
my_tuple = (1, 2, 3, 4, 5)
names = ("Alice", "Bob", "Charlie")
mixed_tuple = (10, "hello", 3.14)

# Truy cập vào phần tử trong Tuple
print(my_tuple[0])  # Kết quả: 1
print(names[2])  # Kết quả: 'Charlie'

# Các phương thức trong Tuple
#Count
my_tuple = (1, 2, 3, 1, 4, 1)
print(my_tuple.count(1))  # Đếm số lần xuất hiện của 1: Kết quả: 3
#Index
my_tuple = ('a', 'b', 'c', 'd', 'b')
print(my_tuple.index('b'))  # Trả về chỉ số đầu tiên của 'b': Kết quả: 1

#Dictionary
# Khai báo dictionary
my_dict = {}  # Dictionary rỗng
person = {"name": "Alice", "age": 25, "city": "New York"}

# Truy cập vào giá trị trong dictionary
print(person["name"])  # Kết quả: "Alice"
print(person["age"])   # Kết quả: 25

# Thêm hoặc cập nhật giá trị trong dictionary
person["email"] = "alice@example.com"  # Thêm một key mới
person["age"] = 26  # Cập nhật giá trị của key

# Xóa một phần tử trong dictionary
del person["city"]  # Xóa phần tử với key "city"
age = person.pop("age")  # Xóa phần tử và lấy giá trị của key "age"

# Các phương thức của dictionary
print(person.keys())   # Lấy tất cả các keys
print(person.values()) # Lấy tất cả các values
print(person.items())  # Lấy tất cả các cặp key-value dưới dạng tuple

#OOP trong python
#Class, Object
# Định nghĩa một lớp đơn giản
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def get_info(self):
        return f"{self.brand} {self.model}"

# Tạo đối tượng từ lớp Car
my_car = Car("Toyota", "Corolla")
# Gọi phương thức của đối tượng
print(my_car.get_info())  # Kết quả: Toyota Corolla
#Contructor
class ClassName:
    def __init__(self, parameter1, parameter2):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def get_info(self):
        return f'{self.brand} {self.model}'

# Tạo một đối tượng từ lớp Car và truy xuất thông tin
my_car = Car("Toyota", "Corolla")
print(my_car.get_info())  # Kết quả: Toyota Corolla

#Attributes
# Định nghĩa thuộc tính trong Python
class ClassName:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1  # Thuộc tính instance
        self.attribute2 = attribute2  # Thuộc tính instance
    class_attribute = "Class Attribute"  # Thuộc tính lớp
# Truy cập thuộc tính trong Python
# Tạo đối tượng từ lớp và truy cập các thuộc tính
object_name = ClassName(value1, value2)
print(object_name.attribute1)    # Truy cập thuộc tính instance
print(object_name.class_attribute) # Truy cập thuộc tính lớp

#Methods
class ClassName:
    def method_name(self, parameter1, parameter2):
        # Các thao tác hoặc xử lý
        return something  # Trả về kết quả (nếu cần)
# Tạo đối tượng từ lớp và gọi phương thức
object_name = ClassName()
# Gọi phương thức và truyền các tham số
object_name.method_name(value1, value2)

#Kế thừa Inheritance
class Animal: #Khai báo lớp Animal
    def __init__(self, name): #Hàm khởi tạo
        self.name = name; #Khai báo thuộc tính name
    def speak(self): #Hàm speak
        print(f"{self.name} makes a sound"); #Xuất ra "name makes a sound"
class Dog(Animal): #Kế thừa lớp Animal
    def speak(self): #Hàm speak
        print(f"{self.name} barks"); #Xuất ra "name barks"
#Đa kế thừa (Multiple Inheritance)
class Bird: #Khai báo lớp Bird
    def fly(self): #Hàm fly
        print(f"{self.name} flies"); #Xuất ra "name flies"
class Parrot(Dog, Bird): #Kế thừa lớp Dog và Bird
    def speak(self): #Hàm speak
        print(f"{self.name} talks"); #Xuất ra "name talks"

#Đa hình (Polymorphism)
#Đa hình ở thời điểm biên dịch (Compile-time Polymorphism):
#overloading
class Calculation:
    def add(self, a, b):
        return a + b
    def add(self, a, b, c):
        return a + b + c
#overriding
class Animal:
    def make_sound(self):
        return "Generic sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"
#Đa hình tại thời điểm chạy (Runtime Polymorphism)
class Animal:
    def make_sound(self):
        return "Generic sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Đa hình tại thời điểm chạy
def animal_sound(animal):
    return animal.make_sound()

dog = Dog()
cat = Cat()
print(animal_sound(dog))  # Kết quả: Woof!
print(animal_sound(cat))  # Kết quả: Meow!

#Trừu tượng hóa (Abstraction)
from abc import ABC, abstractmethod

# Lớp trừu tượng
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

# Lớp con thực hiện (định nghĩa phương thức cụ thể)
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# Lớp con thực hiện (định nghĩa phương thức cụ thể)
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Sử dụng các đối tượng trừu tượng
dog = Dog()
cat = Cat()
print(dog.make_sound())  
print(cat.make_sound())  