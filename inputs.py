# def weather_conditions(temperatures):
#     if temperatures > 7:
#         return "Warm"
#     else:
#         return "Cold"
    
# user_input = float(input("Enter Temperature: "))
# print(weather_conditions((user_input)))

# user_input = input("Enter your name:\n")
# message = "Hello %s!" % user_input
# # message = f"Hello {user_input}!"
# print(message.title())

# name = "Edu"
# surname = "Chiang"
# message = "Your name is {}. Your Surname is {}".format(name, surname)
# print(message)
name = input(f"Enter your name: ")
experience_month = input("Enter your experience in months: ")
experience_years = int(experience_month) / 12
print("Hi {}, you have {} years of expereance".format(name.title(), experience_years))