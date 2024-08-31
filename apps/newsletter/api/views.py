from . serializers import SubscriberSerializers, CreateNewsLetterSerializer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from rest_framework.parsers import JSONParser
from newsletter.utils import decode_id
from ..models import Subscriber, Newletter
# from knox.auth import TokenAuthentication
from .permissions import IsOwnerOrReadOnly
from drf_spectacular.utils import extend_schema, OpenApiTypes
from drf_spectacular.utils import OpenApiParameter
from rest_framework.authentication import SessionAuthentication
from drf_spectacular.utils import extend_schema_view
import _thread
from time import perf_counter







class NewsLatterSubscribtionAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [JSONParser]

    @extend_schema(
        methods=("POST",),
        summary="Subscribe to a newsletter",
        description="An Endpoint for subscribing to the Newsletter List",
        request=SubscriberSerializers(),
        responses=SubscriberSerializers(),
    )
    def post(self, request: Request) -> Response:
        if request.version == "v1.0":
            data = request.data
            print(data)
            serializer = SubscriberSerializers(data=data)
            if serializer.is_valid(raise_exception=True):
                return Response({"Message": "Subscribed successfully check your inbox to verify your email"})
        else:
            return Response({"version": "The version is under constructions"})
    




class ConfirmSubscribtionEmailAPIView(APIView):

    @extend_schema(
        methods=("GET",),
        parameters=[
            OpenApiParameter(name="id", description="A string id", required=True, type=OpenApiTypes.STR, location=OpenApiParameter.QUERY),
            OpenApiParameter(name="conf_num", description="An integer conf_num", required=True, type=OpenApiTypes.INT, location=OpenApiParameter.QUERY)
        ],
        summary="Confirm subscription email",
        description="An EndPoint for for Email Confirmation",
        responses={
            200: OpenApiTypes.OBJECT
        }
    )
    def get(self, request: Request, id: str, conf_num: int) -> Response:
        if request.version == "v1.0":
            userID = decode_id(id)
            try:
                subscriber = Subscriber.objects.get(id=userID[0])
                if subscriber is not None and conf_num == subscriber.conf_num:
                        subscriber.confirmed = True
                        subscriber.save()
                        return Response({"Message": "Email Confirmed Successfully!"})
                else:
                    return Response(status=status.HTTP_401_UNAUTHORIZED)
            except:
                return Response({"Message": "Invalid Link"})
        else:
            return Response({"version": "The version is under constructions"})




class CreateNewsLetterAPIView(APIView):
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    parser_classes = [JSONParser]
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_object(self):
        return Newletter.objects.get(pk=self.kwargs['pk'])

    @extend_schema(
        methods=("GET",),
        # parameters=[OpenApiParameter("pk", exclude=True)],
        summary="List all Newsletters",
        description="Returns a List of Newsletters or a particular Newsletter with an ID",
        responses=CreateNewsLetterSerializer(many=True),
    )
    def get(self, request: Request, pk: int =None, *args, **kwargs) -> Response:
        print(request.version)
        if request.version == "v1.0":
            print(request.version)
            newsletters = Newletter.objects.all()
            serializers = CreateNewsLetterSerializer(newsletters, many=True)
            return Response(serializers.data)
        else:
            return Response({"version": "The version is under construction"})
    



    @extend_schema(
        methods=("POST",),
        # parameters=[OpenApiParameter("pk", exclude=True)],
        summary="Create a Newsletter",
        description="An EndPoint for creating a Newsletter",
        request=CreateNewsLetterSerializer(),
        responses=CreateNewsLetterSerializer(),
    )
    def post(self, request: Request, *args, **kwargs) -> Response:
        if request.version == "v1.0":
            if request.user.is_staff:
                data = request.data
                serializer = CreateNewsLetterSerializer(data=data)
            
                if serializer.is_valid(raise_exception=True):
                    serializer.save(author=request.user)
                    return Response({"status": "Successful"})
            return Response({"Success": "Gotcha"})
        else:
            return Response({"version": "The version is under construction"})



    
    


    
        



