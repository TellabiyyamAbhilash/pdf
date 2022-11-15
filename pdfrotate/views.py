from django.shortcuts import render
from .models import PDF
from rest_framework.views import APIView
from rest_framework.response import Response
from PyPDF2 import PdfFileReader,PdfFileWriter
from django.core.files import File
from django.conf import settings
# Create your views here.


class PDF_Page_Rotate(APIView):
    def post(self,request):
        print(request.FILES['file'])
        data=request.FILES
        page_num=request.data['page_num']
        an_of_rot=request.data['an_of_rot']
        print("base_directory",settings.BASE_DIR)
        try:
            object=PDF.objects.create(file=data['file'],page_num=page_num,an_of_rot=an_of_rot)
            pdf_in = data.get('file')
            pdfFileObj =pdf_in.open()
            pdf_reader = PdfFileReader(pdfFileObj) 
            pdf_writer = PdfFileWriter()
            path=str(data.get('file'))
            out_path=path[:-4]+"_rotated.pdf"
            print(out_path)
            pdf_out = open(out_path, 'wb')
            total_pages=pdf_reader.getNumPages()
            print("number of pages",total_pages)
            for i in range(total_pages):
                if (int(page_num)-1)==i:
                    page = pdf_reader.getPage(i)
                    page.rotateClockwise(int(an_of_rot))
                    pdf_writer.addPage(page)
                else:
                    page=pdf_reader.getPage(i)
                    pdf_writer.addPage(page)
            pdf_writer.write(pdf_out)
            pdf_out.close()
            upload_pdf=open(out_path,'rb')
            object.edited_file.save(out_path,File(upload_pdf))
            Api_out_pdf_path=str(settings.BASE_DIR)+"/"+out_path
        except Exception as e:
            return Response({
                "status":400,
                "message":f"{e}"
            })    
        return Response({
            "status":200,
            "rotated_pdf_path":Api_out_pdf_path,
        })
