#running the docker image script



 #1095  sudo docker build -t ez1 .
 #1096  sudo docker run -e threadCount=1212 -e SIZE=-12  ez1


#sudo docker run -e threadCount=1212 -e SIZE=-12  ez1



#python runThreads.py -t 1212 --program "python throughPutRun.py -t 1212 -s -12"


#run perf on my shit

#run perf on this image with this thread and size -> get a png chart? or just a csv

#then plot that bull shit

#sudo docker run -e threadCount=4 -e SIZE=64 jusclee/ce-202:firstTry

#FULL IPC RUN DUDE
sudo perf stat -D 20 -I 100 -e cpu-cycles,instructions -x, -o output.csv sudo docker run -e threadCount=4 -e SIZE=64 jusclee/ce-202:firstTry
python ce202-jusclee/CE202-face-recognition/newrepo/interval-normalize.py output.csv --output newnew.csv
python ce202-jusclee/CE202-face-recognition/newrepo/plot-normalized-ipc.py newnew.csv --title "Thread 2 IPC size x/64" -y "Instructions per cycle"

#FULL L1 MPKI RUN DUDE
sudo perf stat -D 20 -I 10 -e L1-dcache-load-misses,instructions -x, -o output.csv sudo docker run -e threadCount=4 -e SIZE=64 jusclee/ce-202:firstTry
python ce202-jusclee/CE202-face-recognition/newrepo/interval-normalize.py output.csv --output norm.csv
python ce202-jusclee/CE202-face-recognition/newrepo/plot-normalized-l1.py norm.csv --title "Thread 4 L1 MPKI" -y "L1 Misses per 1000 Instructions" -o T_4_size_64_L1.png

#L2 plot mannn
sudo perf stat -D 20 -I 10 -e l2_rqsts.miss,instructions -x, -o output.csv sudo docker run -e threadCount=4 -e SIZE=64 jusclee/ce-202:firstTry
python ce202-jusclee/CE202-face-recognition/newrepo/interval-normalize.py output.csv --output norm.csv
python ce202-jusclee/CE202-face-recognition/newrepo/plot-normalized-l2.py norm.csv --title "Thread 4 L2 MPKI" -y "L2 Misses per 1000 Instructions" -o T_4_size_64_L2.png

#L3 plot mannn
sudo perf stat -D 20 -I 10 -e mem_load_uops_retired.l3_miss,instructions -x, -o output.csv sudo docker run -e threadCount=4 -e SIZE=64 jusclee/ce-202:firstTry
python ce202-jusclee/CE202-face-recognition/newrepo/interval-normalize.py output.csv --output norm.csv
python ce202-jusclee/CE202-face-recognition/newrepo/plot-normalized-l3.py norm.csv --title "Thread 4 L3 MPKI" -y "L3 Misses per 1000 Instructions" -o T_4_size_64_L3.png

#Branch MPKI
sudo perf stat -D 20 -I 100 -e branch-misses,branch-instructions -x, -o output.csv sudo docker run -e threadCount=2 -e SIZE=1 jusclee/ce-202:firstTry
python ce202-jusclee/CE202-face-recognition/newrepo/interval-normalize.py output.csv --output norm.csv
python ce202-jusclee/CE202-face-recognition/newrepo/plot-normalized-branch-miss.py norm.csv --title "Thread 2 Size 1 Branch MPKI" -y "Branch Misses per 1000 Branch Instructions" -o T_2_size_1_branch.png



