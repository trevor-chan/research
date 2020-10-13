import glob
from sys import argv

assert len(argv) > 1, "(directory containing lineages) (optional: output jobfile name .txt)"
directory_name = argv[1]

if len(argv) == 2:
    outfile = open("lineage_jobfile.txt","w")
elif len(argv) == 3:
    outfile = open(argv[2],"w")
else:
    print("additional args ignored")

for path_name in glob.glob(directory_name + '/*[!.lineage]'):
    outfile.write(f'python compute_lineage.py {path_name}\n')

outfile.close()
