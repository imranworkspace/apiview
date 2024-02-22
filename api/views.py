from django.shortcuts import render
from .models import StudentModel
from .serializer import StudentSerializer
from rest_framework.response import Response
# Create your views here.
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
class ViewClass(APIView):
    print('calling from view class')
    def get(self,request,id):
        result = StudentModel.objects.get(id=id)
        if id:
            serializer = StudentSerializer(result)
            return Response({'status':'success','data':serializer.data},status=status.HTTP_200_OK)
        all = StudentModel.objects.all()
        serializer = StudentSerializer(all,many=True)
        return Response({'status':'success','data':serializer.data},status=status.HTTP_200_OK)
    
    def post(self,request):
        seri = StudentSerializer(data=request.data)
        if seri.is_valid():
            seri.save()
            return Response({'status':'added','data':seri.data},status=status.HTTP_201_CREATED)
        else:
            return Response({'status':'error','data':seri.errors},status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self,request,id):
        result = StudentModel.objects.get(id=id)
        serializer = StudentSerializer(result,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":'partially updated ','data':serializer.data},status=status.HTTP_202_ACCEPTED)
        
    def delete(self,request,id=None):
        result = get_object_or_404(StudentModel,id=id)
        result.delete()
        return Response({"status":'deleted','data':'record deleted'},status=status.HTTP_200_OK)
        