import urllib
import threading
import time

def pinger_urllib(host):
  """
  helper function timing the retrival of index.html 
  TODO: should there be a 1MB bogus file?
  """
  t1 = time.time()
  urllib.urlopen(host + '/index.html').read()
  return (time.time() - t1) * 1000.0


def task(m):
  """
  the actual task
  """
  delay = float(pinger_urllib(m))
  print ('%-30s %5.0f [ms]' % (m, delay))

# parallelization
tasks = []
URLs = ['https://github.com/jvirico']
times = 100
for m in URLs:
    for n in range(times):
        t = threading.Thread(target=task, args=(m,))
        t.start()
        tasks.append(t)

# synchronization point
for t in tasks:
  t.join()