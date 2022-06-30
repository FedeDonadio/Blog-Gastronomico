from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from AppBlog.models import Vino, Quesos, Platos, Postres, Cafe
from AppBlog.forms import VinoFormulario, QuesosFormulario, PlatosFormulario, PostresFormulario, CafeFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.


###############################            PAGINAS PRINCIPALES           #####################################################
##############################################################################################################################

def inicio(request):
    return render(request, 'AppBlog/inicio.html',{'fondo':'inicio-blog.jpg'})

def cafe(request):
    return render(request, 'AppBlog/cafe.html',{'fondo':'15480.jpg'})

def platos(request):
    return render(request, 'AppBlog/platos.html',{'fondo':'hamburguesa.jpg'})

def postres(request):
    return render(request, 'AppBlog/postres.html',{'fondo':'cupcakes.jpg'})

def quesos(request):
    return render(request, 'AppBlog/quesos.html',{'fondo':'cheese.jpg'})

def vinos(request):
    return render(request, 'AppBlog/vinos.html',{'fondo':'alimentos-vino.jpg'})

###############################################################################################################################
###############################################################################################################################
###############################################################################################################################
###############################################################################################################################




###########################             FORMULARIOS                                ############################################
###############################################################################################################################         

def vinosFormulario(request):
    
    if request.method == 'POST':
        formulario = VinoFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
        varietal = informacion['varietal']
        origen = informacion['origen']
        fecha = informacion['fecha']
        temperatura = informacion['temperatura']
        vino = Vino(varietal=varietal , origen=origen, fecha=fecha, temperatura=temperatura )
        vino.save()
        return render(request, 'AppBlog/inicio.html',{'fondo':'inicio-blog.jpg'})
    else:
        formulario = VinoFormulario()
        
    return render(request, "AppBlog/vinoFormulario.html", {"formulario":formulario,'fondo':'alimentos-vino.jpg'})

def quesosFormulario(request):
    
    if request.method == 'POST':
        formulario = QuesosFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
        nombre = informacion['nombre']
        tipo = informacion['tipo']
        origen = informacion['origen']
        pasteurizado = informacion['pasteurizado']
        queso = Quesos(nombre=nombre , tipo=tipo , origen=origen , pasteurizado=pasteurizado)
        queso.save()
        
        return render(request, 'AppBlog/inicio.html',{'fondo':'inicio-blog.jpg'})
    else:
        formulario = QuesosFormulario()
        
    return render(request, "AppBlog/quesosFormulario.html", {"formulario":formulario, 'fondo':'cheese.jpg'})


def platosFormulario(request):
    if request.method == 'POST':
        formulario = PlatosFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
        nombre = informacion['nombre']
        fecha = informacion['fecha']
        cocinero = informacion['cocinero']
        receta = informacion['receta']
        platos = Platos(nombre=nombre, fecha=fecha, cocinero=cocinero, receta=receta)
        platos.save()
        
        return render(request, 'AppBlog/inicio.html',{'fondo':'inicio-blog.jpg'})
    else:
        formulario = PlatosFormulario()
        
    return render(request, "AppBlog/platosFormulario.html", {"formulario":formulario, 'fondo':'especias.jpg'})


def postresFormulario(request):
    
    if request.method == 'POST':
        formulario = PostresFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
        nombre = informacion['nombre']
        pais = informacion['pais']
        fecha = informacion['fecha']
        pastelero = informacion['pastelero']
        postres = Postres(nombre=nombre , pais=pais , fecha=fecha , pastelero=pastelero)
        postres.save()

        return render(request, 'AppBlog/inicio.html',{'fondo':'inicio-blog.jpg'})
    else:
        formulario = PostresFormulario()
        
    return render(request, "AppBlog/postresFormulario.html", {"formulario":formulario, 'fondo':'cupcakes.jpg'})


def cafeFormulario(request):
    
    if request.method == 'POST':
        formulario = CafeFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
        variedad = informacion['variedad']
        filtrado = informacion['filtrado']
        barista = informacion['barista']
        origen = informacion['origen']
        cafe = Cafe(variedad=variedad , filtrado=filtrado , barista=barista , origen=origen)
        cafe.save()

        return render(request, 'AppBlog/inicio.html',{'fondo':'inicio-blog.jpg'})
    else:
        formulario = CafeFormulario()
        
    return render(request, "AppBlog/cafeFormulario.html", {"formulario":formulario, 'fondo':'15480.jpg'})

###############################################################################################################################
###############################################################################################################################   
###############################################################################################################################
###############################################################################################################################   


###########################                  BUSQUEDA                                    ######################################
###############################################################################################################################   

def buscarVinos(request):
    if request.GET['varietal']:
        varietal = request.GET['varietal']
        info = Vino.objects.filter(varietal__icontains=varietal)
        return render(request, "AppBlog/resultadoVinos.html", {'varietal':varietal, 'info':info, 'fondo':'alimentos-vino.jpg'})
    else:
        respuesta = "No hay datos"

    return HttpResponse(respuesta)


def buscarPlatos(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        info = Platos.objects.filter(nombre__icontains=nombre)
        return render(request, "AppBlog/resultadoPlatos.html", {'nombre':nombre, 'info':info, 'fondo':'especias.jpg'})
    else:
        respuesta = "No hay datos"

    return HttpResponse(respuesta)


def buscarPostres(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        info = Postres.objects.filter(nombre__icontains=nombre)
        return render(request, "AppBlog/resultadoPostres.html", {'nombre':nombre, 'info':info, 'fondo':'cupcakes.jpg'})
    else:
        respuesta = "No hay datos"

    return HttpResponse(respuesta)

def buscarCafe(request):
    if request.GET['variedad']:
        variedad = request.GET['variedad']
        info = Cafe.objects.filter(variedad__icontains=variedad)
        return render(request, "AppBlog/resultadoCafe.html", {'variedad':variedad, 'info':info, 'fondo':'15480.jpg'})
    else:
        info = Cafe.objects.all()
    return render(request, "AppBlog/resultadoCafe.html", {'info':info, 'fondo':'15480.jpg'})

def buscarQuesos(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        info = Quesos.objects.filter(nombre__icontains=nombre)
        return render(request, "AppBlog/resultadoQuesos.html", {'nombre':nombre, 'info':info, 'fondo':'cheese.jpg'})
    else:
        respuesta = "No hay datos"

    return HttpResponse(respuesta)


###############################################################################################################################
###############################################################################################################################
###############################################################################################################################
###############################################################################################################################


############################                   CRUD CON VIEWLIST              #################################################
###############################################################################################################################   

class PlatosList(ListView):
    model = Platos
    template_name = "AppBlog/platosLista.html"

class PlatosDetalle(DetailView):
    model = Platos
    template_name = "AppBlog/platosDetalle.html"

class PlatosCreacion(CreateView):
    model = Platos
    success_url = reverse_lazy("platosLista")
    fields = ['nombre','fecha','cocinero','receta']

class PlatosUpdate(UpdateView):
    model = Platos
    success_url = reverse_lazy("platosLista")
    fields = ['nombre','fecha','cocinero','receta']

class PlatosDelete(DeleteView):
    model = Platos
    success_url = reverse_lazy("platosLista")