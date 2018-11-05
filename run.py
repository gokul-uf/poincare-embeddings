import os
import sys

if __name__ == "__main__":
    num_dims = [50, 100, 200, 300]
    num_negs = [50, 60, 70, 100]
    num_epochs = [1500, 1000, 500]

    for nd in num_dims:
        for nn in num_negs:
            for ne in num_epochs:
                op_name = f"../embeddings/pc_{nd}_d_{nn}_neg_{ne}.csv"
                print(f"running {op_name}")
                print("burnin")
                cmd = (f"./poincare -graph ../wordnet/noun_closure.tsv "
                        f"-output-vectors {op_name} -start-lr 0.005 "
                        f"-end-lr 0.005 -dimension {nd} -epochs 50 "
                        f"-number-negatives {nn} -distribution-power 1 "
                        f"-threads 8")
                os.system(cmd)
                cmd = (f"./poincare -graph ../wordnet/noun_closure.tsv "
                        f"-output-vectors {op_name} -input-vectors {op_name} "
                        f"-start-lr 0.5 -end-lr 0.5  -dimension {nd} "
                        f"-epochs {ne-50} -number-negatives {nn} "
                        "-distribution-power 0 -threads 8")
                print("full run")
                os.system(cmd)


