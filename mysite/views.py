from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from pymongo import MongoClient
from django.conf import settings

from .models import get_db
from .serializers import BlogSerializer



@api_view(['GET'])
def get_blogs(request):
    client = MongoClient(settings.MONGO_URI)
    
    # Get the 'new_db' database from the client
    db = client['new_db']
    blogs = list(db.blog.find({}, {"_id":0}))
    return Response(blogs)


@api_view(["GET"])
def get_blog(request, id):
    db = get_db()
    blog = db.blog.find_one({'title':id})
    if blog:
        blog['_id'] = str(blog['_id'])
        return Response(blog, status= status.HTTP_200_OK)
    else:
        return Response({'error': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
def create_blog(request):
    db = get_db()
    new_blog = BlogSerializer(data = request.data)
    if new_blog.is_valid():
        new_blogPost = new_blog.validated_data
        result = db.blog.insert_one(new_blogPost)
        new_blogPost['_id'] = str(result.inserted_id)
        return Response(new_blogPost, status=status.HTTP_201_CREATED)
    return Response(new_blog.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(["PATCH"])
def update_title(request, id):
    db = get_db()
    updated_blog = BlogSerializer(data=request.data, partial=True)
    if updated_blog.is_valid():
        blog_post = updated_blog.validated_data
        result = db.blog.find_one_and_update({'title':id}, {"$set":blog_post}, return_document=True)
        result["_id"] = str(result["_id"])
        return Response(blog_post, status= status.HTTP_200_OK)
    return Response(updated_blog.errors, status= status.HTTP_400_BAD_REQUEST)



@api_view(["PUT"])
def update_blog(request, id):
    db = get_db()
    updated_blog = BlogSerializer(data = request.data)
    if updated_blog.is_valid():
        post = updated_blog.validated_data
        result = db.blog.find_one_and_update({"title":id}, {"$set": post}, return_document=True)
        result["_id"]= str(result["_id"])
        return Response(result, status=status.HTTP_200_OK)
    return Response(updated_blog.errors, status= status.HTTP_400_BAD_REQUEST)



@api_view(["DELETE"])
def delete_blog(request, id):
    db= get_db()
    result = db.blog.delete_one({"title":id})
    if result:
        result["_id"] = str(result["_id"])
        return Response(result, status=status.HTTP_200_OK)
    return Response({'error': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND)



@api_view(["DELETE"])
def delete_all(request):
    db= get_db()
    result = db.blog.delete_many({})
    return Response({'message': f'Deleted {result.deleted_count} users.'}, status=status.HTTP_200_OK)


