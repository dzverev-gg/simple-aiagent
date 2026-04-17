from functions.get_file_content import get_file_content



current_main = get_file_content("calculator", "main.py")
pkg_calc = get_file_content("calculator", "pkg/calculator.py")
bin_cat_file = get_file_content("calculator", "/bin/cat")
non_existing_file = get_file_content("calculator", "pkg/does_net_exist.py")





print("Result for  main.py:")
print(current_main)

print("Result for 'pkg/calculator.py':")
print(pkg_calc)

print("Result for '/bin/cat' file:")
print(bin_cat_file)

print("Result for 'pkg/does_not_exist.py' file:")
print(non_existing_file)
