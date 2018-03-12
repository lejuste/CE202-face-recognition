THREAD=$1
SIZE=$2

#Run program by: ./run1.sh 1 64
#First argument is threads options (1,2,4,8)
#Second argument is size (1,4,16,64,256)

echo thread: $Thread
echo size: $SIZE
echo Starting Throughput Benchmark

#--------------------------------------------------------------------------------------------All Threads Size 1--------------------------------------------------------------------------------------------
echo Running Threads $THREAD size x/$SIZE
sudo perf stat -D 5 -I 100 -e L1-dcache-load-misses,l2_rqsts.miss,branch-misses,branch-instructions,instructions,mem_load_uops_retired.l3_miss,cpu-cycles,LLC-load-misses -x, -o output.csv sudo docker run -e threadCount=$THREAD -e SIZE=$SIZE jusclee/ce-202:firstTry
python ce202-jusclee/CE202-face-recognition/interval-normalize.py output.csv --output new.csv
python ce202-jusclee/CE202-face-recognition/plot-normalized-mpki.py new.csv --title "Threads $THREAD Size x/$SIZE MPKI" -y "Misses per 1000 Instructions" --output "Thread-$THREAD-Size-$SIZE-mpki.png"
python ce202-jusclee/CE202-face-recognition/plot-normalized-ipc.py new.csv --title "Threads $THREAD Size x/$SIZE IPC" -y "Instructions per Cycles" --output "Thread-$THREAD-Size-$SIZE-ipc.png"

