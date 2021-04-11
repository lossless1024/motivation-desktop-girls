import requests
from multiprocessing import Pool
from itertools import product


hosts = [
#	'https://erowall.com/tf558550ef6e/',
	'https://zoomgirls.net/t00a0b00821f/',
	'http://girlwallpaper.pro/t08ece370cf3/',
	'https://www.adultwalls.com/td480c6bc2c7/',
	'https://nakedgirlwallpaper.pro/totempoping/t354881a7582/',
]

def dl(*args):
	host, n = args
	for ch in [chr(c) for c in range(ord('a'), ord('f')+1)]:
		for i in range(0, 2000):
			url = '{:s}{:04d}_{:1d}.mp4'.format(ch, i, n)
			resp = requests.get(host + url)
			if resp.status_code == 200:
				print(host + url)
				with open('videos/' + url, 'wb') as f:
					f.write(resp.content)

if __name__ == '__main__':
	for host in hosts:
		with Pool(10) as p:
			p.starmap(dl, product([host], range(10)))

