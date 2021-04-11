import requests
from multiprocessing import Pool
base = 'https://erowall.com/tf558550ef6e/'

def dl(n):
	for ch in [chr(c) for c in range(ord('a'), ord('f')+1)]:
		for i in range(0, 10000):
			url = '{:s}{:04d}_{:1d}.mp4'.format(ch, i, n)
			resp = requests.get(base + url)
			if resp.status_code == 200:
				print(base + url)
				with open('videos/' + url, 'wb') as f:
					f.write(resp.content)

if __name__ == '__main__':
	with Pool(10) as p:
		p.map(dl, range(10))
