import urllib.request, json
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView
from reportes.models import Reportes

# URL_USERDATASESSION = 'http://cpv.inei.gob.pe/seguridad/getUserData/?key={}'
# URL_USERDATASESSION = 'http://localhost:81/seguridad/getUserData/?key={}'
URL_USERDATASESSION = 'http://192.168.200.123:8000/seguridad/getUserData/?key={}'


# URL_USERDATASESSION_PRUEBA = 'http://cpv.inei.gob.pe/seguridad/getUserData/?key=x7rsdzt0c4s9kkav6rsdzratqubgz3uv'


def setSession(request):
    key = request.GET['key']
    response = urllib.request.urlopen(URL_USERDATASESSION.format(key))
    data = json.loads(response.read().decode('utf-8'))
    request.session['user_session'] = data['data']

    return redirect('/modulos/registro-local/')


def setSessionPrueba(request):
    response = urllib.request.urlopen(URL_USERDATASESSION_PRUEBA)
    data = json.loads(response.read().decode('utf-8'))
    request.session['user_session'] = data['data']
    if not request.session.session_key:
        request.session.save()

    return redirect('/modulos/registro-local/')


class RenderTemplate(TemplateView):
    def get_template_names(self):
        try:
            modulos = self.request.session['user_session']['modulos']['CPV']['modulos_individuales']
            slug = 'modulos/{}'.format(self.kwargs.get('slug'))
            for modulo in modulos:
                if modulo['slug'] == slug:
                    self.request.session['modulo_id'] = modulo['id']
                    return modulo['template_html']
            return '404.html'
        except:
            return '404.html'

    def get_context_data(self, **kwargs):
        context = super(RenderTemplate, self).get_context_data(**kwargs)
        try:
            modulos = self.request.session['user_session']['modulos']['CPV']['modulos_individuales']
            slug = 'modulos/{}'.format(self.kwargs.get('slug'))
            for modulo in modulos:
                if modulo['slug'] == slug:
                    context['breadcumbs'] = modulo['descripcion']
                    context['session_key'] = self.request.session.session_key
            return context
        except:
            return redirect('http://cpv.inei.gob.pe')


class RenderReportes(TemplateView):
    def get_template_names(self):
        slug = self.kwargs.get('slug')
        self.request.session['modulo_id'] = 108
        try:
            if slug == 'main':
                template = 'main.html'
            else:
                template = Reportes.objects.get(slug=slug).template_html
            return 'reportes/{}'.format(template)
        except:
            return 'reportes/reporte.html'

    def get_context_data(self, **kwargs):
        context = super(RenderReportes, self).get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        try:
            if slug == 'main':
                context['breadcumbs'] = 'Reportes'
                context['session_key'] = self.request.session.session_key
            else:
                reporte = Reportes.objects.get(slug=slug)
                context['breadcumbs'] = reporte.nombre
                context['session_key'] = self.request.session.session_key
            return context
        except:
            return redirect('localhost:8001/reportes/main')
