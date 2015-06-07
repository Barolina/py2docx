# coding: utf-8
from py2docx.structure_files import StructureFile


class FontTable(StructureFile):

    def __init__(self):
        self.dir_name = 'word'
        self.file_name = 'fontTable.xml'

    def draw(self):
        xml_string = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>' + \
                     '<w:fonts xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">' + \
                         '<w:font w:name="Cambria">' + \
                             '<w:panose1 w:val="02040503050406030204" />' + \
                             '<w:charset w:val="00" />' + \
                             '<w:family w:val="auto" />' + \
                             '<w:pitch w:val="variable" />' + \
                             '<w:sig w:usb0="00000003" w:usb1="00000000" w:usb2="00000000" w:usb3="00000000" w:csb0="00000001" w:csb1="00000000" />' + \
                         '</w:font>' + \
                         '<w:font w:name="Times New Roman">' + \
                             '<w:panose1 w:val="02020603050405020304" />' + \
                             '<w:charset w:val="00" />' + \
                             '<w:family w:val="auto" />' + \
                             '<w:pitch w:val="variable" />' + \
                             '<w:sig w:usb0="00000003" w:usb1="00000000" w:usb2="00000000" w:usb3="00000000" w:csb0="00000001" w:csb1="00000000" />' + \
                         '</w:font>' + \
                         '<w:font w:name="Arial">' + \
                             '<w:panose1 w:val="020B0604020202020204" />' + \
                             '<w:charset w:val="00" />' + \
                             '<w:family w:val="auto" />' + \
                             '<w:pitch w:val="variable" />' + \
                             '<w:sig w:usb0="00000003" w:usb1="00000000" w:usb2="00000000" w:usb3="00000000" w:csb0="00000001" w:csb1="00000000" />' + \
                         '</w:font>' + \
                         '<w:font w:name="Calibri">' + \
                             '<w:panose1 w:val="020F0502020204030204" />' + \
                             '<w:charset w:val="00" />' + \
                             '<w:family w:val="auto" />' + \
                             '<w:pitch w:val="variable" />' + \
                             '<w:sig w:usb0="00000003" w:usb1="00000000" w:usb2="00000000" w:usb3="00000000" w:csb0="00000001" w:csb1="00000000" />' + \
                         '</w:font>' + \
                     '</w:fonts>'
        return xml_string
