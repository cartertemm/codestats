import fnmatch
import sys
import os
import argparse
import langs
import string

def lstrip(s):
	"""strip whitespace from the left hand side of a string, returning a tuple (string,	number_of_chars_stripped) for S"""
	num_stripped=0
	for i in s:
		#for bytes
		char=(chr(i) if type(i)==int else i)
		if char in string.whitespace:
			s=s[1:]
			num_stripped+=1
		else:
			break
	return (s, num_stripped)

def recursive(directory, wildcard):
	matches = []
	for root, dirnames, filenames in os.walk(directory):
		for filename in fnmatch.filter(filenames, wildcard):
			matches.append(os.path.join(root, filename))
	return matches

def bytes2human(n):
	symbols = ('KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
	prefix = {}
	for i, s in enumerate(symbols):
		prefix[s] = 1 << (i + 1) * 10
	for s in reversed(symbols):
		if n >= prefix[s]:
			value = float(n) / prefix[s]
			return '%.1f%s' % (value, s)
	return "%sB" % n

parser=argparse.ArgumentParser(description="Tool to provide detailed summaries of code in a project.")
parser.add_argument("dir", help="directory to search")
parser.add_argument("-e", "--exclude", dest="excludes", action="append", default=[], help="adds a wildcard exclusion")
parser.add_argument("-ef", "--exclude-file", help="Path to a file containing a list of excludes to be processed seperated by \\n")
parser.add_argument("-v", "--verbose", action="store_true", help="give args.verbose/more detailed output")
parser.add_argument("-dr", "--disable-rundown", action="store_true", help="excludes an individual rundown of every processed file")
args=parser.parse_args()

if not os.path.isdir(args.dir):
	print("error, invalid directory provided")
	sys.exit()
if args.verbose:
	print(f"running on {args.dir} with verbose output")
if args.exclude_file and os.path.isfile(args.exclude_file):
	if args.verbose:
		print(f"found exclude file: {args.exclude_file}")
	f=open("excludes.txt", "r")
	excludes_txt=f.read().split("\n")
	f.close()
	excludes_txt=[i for i in excludes_txt if i]
	args.excludes+=excludes_txt
	if args.verbose:
		print(f"contains {len(excludes_txt)} exclusions")

if args.verbose:
	print("loaded a total of "+str(len(args.excludes))+" exclusion"+("s" if len(args.excludes)!=1 else ""))

total_lines=0
total_whitespace=0
total_size =0
total_indents=0
line_amounts=[0, 0]
files={}
directory=recursive(args.dir, "*")
if args.verbose:
	print(f"{len(args.dir)} files found in directory, now scanning...")
num_excluded=0
for i in directory:
	#os.path.splitext only returns the last component
	ext=i.split("/")[-1]
	ext=ext[ext.find("."):]
	exclude=False
	if i in args.excludes:
		exclude=True
	else:
		for ex in args.excludes:
			if fnmatch.fnmatch(i, ex):
				exclude=True
				break
	if exclude:
		if args.verbose:
			print("skipping: "+i+" due to exclude")
		num_excluded+=1
		continue
	lang=langs.detect_lang(i)
	if not lang:
		if args.verbose:
			print("unknown language from file "+i+". No info will be provided. Continuing")
		continue
	f=open(i, "rb")
	content=f.read()
	size=len(content)
	total_size+=size
	lines=content.split(b"\n")
	total_lines+=len(lines)
	whitespace=0
	indent=0
	for line in lines:
		if line==b"" or line==b"\r":
			whitespace+=1
		else:
			line_amounts[0]+=1
			line_amounts[1]+=len(line)
		indent+=lstrip(line)[1]
	total_indents+=indent
	total_whitespace+=whitespace
	f.close()
	files[i]=[lang, len(lines), size, indent, whitespace]

print(f"{len(files)} files accounted for, with {num_excluded} exclusions encountered")
if len(files)==0:
	print("no stats to show")
	sys.exit()
#calculate percentages per language
lang_amounts={}
for i in files.values():
	if i[0] in lang_amounts:
		lang_amounts[i[0]]+=i[2]
	else:
		lang_amounts[i[0]]=i[2]
for i in lang_amounts:
	print(f"{i}: {round((lang_amounts[i]/total_size)*100, 2)}%")
print(f"total lines: {total_lines}")
print(f"number of blank lines: {total_whitespace}")
print(f"total lines that have content: {total_lines-total_whitespace}")
print(f"average number of characters per line: {round(line_amounts[1]/line_amounts[0], 2)}")
print(f"average number of lines per file: {round(total_lines/len(files), 2)}")
print(f"total number of proceeding spaces/indents: {total_indents}, making up a total of {bytes2human(total_indents)}")
print(f"average indents per file: {round(total_indents/len(files), 2)}")
print(f"total size: {bytes2human(total_size)}, {total_size}b")
without_indents=total_size-total_indents
print(f"total size without indents: {bytes2human(without_indents)}, {without_indents}b")
print(f"average file size: {bytes2human(total_size/len(files))}, {round(total_size/len(files), 2)}b")
print(f"average file size without indents: {bytes2human(without_indents/len(files))}, {round(without_indents/len(files), 2)}b")

if not args.disable_rundown:
	print("individual rundown:")
	for i in files:
		print(f"{i}, {files[i][0].name}, {files[i][1]} lines, {bytes2human(files[i][2])}, {files[i][2]}b")
