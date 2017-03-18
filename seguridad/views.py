import urllib.request, json
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView

# URL_USERDATASESSION = 'http://cpv.inei.gob.pe:8080/seguridad/getUserData/?key={}'


URL_USERDATASESSION = 'http://cpv.inei.gob.pe/seguridad/getUserData/?key={}'


def setSession(request):
    key = request.GET['key']
    response = urllib.request.urlopen(URL_USERDATASESSION.format(key))
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
        modulos = self.request.session['user_session']['modulos']['CPV']['modulos_individuales']
        slug = 'modulos/{}'.format(self.kwargs.get('slug'))
        for modulo in modulos:
            if modulo['slug'] == slug:
                context['breadcumbs'] = modulo['descripcion']
        return context
