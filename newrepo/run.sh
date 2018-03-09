#running the docker image script

sudo apt-get install linux-tools-common linux-tools-generic linux-tools-`uname -r`
sudo apt-get install python-matplotlib

 #1095  sudo docker build -t ez1 .
 #1096  sudo docker run -e threadCount=1212 -e SIZE=-12  ez1


sudo docker run -e threadCount=1212 -e SIZE=-12  ez1



#python runThreads.py -t 1212 --program "python throughPutRun.py -t 1212 -s -12"


#run perf on my shit

#run perf on this image with this thread and size -> get a png chart? or just a csv

#then plot that bull shit


sudo docker run -e threadCount=4 -e SIZE=64 jusclee/ce-202:firstTry

#l1 plot baby
sudo perf stat -I 10 -e L1-dcache-load-misses,instructions -x, -o output.csv sudo docker run -e threadCount=4 -e SIZE=64 jusclee/ce-202:firstTry
python interval-normalize.py output.csv --output norm.csv
python plot-normalized.py norm.csv 



sudo pmu_tools/ocperf.py stat -I 1000 -d -e cpu-cycles,instructions,branch-misses,l2_rqsts.miss,mem_load_uops_retired.l3_miss -x, -o output.csv python face_classifier/src/throughput.py --divider 64; python pmu_tools/interval-normalize.py output.csv --output norm.csv
