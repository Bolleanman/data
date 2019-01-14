import sys


def process_token(src_file, tar_file):
	with open(src_file, "r") as srcfile, open(tar_file, "w", encoding='utf-8') as tarfile:
		for lid, line in enumerate(srcfile.readlines()):
			# print(line)
			if "\\" in line:
				line = line.replace('\\', '')
			line = line.replace('[', '')
			line = line.replace(']', '')
			# print(line)
			line = " ".join([i for i in line])
			# print(line)
			tarfile.write(line)
			# if lid==3: return
	print('done')


def main():
	src_file = sys.argv[1]
	tar_file = sys.argv[2]
	print(src_file, tar_file)
	process_token(src_file, tar_file)


if __name__ == '__main__':
	main()
