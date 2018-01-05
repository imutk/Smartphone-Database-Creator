import xlrd
import csv
from fonAPI import FonApi
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')
fon = FonApi('b0021284efcdf57c5e88870120a3c43f498977c5b59f0854')
devices = ['apple','samsung','Huawei','Google', 'LG', 'Motorola', 'HTC', 'xiaomi', 'motorola', 'oneplus', 'Honor']
#device = 'apple'
fd = open('phone.csv','a')
#phones = fon.getdevice(device)
s = ""
contents = ""
with open('phone.csv') as f:
    s = f.read() + '\n' # add trailing new line character
def addPhone(fields):
	with open(r'phone.csv', 'a') as f:
		writer = csv.writer(f)
		writer.writerow(fields)
def findPhone(device):
	if device in s: # if the username shall be on column 3 (-> index 2)
		return True
with open('phone.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Name", "OS", "Price", "Resolution", "Screen", "Size", "Primary", "Secondary", "Weight", "Sensors", "Announced"])
    for device in devices:
		#b = findPhone(device)
		#if b:
		#	continue
		phones = fon.getdevice(device)
		for phone in phones:
			if "atch" in phone['DeviceName']:
				continue
			if str(phone['DeviceName']) in contents:
				continue
			s = []
			try:
				name = phone['DeviceName']
				s.append(name)
			except:
				s.append("")
			try:
				os = phone['os']
				s.append(os)
			except:
				s.append("")
			try:
				price = str(float((float(phone['price'][6:][:-4]))*1.21))
				s.append(price)
			except:
				s.append("")
			try:
				resolution = (phone['resolution'])
				s.append(resolution)
			except:
				s.append("")
			try:
				screenType = (phone['type'])
				s.append(screenType)
			except:
				s.append("")
			try:
				size = (phone['size'])
				s.append(size)
			except:
				s.append("")
			try:
				primary = (phone['primary_'])
				s.append(primary)
			except:
				s.append("")
			try:
				secondary = (phone['secondary'])
				s.append(secondary)
			except:
				s.append("")
			try:
				weight = (phone['weight'][:3])
				s.append(weight)
			except:
				s.append("")
			try:
				sensors = phone['sensors']
				s.append(sensors)
			except:
				s.append("")
			try:
				sensors = phone['announced']
				s.append(sensors)
			except:
				s.append("")
			contents += (''.join(s))		
			writer.writerow(s)
			#except:
				#writer.writerow([device])
			#	print phone['DeviceName'], phone['sensors'], phone['os'], phone['weight'], phone['announced'], phone['price']
