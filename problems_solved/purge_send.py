import xml.etree.ElementTree as ET
import paramiko,subprocess
tree = ET.parse("script.xml")
root = tree.getroot()

#seq_no = 1
for seq_no in xrange(641,681,1):
	request_no = "test_hds_" + str(seq_no)
	request_url = "http://hdpurgetest-vh.edgeflash.qa.akamai.com/z/prasanna/firefly/voduniversal_62107642_2000K_" + str(seq_no) + ".mp4/manifest.f4m"
	request_file = "/prasanna/firefly/voduniversal_62107642_2000K_" + str(seq_no) + ".mp4"
	print "Url is : ",request_url
	for node in root.findall('request-name'):
		node.text = request_no
	for node in root.iter('url'):
		node.text = request_url
	for node in root.iter('file'):
		node.text = request_file

	tree = ET.ElementTree(root)
	tree.write("script_modify.xml")

	cmd = "curl -u 'ffsqauser1':'abc123' -H \"Content-type: application/xml\" -H \"X-ECWS-ManagedCustomer: 1-7KLGH\" https://control.sqa-shared.qa.akamai.com/streaming/api/hdnetwork/api/vod/purge/hd_zeri_vod -d @script_modify.xml  -k"

	output = subprocess.check_output(cmd, shell=True)
	print "output is ",output

