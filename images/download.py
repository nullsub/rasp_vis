# Python 3 code
import urllib.request, urllib.parse, urllib.error
 
url = 'http://rasp.linta.de/GERMANY/'
suffix = '00lst.d2.png'

prefixes = ["wstar_bsratio", "wstar", "sfctemp", "sfcsun", "sfcsunpct", "sfcshf", "dbl", "hbl", "hwcrit", "dwcrit", "bltopvariab", "bsratio",
		"zsfclcldif", "zsfclcl", "zsfclclmask", "zblcldif", "zblcl", "zblclmask", "blcloudpct", "sfcdewpt", "cape", "rain1", "rain3",
		"sounding1", "sounding2", "sounding3", "sounding4", "sounding5", "sounding6", "sounding7", "sounding8", "sounding9"]

def download(prefix):
	for x in range(7,20):
		filename = prefix + '%0*d' % (2, x) + suffix
		print("downloading: " + filename)
		urllib.request.urlretrieve(url + filename, filename)
 
if __name__ == '__main__':
	#download today		
	for prefix in prefixes:
		download(prefix +".curr.");
	#download tommorow		
	for prefix in prefixes:
		download(prefix +".curr+1.");
