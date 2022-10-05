import os
import requests
from multiprocessing import Pool
from itertools import product
import json

with open('anims.json') as f:
	anims = json.load(f)

def dl(host):
	for anim in host['anims']:
		fname = anim['id'] + '.mp4'
		if not os.path.exists('videos/' + fname):
			resp = requests.get(host['base'] + fname)
			print(fname)
			if resp.status_code == 200:
				with open('videos/' + fname, 'wb') as f:
					f.write(resp.content)

if __name__ == '__main__':
	for host in anims:
		dl(host)
