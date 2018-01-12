from sys import argv 
script, in_file, out_file = argv 
in_file = open(in_file)
content = in_file.read()
out_file = open(out_file, 'w')
out_file.write(content)
in_file.close()
out_file.close()
