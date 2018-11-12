from glob import glob
import os
import sys

if __name__ == "__main__":
    csv_dir = "/cluster/scratch/sgokula/trained_pc_embeddings"
    files = glob(f"{csv_dir}/*.csv")
    print(len(files))

    for f in files:
        f = os.path.basename(f)
        bsub_cmd = (f"bsub -n 1 -J {f} -W 8:00 -o eval_op/{f}.OUT -R 'rusage[mem=4096]' "
                    f"-e eval_op/{f}.ERR './evaluate "
                    f"--graph wordnet/noun_closure.tsv --vectors {csv_dir}/{f} "
                    "--sample-seed 2 --include-map'")
        print(f"running {f}")
        os.system(bsub_cmd)
