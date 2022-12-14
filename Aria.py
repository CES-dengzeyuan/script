import os

if __name__ == '__main__':
    dblist = ['Aria', 'Calvin']
    wkldlist = ['neworder', 'payment', 'mixed']
    cross_ratios = [0, 20, 80, 100]
    mid = 0
    port = 12345
    ip0 = '172.22.32.37'
    ip1 = '172.22.32.38'
    ip2 = '172.22.32.39'
    os.system('mkdir log')
    os.system('mkdir log/Aria')
    for db in dblist:
        # impact of payment distribution
        for cr in cross_ratios:
            for batch_size in range(20, 520, 20):
                logdir = 'log/' + db + '/pay-' + str(cr)
                os.system('mkdir ' + logdir)
                ips = ip0 + ":" + str(port) + ";" + ip1 + ":" + str(port) + ";" + ip2 + ":" + str(port)
                command = "./bench_tpcc --log_dir=" + logdir + " --id=" + str(mid) + " --servers='" + ips + "' --protocol=Aria --partition_num=324 --threads=5 --batch_size=" + str(batch_size) + " --query=payment --payment_dist=" + str(cr)
                print(command)
                os.system(command)
                port += 1
