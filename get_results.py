import os
import numpy as np
import warnings

warnings.filterwarnings(action='ignore')
dir = './cifar10'

def print_from_log(exp_name, seeds=(1,2,3)):
    A_auc = []
    A_last = []
    A_cls_avg = []
    A_cls_last = []
    A_online = []
    train_auc = []
    train_last = []
    F_last = []
    IF_avg = []
    KG_avg = []
    FLOPS = []
    for i in seeds:
        f = open(f'{dir}/{exp_name}/seed_{i}.log', 'r')
        lines = f.readlines()
        cls_avg = []
        train_seed_last = 0
        for line in lines:
            if 'auc' in line:
                list = line.split(" | ")
                A_auc.append(float(list[0].split(" ")[-1])*100)
                A_last.append(float(list[2].split(" ")[-1])*100)
        A_cls_avg.append(np.mean(cls_avg))
        train_last.append(train_seed_last)
    if np.isnan(np.mean(A_auc)):
        pass
    else:
        # print(A_last)
        # print(A_cls_last)
        # print(train_last)
        print(f'Exp:{exp_name} \t\t\t {np.mean(A_auc):.2f}/{np.std(A_auc):.2f} \t {np.mean(A_last):.2f}/{np.std(A_last):.2f} \t  {np.mean(IF_avg):.2f}/{np.std(IF_avg):.2f}  \t  {np.mean(KG_avg):.2f}/{np.std(KG_avg):.2f}  \t  {np.mean(FLOPS):.2f}/{np.std(FLOPS):.2f}|')
        # print(f'CLS AVG Exp:{exp_name} \t\t\t {np.mean(A_cls_avg):.2f}/{np.std(A_cls_avg):.2f} \t {np.mean(A_cls_last):.2f}/{np.std(A_cls_last):.2f} \t  {np.mean(IF_avg):.2f}/{np.std(IF_avg):.2f}  \t  {np.mean(KG_avg):.2f}/{np.std(KG_avg):.2f}  \t  {np.mean(FLOPS):.2f}/{np.std(FLOPS):.2f}|')
        # print(f'REAL TIME Exp:{exp_name} \t\t\t {np.mean(train_auc):.2f}/{np.std(train_auc):.2f} \t {np.mean(train_last):.2f}/{np.std(train_last):.2f} \t  {np.mean(IF_avg):.2f}/{np.std(IF_avg):.2f}  \t  {np.mean(KG_avg):.2f}/{np.std(KG_avg):.2f}  \t  {np.mean(FLOPS):.2f}/{np.std(FLOPS):.2f}|')

print("A_auc, A_last, IF_avg, KG_avg FLOPS")

exp_list = sorted([exp for exp in os.listdir(dir)])

for exp in exp_list:
    try:
        print_from_log(exp)
    except:
        pass




