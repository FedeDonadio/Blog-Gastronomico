
from django.urls import path
from AppBlog.views import inicio, cafe, platos, postres, quesos, vinos, buscarVinos, vinosFormulario, platosFormulario, postresFormulario, quesosFormulario, cafeFormulario, buscarCafe, buscarPlatos, buscarPostres,buscarQuesos

urlpatterns = [
    path('', inicio, name='inicio'),
    path('cafe/', cafe, name='cafe'),
    path('platos/', platos, name='platos'),
    path('postres/', postres, name='postres'),
    path('quesos/', quesos, name='quesos'),
    path('vinos/', vinos, name='vinos'),
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
]