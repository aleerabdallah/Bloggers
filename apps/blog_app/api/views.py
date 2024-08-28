from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from .serializers import PostSerializer, CreatePostSerializer
from ..models import Post
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.renderers import MultiPartRenderer, JSONRenderer
from rest_framework.parsers import MultiPartParser, FormParser






class PostsAPIView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = PostSerializer

    @extend_schema(
        methods=("GET",),
        summary="Retrieve all Posts",
        description=(
            "An EndPoint for deleting a Newsletter"
            "Only allows a Newsletter to be deleted if the user is authenticated and at the same time the owner"
        ),
        responses={200: PostSerializer()},
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
        summary="Create a new Post",
        description=(
            "An EndPoint for deleting a Newsletter"
            "Only allows a Newsletter to be deleted if the user is authenticated and at the same time the owner"
        ),
        responses=CreatePostSerializer(),
    )
    def post(self, request: Request) -> Response:
        if request.version == "v1.0":
            data = request.data
            serializer = CreatePostSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
        
        return Response({'status': 'OK'})






class PostAPIView(APIView):
    serializer_class = PostSerializer
    @extend_schema(
        methods=("GET",),
        parameters=[OpenApiParameter("pk", type=int, exclude=True), ],
        summary="Retrieve a single Post",
        description=(
            "An EndPoint for deleting a Newsletter"
            "Only allows a Newsletter to be deleted if the user is authenticated and at the same time the owner"
        ),
        responses=PostSerializer(),
    )
    def get(self, request: Request, pk: int = None) -> Response:
        if request.version == "v1.0":
            if pk:
                try:
                    post = Post.objects.get(id=pk)
                    serializer = PostSerializer(post)
                    return Response(serializer.data)
    
                except Post.DoesNotExist:
                    return Response({'Error': "Object doesn't exist"})


    @extend_schema(
        methods=("PATCH",),
        parameters=[OpenApiParameter("pk", type=int, exclude=True), ],
        summary="Update a Post",
        description=(
            "An EndPoint for deleting a Newsletter"
            "Only allows a Newsletter to be deleted if the user is authenticated and at the same time the owner"
        ),
        request=CreatePostSerializer(),
        responses=CreatePostSerializer(),
    )
    def patch(self, request: Request, pk: int =None) -> Response:
        if request.version == "v1.0":
            data = request.data
            serializer = CreatePostSerializer(data=data)
            return Response({"status": "yes"})
        


    @extend_schema(
        methods=("DELETE",),
        parameters=[OpenApiParameter("pk", type=int, exclude=True), ],
        summary="Delete or Destroy a Post",
        description=(
            "An EndPoint for deleting a Newsletter"
            "Only allows a Newsletter to be deleted if the user is authenticated and at the same time the owner"
        ),
        # responses=CreatePostSerializer(),
    )
    def delete(self, request: Request, pk: int = None, formate=None) -> Response:
        if request.version == "v1.0":
            return Response({"status": "ok"})

