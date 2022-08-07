import os

if __name__ == '__main__':
    dblist = ['Calvin']
    wkldlist = ['neworder', 'payment', 'mixed']
    cross_ratios = [0, 20, 80, 100]
    mid = 0
    port = 12345
    ip0 = '172.17.0.2'
    os.system('mkdir log')
    os.system('mkdir log/Calvin')
    for db in dblist:
        # impact of workload
        for wkld in wkldlist:
            for batch_size in range(20, 520, 20):
                logdir = 'log/' + db + '/' + wkld
                os.system('mkdir ' + logdir)
                ips = ip0 + ":" + str(port)
                command = "./bench_tpcc --log_dir=" + logdir + " --id=" + str(mid) + " --servers='" + ips + "' --protocol=Calvin --partition_num=324 --threads=5 --batch_size=" + str(batch_size) + " --query=" + wkld + " --replica_group=1"
                print(command)
                os.system(command)
                port += 1
        # impact of neworder distribution
        for cr in cross_ratios:
            for batch_size in range(20, 520, 20):
                logdir = 'log/' + db + '/new-' + str(cr)
                os.system('mkdir ' + logdir)
                ips = ip0 + ":" + str(port) + ";" + ip1 + ":" + str(port) + ";" + ip2 + ":" + str(port)
                command = "./bench_tpcc --log_dir=" + logdir + " --id=" + str(mid) + " --servers='" + ips + "' --protocol=Calvin --partition_num=324 --threads=5 --batch_size=" + str(batch_size) + " --query=neworder --replica_group=1 --neworder_dist=" + str(cr)
                print(command)
                os.system(command)
                port += 1
        # impact of payment distribution
        for cr in cross_ratios:
            for batch_size in range(20, 520, 20):
                logdir = 'log/' + db + '/pay-' + str(cr)
                os.system('mkdir ' + logdir)
                ips = ip0 + ":" + str(port) + ";" + ip1 + ":" + str(port) + ";" + ip2 + ":" + str(port)
                command = "./bench_tpcc --log_dir=" + logdir + " --id=" + str(mid) + " --servers='" + ips + "' --protocol=Calvin --partition_num=324 --threads=5 --batch_size=" + str(batch_size) + " --query=neworder --replica_group=1 --payment_dist=" + str(cr)
                print(command)
                os.system(command)
                port += 1
        # impact of threads
        for thread in range(2, 5):
            for batch_size in range(20, 520, 20):
                logdir = 'log/' + db + '/threads-' + str(thread)
                os.system('mkdir ' + logdir)
                ips = ip0 + ":" + str(port) + ";" + ip1 + ":" + str(port) + ";" + ip2 + ":" + str(port)
                command = "./bench_tpcc --log_dir=" + logdir + " --id=" + str(mid) + " --servers='" + ips + "' --protocol=Calvin --partition_num=324 --threads=" + str(thread) + " --batch_size=" + str(batch_size) + " --query=neworder --replica_group=3"
                print(command)
                os.system(command)
                port += 1
