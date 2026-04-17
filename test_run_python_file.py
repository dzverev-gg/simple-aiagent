from functions.run_python_file import run_python_file


run_main = run_python_file("calculator", "main.py")
run_main_with_args = run_python_file("calculator", "main.py", ["3 + 5"])
run_tests = run_python_file("calculator", "tests.py")
run_outside = run_python_file("calculator", "../main.py")
run_nonexistant = run_python_file("calculator", "nonexistent.py")
run_lorem = run_python_file("calculator", "lorem.txt")



print("Result for main.py file run")
print(run_main)

print("Result for main.py file with args run")
print(run_main_with_args)

print("Result for tests.py file run")
print(run_tests)

print("Result for outside file run")
print(run_outside)

print("Result for nonexistent file run")
print(run_nonexistant)

print("Result for non python file run")
print(run_lorem)
