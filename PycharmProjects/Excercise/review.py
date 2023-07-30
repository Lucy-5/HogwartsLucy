# 9.1
# class Restaurant:
#     """餐厅"""
#     def __init__(self,restaurant_name,cuisine_type):
#         """初始化餐馆名和类型"""
#         self.restaurant_name=restaurant_name
#         self.cuisine_type=cuisine_type
#
#     def describe_restaurant(self):
#         """描述餐厅"""
#         print(f"restaurant name:{self.restaurant_name}")
#         print(f"cuisine type:{self.cuisine_type}")
#
#     def open_restaurant(self):
#         """营业中"""
#         print("opening now.")
#
# kfc=Restaurant('KFC','fastfood')
# kfc.describe_restaurant()
# kfc.open_restaurant()
#
# 9.2
# juicy=Restaurant('Juicy','juice')
# juicy.describe_restaurant()
# juicy.open_restaurant()

# class User:
#     """储存用户信息"""
#     def __init__(self,first_name,last_name,age,gender,location):
#         """初始化用户"""
#         self.first=first_name
#         self.last=last_name
#         self.age=age
#         self.gender=gender
#         self.location=location
#         self.friends=9
#     def describe_user(self):
#         print(f"username:{self.first} {self.last}\n"
#               f"- {self.age} years old\n- {self.gender}\n- {self.location}")
#     def greet_user(self):
#         print(f"Welcome {self.first}!")
#     def hometown(self):
#         print(f"You come from {self.friends}")
#
# lucy=User('Lucy','S','18','female','Shanghai')
# lucy.describe_user()
# lucy.greet_user()
# lucy.hometown()
# # Lucy.friends()
# print(lucy.friends)
#
# class Restaurant:
#     """餐厅"""
#     def __init__(self,restaurant_name,cuisine_type):
#         """初始化餐馆名和类型"""
#         self.restaurant_name=restaurant_name
#         self.cuisine_type=cuisine_type
#         self.number_served=0
#
#     def describe_restaurant(self):
#         """描述餐厅"""
#         print(f"restaurant name:{self.restaurant_name}")
#         print(f"cuisine type:{self.cuisine_type}")
#
#     def open_restaurant(self):
#         """营业中"""
#         print("opening now.")
#
#     def set_number_served(self,value):
#         """设置值"""
#         self.number_served=value
#
#     def increment_number_served(self,increment):
#         """增加值"""
#         if increment > self.number_served:
#             self.number_served += increment
#         else:
#             print(f"You can't roll back")
#
#     def number_print(self):
#         """打印已提供的数目"""
#         print(f'number_served:{self.number_served}')
#
#
# kfc=Restaurant('KFC','fastfood')
# kfc.describe_restaurant()
# kfc.open_restaurant()
# kfc.set_number_served(10)
# kfc.number_print()
# kfc.increment_number_served(3)
# kfc.number_print()
#
# class User:
#     """储存用户信息"""
#     def __init__(self,first_name,last_name,age,gender,location):
#         """初始化用户"""
#         self.first=first_name
#         self.last=last_name
#         self.age=age
#         self.gender=gender
#         self.location=location
#         self.login_attempts=0
#
#     def describe_user(self):
#         print(f"username:{self.first} {self.last}\n"
#               f"- {self.age} years old\n- {self.gender}\n- {self.location}")
#
#     def greet_user(self):
#         print(f"Welcome {self.first}!")
#
#     def increment_login_attempts(self):
#         self.login_attempts+=1
#         print(f"login_attempts:{self.login_attempts}")
#
#     def reset_login_attempts(self):
#         self.login_attempts=0
#         print(f"login_attempts:{self.login_attempts}")
#
# lucy=User('Lucy','S','18','female','Shanghai')
# lucy.describe_user()
# lucy.greet_user()
# lucy.increment_login_attempts()
# lucy.increment_login_attempts()
# lucy.increment_login_attempts()
# lucy.reset_login_attempts()
#
# class Restaurant:
#     """餐厅"""
#     def __init__(self,restaurant_name,cuisine_type):
#         """初始化餐馆名和类型"""
#         self.restaurant_name=restaurant_name
#         self.cuisine_type=cuisine_type
#         self.number_served=0
#
#     def describe_restaurant(self):
#         """描述餐厅"""
#         print(f"restaurant name:{self.restaurant_name}")
#         print(f"cuisine type:{self.cuisine_type}")
#
#     def open_restaurant(self):
#         """营业中"""
#         print("opening now.")
#
#     def set_number_served(self,value):
#         """设置值"""
#         self.number_served=value
#
#     def increment_number_served(self,increment):
#         """增加值"""
#         if increment > self.number_served:
#             self.number_served += increment
#         else:
#             print(f"You can't roll back")
#
#     def number_print(self):
#         """打印已提供的数目"""
#         print(f'number_served:{self.number_served}')
#
#
# class IceCreamStand(Restaurant):
#     """子类"""
#     def __init__(self,restaurant_name,cuisine_type='icecream'):
#         """初始化餐馆名和类型"""
#         self.restaurant_name=restaurant_name
#         self.cuisine_type=cuisine_type
#         super().__init__(restaurant_name,cuisine_type)
#         self.flavors=[]
#     def show_flavors(self):
#         """显示正在出售的冰淇凌品种"""
#         for flavor in self.flavors:
#             print(f'{flavor.title()}')
#
# kfc=IceCreamStand('KFC')
# kfc.flavors=['apple','banana','chocolete']
# kfc.describe_restaurant()
# kfc.open_restaurant()
# kfc.set_number_served(10)
# kfc.number_print()
# kfc.show_flavors()
#
# class User:
#     """储存用户信息"""
#     def __init__(self,first_name,last_name,age,gender,location):
#         """初始化用户"""
#         self.first=first_name
#         self.last=last_name
#         self.age=age
#         self.gender=gender
#         self.location=location
#         self.login_attempts=0
#
#     def describe_user(self):
#         print(f"username:{self.first} {self.last}\n"
#               f"- {self.age} years old\n- {self.gender}\n- {self.location}")
#
#     def greet_user(self):
#         print(f"Welcome {self.first}!")
#
#     def increment_login_attempts(self):
#         self.login_attempts+=1
#         print(f"login_attempts:{self.login_attempts}")
#
#     def reset_login_attempts(self):
#         self.login_attempts=0
#         print(f"login_attempts:{self.login_attempts}")
#
# lucy=User('Lucy','S','18','female','Shanghai')
# lucy.describe_user()
# lucy.greet_user()
# lucy.increment_login_attempts()
# lucy.increment_login_attempts()
# lucy.increment_login_attempts()
# lucy.reset_login_attempts()
#
#
# class User:
#     """储存用户信息"""
#     def __init__(self,first_name,last_name,age,gender,location):
#         """初始化用户"""
#         self.first=first_name
#         self.last=last_name
#         self.age=age
#         self.gender=gender
#         self.location=location
#         self.login_attempts=0
#
#     def describe_user(self):
#         print(f"username:{self.first} {self.last}\n"
#               f"- {self.age} years old\n- {self.gender}\n- {self.location}")
#
#     def greet_user(self):
#         print(f"Welcome {self.first}!")
#
#     def increment_login_attempts(self):
#         self.login_attempts+=1
#         print(f"login_attempts:{self.login_attempts}")
#
#     def reset_login_attempts(self):
#         self.login_attempts=0
#         print(f"login_attempts:{self.login_attempts}")
#
# class Admin(User):
#     """管理员"""
#
#     def __init__(self, first_name, last_name, age, gender, location):
#         """初始化用户"""
#         self.first = first_name
#         self.last = last_name
#         self.age = age
#         self.gender = gender
#         self.location = location
#         self.login_attempts = 0
#         super().__init__(first_name, last_name, age, gender, location)
#         self.privileges=["can add post","can delete post","can ban user"]
#
#     def show_privileges(self):
#         for privilege in self.privileges:
#             print(f"-{privilege}")
#
# eric = Admin('eric', 'matthes', 9, 'male', 'UK')
# eric.describe_user()
# eric.privileges = [
# 'can reset passwords',
# 'can moderate discussions',]
# eric.show_privileges()
