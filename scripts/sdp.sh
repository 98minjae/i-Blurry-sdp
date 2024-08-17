#/bin/bash

# CIL CONFIG
NOTE="sdp_10_50_lr_3e-4_trial3" # Short description of the experiment. (WARNING: logs/results with the same note will be overwritten!)
MODE="sdp"
DATASET="cifar10" # cifar10, cifar100, tinyimagenet, imagenet
N_TASKS=5
N=50
M=10
GPU_TRANSFORM="--gpu_transform"
USE_AMP="--use_amp"
SEEDS=("1" "2" "3")
GPU_IDS=("6" "6" "6")

if [ "$DATASET" == "cifar10" ]; then
    MEM_SIZE=500 ONLINE_ITER=1
    MODEL_NAME="resnet18" EVAL_PERIOD=100
    BATCHSIZE=16; LR=3e-4 OPT_NAME="adam" SCHED_NAME="default"

elif [ "$DATASET" == "cifar100" ]; then
    MEM_SIZE=2000 ONLINE_ITER=3
    MODEL_NAME="resnet34" EVAL_PERIOD=100
    BATCHSIZE=16; LR=3e-4 OPT_NAME="adam" SCHED_NAME="default"

elif [ "$DATASET" == "tinyimagenet" ]; then
    MEM_SIZE=4000 ONLINE_ITER=3
    MODEL_NAME="resnet34" EVAL_PERIOD=100
    BATCHSIZE=32; LR=3e-4 OPT_NAME="adam" SCHED_NAME="default"

elif [ "$DATASET" == "imagenet" ]; then
    N_TASKS=10 MEM_SIZE=20000 ONLINE_ITER=0.25
    MODEL_NAME="resnet34" EVAL_PERIOD=1000
    BATCHSIZE=256; LR=3e-4 OPT_NAME="adam" SCHED_NAME="default"

else
    echo "Undefined setting"
    exit 1
fi

for i in "${!SEEDS[@]}"; do
    RANDOM_SEED="${SEEDS[$i]}"
    GPU_ID="${GPU_IDS[$i]}"
    CUDA_VISIBLE_DEVICES=$GPU_ID nohup python main.py --mode $MODE \
    --dataset $DATASET \
    --n_tasks $N_TASKS --m $M --n $N \
    --rnd_seed $RANDOM_SEED \
    --model_name $MODEL_NAME --opt_name $OPT_NAME --sched_name $SCHED_NAME \
    --lr $LR --batchsize $BATCHSIZE \
    --memory_size $MEM_SIZE $GPU_TRANSFORM --online_iter $ONLINE_ITER \
    --note $NOTE --eval_period $EVAL_PERIOD $USE_AMP 2>&1 &
done
