import time


start_time_file1 = time.time()
exec(open('json_to_yaml_1.py').read())
end_time_file1 = time.time()
execution_time_file1 = end_time_file1 - start_time_file1
print("Время выполнения задания 1:", execution_time_file1 * 100, "s")


start_time_file2 = time.time()
exec(open('json_to_yaml_2.1.py').read())
end_time_file2 = time.time()
execution_time_file2 = end_time_file2 - start_time_file2
print("Время выполнения допа 1:", execution_time_file2 * 100, "s")

start_time_file3 = time.time()
exec(open('json_to_yaml_2.2.py').read())
end_time_file3 = time.time()
execution_time_file3 = end_time_file3 - start_time_file3
print("Время выполнения допа 2:", execution_time_file3 * 100, "s")

start_time_file4 = time.time()
exec(open('json_to_yaml_2.3.py').read())
end_time_file4 = time.time()
execution_time_file4 = end_time_file4 - start_time_file4
print("Время выполнения допа 3:", execution_time_file4 * 100, "s")