import pypandoc

output = pypandoc.convert_file('Test_word_doc_to_convert_to_pdf.docx', 'pdf', outputfile="Test_word_doc_to_convert_to_pdf.pdf", 
extra_args=['-V', 'geometry:margin=1.5cm'])
assert output == ""



#output = pypandoc.convert_file('Test_word_doc_to_convert_to_pdf.docx', 'pdf', outputfile="Test_word_doc_to_convert_to_pdf.pdf")
#assert output == "Test_word_doc_to_convert_to_pdf.pdf"












#word2PDF = pandoc.Document()
#word2PDF.docx = 'Test_word_doc_to_convert_to_pdf.docx'

#pandoc -f word2PDF.docx -o word2PDF.pdf
#print word2PDF.pdfoutput = pypandoc.convert_file('somefile.txt', 'rst', format='md')

