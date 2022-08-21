

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
