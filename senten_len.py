import sys

def sentence_len(filepath):
	"""
	get the maxlen of sentence should set
	baseline maxlen 0.99%
	answer maxlen 137, comment maxlen 141, we set 140
	"""
	sen_lens = []
	with open(filepath, "r") as f:
		for line in f.readlines():
			sen_lens.append(len(line.split(' ')))
	sen_lens = sorted(sen_lens, reverse=False)
	avg_len = sum(sen_lens)/len(sen_lens)
	print("avg len:", avg_len)
	for i in [0.5, 0.6, 0.7, 0.8, 0.9, 0.99, 1.0]:
		index = int(i*len(sen_lens))-1
		print("{} %data len:{}".format(i, sen_lens[index]))

def main():
	filepath = sys.argv[1]
	sentence_len(filepath)


if __name__ == '__main__':
	main()