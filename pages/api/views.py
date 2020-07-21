from rest_framework.generics import ListAPIView

from ..models import Slide
from .serializers import SlideSerializer

class SlideListAPIView(ListAPIView):
    queryset = Slide.objects.all()
    serializer_class = SlideSerializer
