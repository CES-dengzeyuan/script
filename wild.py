import os

if __name__ == '__main__':
    dblist = ['Aria', 'Calvin']
    wkldlist = ['neworder']
    mid = 0
    port = 12345
    ip0 = '172.22.32.25'
    ip1 = '172.22.32.26'
    ip2 = '172.22.32.27'
    os.system('mkdir log')
    os.system('mkdir log/Aria')
    os.system('mkdir log/Calvin')
    for db in dblist:
        # impact of workload
        for wkld in wkldlist:
            for batch_size in range(20, 520, 20):
                logdir = 'log/' + db + '/' + wkld
                os.system('mkdir ' + logdir)
                ips = ip0 + ":" + str(port) + ";" + ip1 + ":" + str(port) + ";" + ip2 + ":" + str(port)
                if db == 'Aria':
                    command = "./bench_tpcc --log_dir=" + logdir + " --id=" + str(mid) + " --servers='" + ips + "' --protocol=Aria --partition_num=324 --threads=5 --batch_size=" + str(batch_size) + " --query=" + wkld
                else:
                    command = "./bench_tpcc --log_dir=" + logdir + " --id=" + str(mid) + " --servers='" + ips + "' --protocol=Calvin --partition_num=324 --threads=5 --batch_size=" + str(batch_size) + " --query=" + wkld + " --replica_group=3  --same_batch=True"
                print(command)
                os.system(command)
                port += 1
