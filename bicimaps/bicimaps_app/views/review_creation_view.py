from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models.review import Review
from ..models.user import User

class ReviewCreationView(APIView):
    def post(self, request):

        try:
            data = request.data
            user_email = request.user.email
            review_location = data["review_location"]
            review = data["review"]

            user_instance = User.objects.get(email=user_email)

            Review.objects.create(
                user_id = user_instance,
                review_location=review_location,
                review=review
            )

            return Response({"detail": "Review creada exitosamente."}, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response({"detail": "Error al crear review.", "error": e}, status=status.HTTP_400_BAD_REQUEST)
        
        

