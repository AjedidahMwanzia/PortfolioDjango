from django.shortcuts import render,redirect

# Create your views here.
def home (request):
    return render(request, 'home.html',{})


class ProfileList(APIView):
    permission_classes =(IsAdminOrReadOnly)
    def get (self,request,format=None ):
        all_projects