class NewsletterAPIView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    @extend_schema(
        methods=("GET",),
        parameters=[OpenApiParameter("pk", type=int, exclude=True)],
        summary="Retrieve an individual Newsletter",
        description="An EndPoint for retrieving an individual Newsletter",
        # request=CreateNewsLetterSerializer(),
        responses=CreateNewsLetterSerializer(),
    )
    def get(self, request: Request, pk: int = None) -> Response:
        if request.version == "v1.0":
            if pk:
                newsletter = self.get_object()
                if newsletter is not None:
                    serializer = CreateNewsLetterSerializer(newsletter)
                    return Response(serializer.data)
                return Response({"Status": "object not found"})

    @extend_schema(
        methods=("PATCH",),
        parameters=[OpenApiParameter("pk", type=int, exclude=True)],
        summary="Update a Newsletter",
        description="An EndPoint for editing a Newsletter",
        request=CreateNewsLetterSerializer(),
        responses=CreateNewsLetterSerializer(),
    )
    def patch(self, request: Request, pk: int, *args, **kwargs) -> Response:
        if request.version == "v1.0":
            if pk:
                try:
                    newsletter = Newletter.objects.get(id=pk)
                    self.check_object_permissions(request, newsletter)
                    serializer = CreateNewsLetterSerializer(newsletter, data=request.data, partial=True)
                    if serializer.is_valid(raise_exception=True):
                        serializer.save()
                        return Response(status=status.HTTP_200_OK)
                    
                except Newletter.DoesNotExist:
                    pass
            else:
                return Response({"status": "Not Found"})
        else:
            return Response({"version": "The version is under construction"})
        


    @extend_schema(
        methods=("DELETE",),
        parameters=[OpenApiParameter("pk", type=int, exclude=True), ],
        summary="Delete a Newsletter",
        description=(
            "An EndPoint for deleting a Newsletter"
            "Only allows a Newsletter to be deleted if the user is authenticated and at the same time the owner"
        ),
        responses=CreateNewsLetterSerializer(),
    )
    def delete(self, request: Request, pk: int, *args, **kwargs) -> Response:
        print(request.user)
        print(pk)
        if request.version == "v1.0":
            if request.user.is_staff:
                if pk:
                    newsletter = Newletter.objects.get(id=pk)
                    print(newsletter)
                    self.check_object_permissions(request, newsletter)
                    newsletter.delete()
                    return Response(status=status.HTTP_204_NO_CONTENT)
                
                return Response(status=status.HTTP_404_NOT_FOUND)
            
            return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            return Response({"version": "The version is under construction"})







class SendNewsLetterAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    parser_classes = [JSONParser]
    serializer_class = CreateNewsLetterSerializer

    @extend_schema(
        methods=("PATCH",),
        parameters=[
            OpenApiParameter(name="pk", description="An integer pk", required=True, type=OpenApiTypes.INT, location=OpenApiParameter.QUERY)
        ],
        summary="Send a Newsletter",
        description=(
            "An EndPoint for deleting a Newsletter"
            "Only allows a Newsletter to be deleted if the user is authenticated and at the same time the owner"
        ),
        responses={
            200: OpenApiTypes.OBJECT
        },
    )   
    def patch(self, request: Request, pk: int = None, *args, **kargs) -> Response:
        # Check if the user is part of the stuff
        user = request.user
        # print(user)
        t = _thread
        if request.version == "v1.0":
            if user.is_staff:
                if pk:
                    newsletter = Newletter.objects.get(id=pk)
                    self.check_object_permissions(request, newsletter)
                    try:
                        before = perf_counter()
                        # t.start_new_thread(newsletter.send, (request,))
                        newsletter.send(request=request)
                        after = perf_counter()
                        execution_time = after - before
                        # print(f"Execution time: {execution_time:.2f} seconds")
                        newsletter.status=Newletter.SENT
                        newsletter.save()
                        return Response(status=status.HTTP_200_OK)
                    
                    except Exception as e:
                        return Response({"status": "Error sending email"})
        else:
            return Response({"version": "The version is under construction"})
        

