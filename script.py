import os

if __name__ == '__main__':
    port=12345
    for threads in range(1, 6, 4):
        os.system("mkdir log")
        logdir = "log/thread" + str(threads)
        os.system("mkdir " + logdir)
        for batch_size in range(10, 610, 20):
            print("ruuning on batch_size"+str(batch_size))
            command ="./bench_tpcc --log_dir="+logdir+" --id=0 --servers='172.22.32.18:"+str(port)+";172.22.32.19:"+str(port)+";172.22.32.20:"+str(port)+"' --protocol=Aria  --threads="+str(threads)+"  --query=neworder --partition_num=108 --batch_size="+str(batch_size)
            os.system(command)
            print(command)
            port += 1
