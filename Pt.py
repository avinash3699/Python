# program to find "what is the programming language used" by the user

print("Hello, Enter the code to print 'Hello World' in your preferred Language and I will find the Language you have used\n")
print("You can write among the following languages given below")
print(" -> Java \n -> Python \n -> C \n -> C++ \n -> Ruby \n -> Pascal \n -> JavaScript \n -> R \n -> AppleScript \n -> Php \n -> C# \n -> COBOL\n")
print("Enter 'Finished' once you have completed your code\n")

#getting input code from the user
input_code = ""
not_finished = True 
while(not_finished):
	input_line = input().strip()
	if(input_line.upper() == "FINISHED"):
		not_finished = False
	else:
		input_code += input_line

# to find the programming language used
language_used = ""
if("printf" in input_code and ".h" in input_code and "#include" in input_code):
	language_used = "C"
elif("cout" in input_code or "printf" in input_code and "#include" in input_code):
	language_used = "C++"
elif("System" in input_code):
	language_used = "Java"
elif("print(" in input_code):
        language_used = "Python"
elif("php" in input_code and "echo" in input_code):
        language_used = "Php"
elif("puts" in input_code):
        language_used = "Ruby"
elif("Console.WriteLine" in input_code):
        language_used = "C#"
elif("console.log" in input_code):
        language_used = "JavaScript"
elif("begin" in input_code and "Write" in input_code):
        language_used = "Pascal"
elif("say" in input_code and ";" not in input_code):
        language_used = "AppleScript"
elif("DISPLAY" in input_code):
        language_used = "COBOL"
elif("cat" in input_code):
        language_used = "R"
else:
        pass
        

# print the output
if language_used:
        print(language_used + " is the Programming Language Used")
        print("I hope the guessed answer is correct")
else:
        print("Please Look at your code for any mistakes")
	
