from glob import glob
import os
import sys

if __name__ == "__main__":
    files = glob("embeddings/*.csv")

    for f in files:
        f = os.path.basename(f)
        bsub_cmd = (f"bsub -n 1 -J {f} -W 8:00 -o eval_op/{f}.OUT "
                    f"-e eval_op/{f}.ERR './evaluate "
                    f"--graph wordnet/noun_closure.tsv --vectors embeddings/{f} "
                    "--include-map'")
        print(f"running {f}")
        os.system(bsub_cmd)
