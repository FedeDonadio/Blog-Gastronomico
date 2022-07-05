from atexit import register
from django.urls import path
#from AppBlog.views import inicio, cafe, platos, postres, quesos, vinos, buscarVinos, vinosFormulario, platosFormulario, postresFormulario, quesosFormulario, cafeFormulario, buscarCafe, buscarPlatos, buscarPostres,buscarQuesos
from AppBlog.views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('cafe/', cafe, name='cafe'),
    path('platos/', platos, name='platos'),
    path('postres/', postres, name='postres'),
    path('quesos/', quesos, name='quesos'),
    path('vinos/', vinos, name='vinos'),
    path('acercaDeMi/', acercaDeMi, name='acercaDeMi'),
    path('vinosFormulario/', vinosFormulario, name='vinosFormulario'),
    path('platosFormulario/', platosFormulario, name='platosFormulario'),
    path('postresFormulario/', postresFormulario, name='postresFormulario'),
    path('cafeFormulario/', cafeFormulario, name='cafeFormulario'),
    path('quesosFormulario/', quesosFormulario, name='quesosFormulario'),
    path('buscarVinos/', buscarVinos, name='buscarVinos'),
    path('buscarPlatos/', buscarPlatos, name='buscarPlatos'),
    path('buscarPostres/', buscarPostres, name='buscarPostres'),
    path('buscarCafe/', buscarCafe, name='buscarCafe'),
    path('buscarQuesos/', buscarQuesos, name='buscarQuesos'),
    path('platos/lista/', PlatosList.as_view(), name='platosLista'),
    path('platos/<pk>', PlatosDetalle.as_view(), name='platosDetalle'),
    path('platos/nuevo/', PlatosCreacion.as_view(), name='platosNuevo'),
    path('platos/editar/<pk>', PlatosUpdate.as_view(), name='platosEditar'),
    path('platos/borrar/<pk>', PlatosDelete.as_view(), name='platosBorrar'),
    path('login',login_request, name='Login'),
    path('register', register_request, name='Register'),
    path('logout',logout_request, name='Logout'),
<<<<<<< HEAD
    path('postres/lista/', PostresList.as_view(), name = 'postresLista'),
    path('postres/<int:pk>',PostresDetalle.as_view(), name = 'postresDetalle'),
    path('postres/nuevo/', PostresCreacion.as_view(), name='postresNuevo'),
    path('postres/editar/<pk>', PostresUpdate.as_view(), name='postresEditar'),
    path('postres/borrar/<pk>', PostresDelete.as_view(), name='postresBorrar'),
    path('vinos/lista/', VinosList.as_view(), name = 'vinosLista'),
    path('vinos/<int:pk>',VinosDetalle.as_view(), name = 'vinosDetalle'),
    path('vinos/nuevo/', VinosCreacion.as_view(), name='vinosNuevo'),
    path('vinos/editar/<pk>', VinosUpdate.as_view(), name='vinosEditar'),
    path('vinos/borrar/<pk>', VinosDelete.as_view(), name='vinosBorrar'), 
    path('quesos/lista/', QuesosList.as_view(), name = 'quesosLista'),
    path('quesos/<int:pk>',QuesosDetalle.as_view(), name = 'quesosDetalle'),
    path('quesos/nuevo/', QuesosCreacion.as_view(), name='quesosNuevo'),
    path('quesos/editar/<pk>', QuesosUpdate.as_view(), name='quesosEditar'),
    path('quesos/borrar/<pk>', QuesosDelete.as_view(), name='quesosBorrar'), 
    path('cafe/lista/', CafeList.as_view(), name = 'cafeLista'),
    path('cafe/<int:pk>',CafeDetalle.as_view(), name = 'cafeDetalle'),
    path('cafe/nuevo/', CafeCreacion.as_view(), name='cafeNuevo'),
    path('cafe/editar/<pk>', CafeUpdate.as_view(), name='cafeEditar'),
    path('cafe/borrar/<pk>', CafeDelete.as_view(), name='cafeBorrar'),
]
=======
    
]

>>>>>>> 3ba5825c822415047ffaf83b6d2b423489240317
