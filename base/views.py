from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import AdvocateSerializer
from rest_framework.views import APIView
from django.db.models import Q


# Create your views here.
@api_view(['GET'])
def endpoints(request):
    data= ['/advocates', 'advocates/:username']
    return Response(data)

@api_view(['GET', 'POST'])
def advocates_list(request):
#handles GET requests
  if request.method == 'GET':  
    query = request.GET.get('query')

    if query == None:
        query = ''
    


    advocates = Advocate.objects.filter(Q(username__icontains=query) | Q(bio__icontains=query))
    serializer = AdvocateSerializer(advocates, many=True)
    return Response(serializer.data)
  

  if request.method == 'POST':
    
     advocate = Advocate.objects.create(
        username=request.data['username'],
        bio=request.data['bio']
     )

     serializer = AdvocateSerializer(advocate, many=False)

     return Response(serializer.data)    
  


class AdvocateDetail(APIView):

   def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404


   def get(self, request, username):
      advocate =self.get_object(username)
      serializer = AdvocateSerializer(advocate, many= False)
      return Response(serializer.data)



   def put(self, request, username):
      advocate = self.get_object(username)
      advocate.username = request.data['username']
      advocate.bio = request.data['bio']
      serializer = AdvocateSerializer(advocate, many= False)
      return Response(serializer.data)
   
   def delete(self, request, username):
      advocate = self.get_object(username)
      advocate.delete()
      return redirect('user was deleted')




# @api_view(['GET', 'PUT', 'DELETE'])
# def advocates_details(request, username): 
#     advocate = Advocate.objects.get(username=username)

#     if request.method == 'GET':              
#       serializer = AdvocateSerializer(advocate, many= False)
#       return Response(serializer.data)
    
#     if request.method == 'PUT':
#        advocate.username = request.data['username']
#        advocate.bio = request.data['bio']

#        advocate.save()

#        serializer = AdvocateSerializer(advocate, many= False)
#        return Response(serializer.data)

#     if request.method == 'DELETE':
#        advocate.delete()
#        return redirect('user was deleted')

          

       