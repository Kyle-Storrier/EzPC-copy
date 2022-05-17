import os

if __name__ == "__main__" :
	for dg in ["dense", "group"] :
		for sm in ["single", "multi"] :
			if dg == "group" and sm == "multi" :
				continue

			for nw in ["normal", "winograd"] :
				for ex in ["clear", "secure"] :
					os.system(f"python3 ../helper.py --root .. --filter 3 --dg {dg} --sm {sm} --exec {ex} --nw {nw}")
					os.system(f"python3 ../../../CompileONNXGraph.py --config config.json --role server")


	os.system("mv *.ezpc EzPC/")
	os.system("mv *.inp Weights/")
	os.system("mv *.cpp CPP/")