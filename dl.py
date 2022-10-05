import os
import requests
from multiprocessing import Pool
from itertools import product

baseurl = 'https://affiliates.istripper.com/tools/poppings/'

with open('iStripper-shows.csv') as f:
	l = [x.split(';') for x in f.read().split('\n')]

go = True
if __name__ == '__main__':
	for s in l:
		id = s[0]
		name = s[3].replace(' ', '').replace('"', '')
		
		if id == 'c0521':
			go = True
		if go == False:
			continue
		
		for i in range(1, 100):
		
			fname = id + '_{:1d}.mp4'.format(i)
			#fname = id + '_{:02d}.mp4'.format(i)
			#fname = id + '_' + name + '_{:1d}.mp4'.format(i)
			#fname = id + '_' + name + '_{:02d}.mp4'.format(i)
			
			print(fname, end=' ')
			if not os.path.exists('videos/' + fname):
				resp = requests.get(baseurl + fname)
				if resp.status_code == 200:
					print('DL', end='')
					with open('videos/' + fname, 'wb') as f:
						f.write(resp.content)
				elif resp.status_code == 404:
					print()
					break
			print()
