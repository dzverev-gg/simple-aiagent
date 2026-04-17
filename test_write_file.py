from functions.write_file import write_file



lorem_write = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
pkg_morelorem_write = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
not_allowed_write = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")



print("Resut for lorem write test:")
print(lorem_write)

print("Result for pkg_lorem write test:")
print(pkg_morelorem_write)

print("Result for not allowed write:")
print(not_allowed_write)
