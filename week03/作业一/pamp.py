import os
import argparse
import re
from multiprocessing.pool import Pool
from concurrent.futures import ThreadPoolExecutor,as_completed
from threading import Lock

def simple_ping(fmode,test_ip):
    d = os.popen(fmode + ' ' + test_ip)
    f = d.read()
    print(f)
    return f

def ping(fmode,test_ip,filepath):
    d = os.popen(fmode + ' ' + test_ip)
    f = d.read()
    print(f)
    return {filepath:f}

def mycallback(x):
    filepath = list(x.keys())[0]
    result = x[filepath]
    with open(filepath,'a+',encoding='utf-8') as f:
        f.write(result)
    f.close()

def pamp(fmode,ip,run_mode='',nodes=0,filepath=''):
    result = ''
    if fmode != 'ping' and fmode != 'telnet':
        print('-f参数未输入或输入除ping,telnet之外的参数')
        return None
    ips = ip.split('-')
    for i in ips:
        if not re.match(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", i):
            print('ip地址不合法')
            return None
    if run_mode != '' and run_mode != 'proc' and run_mode != 'thread':
        print('运行模式错误')
        return None
    if len(ips)==1:
        result = ping(fmode,ip,filepath)
        print(result)
    if len(ips)==2:
        start_index = int((ips[0]).split('.')[3])
        finish_index = int((ips[1]).split('.')[3])
        if run_mode == 'proc':
            p = Pool(nodes)
            for i in range(start_index,finish_index+1):
                test_ip = (ips[0])[0:-len((ips[0]).split('.')[3])]
                test_ip = test_ip + str(i)
                p.apply_async(ping,args=(fmode,test_ip,filepath,),callback=mycallback)
            p.close()
            p.join()
        if run_mode == 'thread':
            file = open(filepath,'a+',encoding='utf-8')
            lock = Lock()
            with ThreadPoolExecutor(max_workers=nodes) as executor:
                futures = {}
                for i in range(start_index,finish_index+1):
                    test_ip = (ips[0])[0:-len((ips[0]).split('.')[3])]
                    test_ip = test_ip + str(i)
                    job = executor.submit(simple_ping,fmode,test_ip)
                    futures[job]=test_ip
                for job in as_completed(futures):
                    try:
                        result = job.result()
                        test_ip = futures[job]
                        with lock:
                            file.write(result)
                    except Exception as e:
                        file.write(str(e))
            file.close()
    return result

parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument("-f",type=str,default='')
parser.add_argument("-ip",type=str,default='')
parser.add_argument("-w",type=str,default='')
parser.add_argument("-m",type=str,default='')
parser.add_argument("-n",type=int,default=1)
args = parser.parse_args()
fmode = args.f
ip = args.ip
run_mode = args.m
nodes = args.n
filepath = args.w
print(fmode)
print(ip)
print(filepath)
print(run_mode)
print(nodes)

try:
    pamp(fmode,ip,run_mode=run_mode,nodes=nodes,filepath=filepath)
except Exception as e:
    print(e)