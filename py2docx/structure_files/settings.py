# coding: utf-8
from py2docx.structure_files import StructureFile


class Settings(StructureFile):

    def __init__(self):
        self.dir_name = 'word'
        self.file_name = 'settings.xml'

    def draw(self):
        xml_string = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>' + \
                      '<w:settings xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w10="urn:schemas-microsoft-com:office:word" xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:sl="http://schemas.openxmlformats.org/schemaLibrary/2006/main">' + \
                          '<w:zoom w:percent="90" />' + \
                          '<w:embedSystemFonts />' + \
                          '<w:proofState w:spelling="clean" w:grammar="clean" />' + \
                          '<w:doNotTrackMoves />' + \
                          '<w:defaultTabStop w:val="720" />' + \
                          '<w:drawingGridHorizontalSpacing w:val="360" />' + \
                          '<w:drawingGridVerticalSpacing w:val="360" />' + \
                          '<w:displayHorizontalDrawingGridEvery w:val="0" />' + \
                          '<w:displayVerticalDrawingGridEvery w:val="0" />' + \
                          '<w:characterSpacingControl w:val="doNotCompress" />' + \
                          '<w:savePreviewPicture />' + \
                          '<w:compat>' + \
                              '<w:doNotAutofitConstrainedTables />' + \
                              '<w:doNotVertAlignCellWithSp />' + \
                              '<w:doNotBreakConstrainedForcedTable />' + \
                              '<w:useAnsiKerningPairs />' + \
                              '<w:cachedColBalance />' + \
                              '<w:splitPgBreakAndParaMark />' + \
                          '</w:compat>' + \
                          '<w:rsids>' + \
                              '<w:rsidRoot w:val="00854B22" />' + \
                              '<w:rsid w:val="00854B22" />' + \
                          '</w:rsids>' + \
                          '<m:mathPr>' + \
                              '<m:mathFont m:val="Arial Black" />' + \
                              '<m:brkBin m:val="before" />' + \
                              '<m:brkBinSub m:val="--" />' + \
                              '<m:smallFrac m:val="off" />' + \
                              '<m:dispDef m:val="off" />' + \
                              '<m:lMargin m:val="0" />' + \
                              '<m:rMargin m:val="0" />' + \
                              '<m:wrapRight />' + \
                              '<m:intLim m:val="subSup" />' + \
                              '<m:naryLim m:val="subSup" />' + \
                          '</m:mathPr>' + \
                          '<w:themeFontLang w:val="en-US" />' + \
                          '<w:clrSchemeMapping w:bg1="light1" w:t1="dark1" w:bg2="light2" w:t2="dark2" w:accent1="accent1" w:accent2="accent2" w:accent3="accent3" w:accent4="accent4" w:accent5="accent5" w:accent6="accent6" w:hyperlink="hyperlink" w:followedHyperlink="followedHyperlink" />' + \
                          '<w:decimalSymbol w:val="." />' + \
                          '<w:listSeparator w:val="," />' + \
                      '</w:settings>'
        return xml_string
