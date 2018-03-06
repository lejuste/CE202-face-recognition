import os

print 'shrinking..'

os.system('python file_shrink.py thread_1_size_1.txt')
os.system('python file_shrink.py thread_1_size_4.txt')
os.system('python file_shrink.py thread_1_size_16.txt')
os.system('python file_shrink.py thread_1_size_64.txt')
os.system('python file_shrink.py thread_1_size_256.txt')

os.system('python file_shrink.py thread_2_size_1.txt')
os.system('python file_shrink.py thread_2_size_4.txt')
os.system('python file_shrink.py thread_2_size_16.txt')
os.system('python file_shrink.py thread_2_size_64.txt')
os.system('python file_shrink.py thread_2_size_256.txt')

os.system('python file_shrink.py thread_4_size_1.txt')
os.system('python file_shrink.py thread_4_size_4.txt')
os.system('python file_shrink.py thread_4_size_16.txt')
os.system('python file_shrink.py thread_4_size_64.txt')
os.system('python file_shrink.py thread_4_size_256.txt')

os.system('python file_shrink.py thread_8_size_1.txt')
os.system('python file_shrink.py thread_8_size_4.txt')
os.system('python file_shrink.py thread_8_size_16.txt')
os.system('python file_shrink.py thread_8_size_64.txt')
os.system('python file_shrink.py thread_8_size_256.txt')
