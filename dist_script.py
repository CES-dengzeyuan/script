import os

if __name__ == '__main__':
    dblist = ['Aria', 'Calvin']
    wkldlist = ['neworder', 'payment', 'mixed']
    cross_ratios = [0, 20, 80, 100]
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
        # impact of neworder distribution
        for cr in cross_ratios:
            for batch_size in range(20, 520, 20):
                logdir = 'log/' + db + '/new-' + str(cr)
                os.system('mkdir ' + logdir)
                ips = ip0 + ":" + str(port) + ";" + ip1 + ":" + str(port) + ";" + ip2 + ":" + str(port)
                if db == 'Aria':
                    command = "./bench_tpcc --log_dir=" + logdir + " --id=" + str(mid) + " --servers='" + ips + "' --protocol=Aria --partition_num=324 --threads=5 --batch_size=" + str(batch_size) + " --query=neworder --neworder_dist=" + str(cr)
                else:
                    command = "./bench_tpcc --log_dir=" + logdir + " --id=" + str(mid) + " --servers='" + ips + "' --protocol=Calvin --partition_num=324 --threads=5 --batch_size=" + str(batch_size) + " --query=neworder --replica_group=3  --same_batch=True --neworder_dist=" + str(cr)
                print(command)
                os.system(command)
                port += 1
        # impact of payment distribution
        for cr in cross_ratios:
            for batch_size in range(20, 520, 20):
                logdir = 'log/' + db + '/pay-' + str(cr)
                os.system('mkdir ' + logdir)
                ips = ip0 + ":" + str(port) + ";" + ip1 + ":" + str(port) + ";" + ip2 + ":" + str(port)
                if db == 'Aria':
                    command = "./bench_tpcc --log_dir=" + logdir + " --id=" + str(mid) + " --servers='" + ips + "' --protocol=Aria --partition_num=324 --threads=5 --batch_size=" + str(batch_size) + " --query=payment --payment_dist=" + str(cr)
                else:
                    command = "./bench_tpcc --log_dir=" + logdir + " --id=" + str(mid) + " --servers='" + ips + "' --protocol=Calvin --partition_num=324 --threads=5 --batch_size=" + str(batch_size) + " --query=payment --replica_group=3  --same_batch=True --payment_dist=" + str(cr)
                print(command)
                os.system(command)
                port += 1
        # impact of threads
        for thread in range(2, 5):
            for batch_size in range(20, 520, 20):
                logdir = 'log/' + db + '/threads-' + str(thread)
                os.system('mkdir ' + logdir)
                ips = ip0 + ":" + str(port) + ";" + ip1 + ":" + str(port) + ";" + ip2 + ":" + str(port)
                if db == 'Aria':
                    command = "./bench_tpcc --log_dir=" + logdir + " --id=" + str(mid) + " --servers='" + ips + "' --protocol=Aria --partition_num=324 --threads=" + str(thread) + " --batch_size=" + str(batch_size) + " --query=neworder"
                else:
                    command = "./bench_tpcc --log_dir=" + logdir + " --id=" + str(mid) + " --servers='" + ips + "' --protocol=Calvin --partition_num=324 --threads=" + str(thread) + " --batch_size=" + str(batch_size) + " --query=neworder --replica_group=3  --same_batch=True"
                print(command)
                os.system(command)
                port += 1
