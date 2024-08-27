from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from .serializers import PostSerializer, CreatePostSerializer
from ..models import Post
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.renderers import MultiPartRenderer, JSONRenderer
from rest_framework.parsers import MultiPartParser, FormParser




class PostAPIView(APIView):
    # renderer_classes = [MultiPartRenderer]
    parser_classes = [MultiPartParser, FormParser]
    @extend_schema(
        methods=("GET",),
        # parameters=[OpenApiParameter("pk", exclude=True)],
        description="An EndPoint for Listing all posts",
        # request=EventSerializer(),
        responses=PostSerializer(),
    )
    def get(self, request: Request) -> Response:
        if request.version == "v1.0":
            posts = Post.objects.all()
            print(request.version)
            serializer = PostSerializer(posts, many=True)
            return Response(serializer.data)
        else:
            return Response({"version": "under construction"})
    

    @extend_schema(
        methods=("POST",),
        # parameters=[OpenApiParameter("pk", exclude=True)],
        description="An EndPoint for creating a Post",
        request=CreatePostSerializer(),
        responses=PostSerializer(),
    )
    def post(self, request: Request) -> Response:
        if request.version == "v1.0":
            data = request.data
            serializer = CreatePostSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
        
        return Response({'status': 'OK'})
