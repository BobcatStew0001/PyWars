#I chose to create all the information in variables and plug them in as and where they are needed. 
divider = "=" * 20
first_name = "Zach"
last_name = "Brown"
age = 42
city = "Brandon"
previous_career = "Industrial Generator Technician"
reason = "I am learning to code because it is something that puts my logical problem solving skills to use and also improves my income allowing me to provide a better life for my wife and kids."
fun_fact = "I coach youth soccer in the spring and have won the championship all 6 years."

print(divider)
print("Student Profile")
print(divider)#This is my string multiplication trick 
print(first_name)
print(last_name)
print(age)
print(city)
print(previous_career)
print(f"Why am I learning to code? {reason}")#I used the string interpolation here to make the program flow smoothly 
print(f"What is a fun fact about me? {fun_fact}")
