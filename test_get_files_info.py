from functions.get_files_info import get_files_info

current_dir = get_files_info("calculator", ".")
pkg = get_files_info("calculator", "pkg")
bin_directory = get_files_info("calculator", "/bin")
parent_directory = get_files_info("calculator", "../")





print("Result for  current directory:")
print(current_dir)

print("Result for 'pkg' directory:")
print(pkg)

print("Result for '/bin' directory:")
print(bin_directory)

print("Result for '../' directory:")
print(parent_directory)
