import os

if __name__ == '__main__':
    dblist = ['Calvin']
    wkldlist = ['payment', 'mixed']
    cross_ratios = [0, 15, 20, 80, 100]
    mid = 0
    port = 12345
    ip0 = '172.22.32.34'
    ip1 = '172.22.32.35'
    ip2 = '172.22.32.36'
    os.system('mkdir log')
    os.system('mkdir log/Calvin')
    for db in dblist:
       for cr in cross_ratios:
            for batch_size in range(20, 520, 20):
                logdir = 'log/' + db + '/pay-' + str(cr)
                os.system('mkdir ' + logdir)
                ips = ip0 + ":" + str(port) + ";" + ip1 + ":" + str(port) + ";" + ip2 + ":" + str(port)
                command = "./bench_tpcc --log_dir=" + logdir + " --id=" + str(mid) + " --servers='" + ips + "' --protocol=Calvin --partition_num=324 --threads=5 --batch_size=" + str(batch_size) + " --query=payment --replica_group=3 --payment_dist=" + str(cr)
                print(command)
                os.system(command)
                port += 1
