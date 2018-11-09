import os

if __name__ == "__main__":
    num_dims = [50, 100, 200, 300]
    num_negs = [50, 70]
    num_epochs = [500, 1000, 1500]

    for nd in num_dims:
        for nn in num_negs:
            for ne in num_epochs:
                config = f"pc_{nd}_d_{nn}_neg_{ne}_epoch"
                op_name = f"embeddings/{config}.csv"
                bi_name = f"embeddings/bi_{config}.csv"
                print(f"running {config}")
                burnin_cmd = (
                    f"./build/poincare -graph wordnet/noun_closure.tsv "
                    f"-output-vectors {bi_name} -start-lr 0.005 "
                    f"-end-lr 0.005 -dimension {nd} -epochs 50 "
                    f"-number-negatives {nn} -distribution-power 1 "
                    f"-threads 8")
                full_cmd = (
                    f"./build/poincare -graph wordnet/noun_closure.tsv "
                    f"-output-vectors {op_name} -input-vectors {bi_name} "
                    f"-start-lr 1. -end-lr 1.  -dimension {nd} "
                    f"-epochs {ne-50} -number-negatives {nn} "
                    "-distribution-power 0 -threads 8")
                cmd = " ".join([burnin_cmd, "&&", full_cmd])
                bsub_cmd = (f"bsub -n 4 -W 120:00 -o bsub_log/{config}.OUT "
                            f" -e bsub_log/{config}.ERR -J {config} '{cmd}'")
                os.system(bsub_cmd)
