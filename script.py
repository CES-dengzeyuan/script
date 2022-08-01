import os

if __name__ == '__main__':
    port=12345
    for threads in range(1, 6,2):
        os.system("mkdir log")
        logdir = "log/thread" + str(threads)
        os.system("mkdir " + logdir)
        for batch_size in range(10, 610, 20):
            print("ruuning on batch_size"+str(batch_size))
            command ="./bench_tpcc --log_dir="+logdir+" --id=2 --servers='172.17.0.2:"+str(port)+";172.17.0.3:"+str(port)+";172.17.0.4:"+str(port)+"' --protocol=Aria  --threads="+str(threads)+"  --query=neworder --partition_num=324 --batch_size="+str(batch_size)
            os.system(command)
            print(command)
            port += 1
