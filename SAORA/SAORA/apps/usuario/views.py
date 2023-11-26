from rest_framework import generics
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView
from .models import Usuario, Afiliado
from .serializers import UsuarioSerializer, AfiliadoSerializer

# Create your views here.

def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			# Lógica para iniciar sesión si el formulario es válido
			return HttpResponseRedirect('/')
		else:
			form = AuthenticationForm()

		return render(request,'login.html',{'form':form})

class UsuarioAPIView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class AfiliadoAPIView(generics.ListCreateAPIView):
    queryset = Afiliado.objects.all()
    serializer_class = AfiliadoSerializer