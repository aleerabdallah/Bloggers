from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import PostSerializer, CreatePostSerializer
from ..models import Post, Category, Tag
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.renderers import MultiPartRenderer, JSONRenderer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status





class PostsAPIView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
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
            # posts = Post.objects.all()
            posts = Post.objects.select_related("category").prefetch_related("tags").filter(status=Post.PUBLISHED)
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
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    @extend_schema(
        methods=("GET",),
        parameters=[OpenApiParameter("slug", type=str, exclude=True), ],
        summary="Retrieve a single Post",
        description=(
            "An EndPoint for deleting a Newsletter"
            "Only allows a Newsletter to be deleted if the user is authenticated and at the same time the owner"
        ),
        responses=PostSerializer(),
    )
    def get(self, request: Request, slug: str = None) -> Response:
        if request.version == "v1.0":
            if slug:
                try:
                    post = Post.objects.get(slug=slug)
                    print(post.tags)
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




class CategoryAPIView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    
    @extend_schema(
        methods=("GET",),
        parameters=[OpenApiParameter("name", type=str, exclude=True), ],
        summary="Get all posts related to a category",
        description=(
            "An EndPoint for deleting a Newsletter"
            "Only allows a Newsletter to be deleted if the user is authenticated and at the same time the owner"
        ),
        # responses=CreatePostSerializer(),
    )
    def get(self, request: Request, name: str = None) -> Response:
        if request.version == "v1.0":
            if name:
                name = name.capitalize()
                try:
                    category = Category.objects.get(name=name)
                    # posts = Post.objects.select_related().filter(category=category)
                    # The following serializer should just return a post image, title, description, author
                    posts = category.posts.all()
                    serializer = PostSerializer(posts, many=True)
                    return Response(serializer.data)
                
                except Category.DoesNotExist:
                    pass




class TagAPIView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    @extend_schema(
        methods=("GET",),
        parameters=[OpenApiParameter("name", type=str, exclude=True), ],
        summary="Get all posts related to a Tag",
        description=(
            "An EndPoint for deleting a Newsletter"
            "Only allows a Newsletter to be deleted if the user is authenticated and at the same time the owner"
        ),
        # responses=CreatePostSerializer(),
    )
    def get(self, request: Request, name: str = None) -> Response:
        if request.version == "v1.0":
            if name:
                try:
                    # tag = Tag.objects.get(name=name)
                    # The following serializer should just return a post image, title, description, author
                    # related_posts = tag.posts.all()

                    tag = Tag.objects.prefetch_related("posts").get(name=name)
                    related_posts = tag.posts.all()
                    serializer = PostSerializer(related_posts, many=True)
                    return Response(serializer.data)
                
                except Category.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)


