import pyx12.x12n_document
fd_source = "/home/az2/Download/x12input_1.txt"
output_file = "result.xml"
with open(output_file, 'w') as fd_xml:
    result = pyx12.x12n_document.x12n_document(param=param, src_file=fd_source,fd_997=None, fd_html=None, fd_xmldoc=fd_xml, xslt_files=None)

##    testfile = '/home/az2/Download/5014.131020.2350.28i04i5m'
