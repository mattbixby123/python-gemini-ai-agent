from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

def main():
  working_dir = "calculator"
  # print(write_file(working_dir, "lorem.txt", "wait, this isn't lorem ipsum"))
  # print(write_file(working_dir, "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
  # print(write_file(working_dir, "/tmp/temp.txt", "this should not be allowed"))
  # print(write_file(working_dir, "pkg2/temp.txt", "this should be allowed"))

  # print(get_file_content(working_dir, "main.py"))
  # print(get_file_content(working_dir, "pkg/calculator.py"))
  # print(get_file_content(working_dir, "pkg/notexists.py"))
  # print(get_file_content(working_dir, "/bin/cat"))

main()