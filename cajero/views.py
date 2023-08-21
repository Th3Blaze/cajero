from django.shortcuts import render, HttpResponseRedirect
from . import forms
from . import models
from decimal import Decimal

# Create your views here.

def index_view(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            id_usuario = form.cleaned_data['usuario']
            contrasena = form.cleaned_data['contrasena']
            try:
                cuenta = models.UsuarioBanco.objects.get(id_usuario=id_usuario, contrasenha=contrasena)
                cuenta_bancaria = cuenta.cuentabancaria_set.first()
                if cuenta_bancaria:
                    cuenta_bancaria.sesion = True
                    cuenta_bancaria.save()

                    # Convierte el valor Decimal en string para almacenarlo en la sesión
                    id_nro_cta_str = str(cuenta_bancaria.id_nro_cta)
                    request.session['id_nro_cta'] = id_nro_cta_str
                    response = HttpResponseRedirect("/cajero")
                    return response
            except models.UsuarioBanco.DoesNotExist:
                pass
    else:
        form = forms.LoginForm()

    context = {
        'form': form,
    }
    return render(request, 'index.html', context)

def cajero_view(request):
    # Obtiene el valor de id_nro_cta desde la sesión y convierte de vuelta a Decimal
    id_nro_cta_str = request.session.get('id_nro_cta', None)
    id_nro_cta = Decimal(id_nro_cta_str) if id_nro_cta_str is not None else None
    
    # Obtiene la cuenta con base en el id_nro_cta
    cuenta = models.CuentaBancaria.objects.filter(id_nro_cta=id_nro_cta).first()
    context={
        'id_nro_cta': id_nro_cta,
        'cuenta': cuenta
    }
    return render(request, 'cajero.html',context)


def salir(request):
    sesion_activada = request.session.get('id_nro_cta')
    # Realiza las acciones que necesites con los valores obtenidos
    cuenta = models.CuentaBancaria.objects.get(id_nro_cta=sesion_activada)
    cuenta.sesion = False  # Actualiza el campo sesion a False
    cuenta.save()

    return render(request, 'logout.html')

def giro_view(request):
    form = forms.GiroForm()
    if request.method == 'POST':
        sesion_activada = request.session.get('id_nro_cta')
        cuenta = models.CuentaBancaria.objects.get(id_nro_cta=sesion_activada)
        form = forms.GiroForm(request.POST)  # Crear una instancia de GiroForm con los datos POST
        if form.is_valid():  # Verificar si el formulario es válido
            giro = form.cleaned_data['cantidad']
            nuevo_saldo = cuenta.balance - giro
            if nuevo_saldo <0:# Verificar saldo positivo
                context={
                    'form':form,
                    'mensaje':'Saldo Insuficiente',
                    'cuenta':cuenta
                }
                return render(request,'giro.html',context)
            else:#realiza giro si saldo es positivo
                cuenta.balance=nuevo_saldo
                cuenta.save()
                context = {
                    'cuenta': cuenta
                }
                return render(request,'balance.html',context)
        else:
            print("El formulario no es válido")
    else:#ingreso a pagina 
        id_nro_cta_str = request.session.get('id_nro_cta')
        id_nro_cta = Decimal(id_nro_cta_str) if id_nro_cta_str is not None else None
        cuenta = models.CuentaBancaria.objects.filter(id_nro_cta=id_nro_cta).first()
        context = {
            'form': form,
            'cuenta': cuenta
        }
        return render(request, 'giro.html', context)


def deposito_view(request):
    form=forms.DepositoForm()
    if request.method=='POST':
        sesion_activada = request.session.get('id_nro_cta')
        cuenta = models.CuentaBancaria.objects.get(id_nro_cta=sesion_activada)
        form = forms.GiroForm(request.POST)  # Crear una instancia de GiroForm con los datos POST
        if form.is_valid():  # Verificar si el formulario es válido
            deposito = form.cleaned_data['cantidad']
            nuevo_saldo = cuenta.balance +deposito
            cuenta.balance=nuevo_saldo
            cuenta.save()
            context = {
                    'cuenta': cuenta
                }
            return render(request,'balance.html',context)
        else:
            context = {
                'form': form,
                'cuenta': cuenta
            }
            return render(request, 'deposito.html', context)

    else:
        id_nro_cta_str = request.session.get('id_nro_cta', None)
        id_nro_cta = Decimal(id_nro_cta_str) if id_nro_cta_str is not None else None
        cuenta = models.CuentaBancaria.objects.filter(id_nro_cta=id_nro_cta).first()
        context={
            'form':form,
            'cuenta':cuenta
        }
        return render(request,'deposito.html',context)

def balance_view(request):
    id_nro_cta_str = request.session.get('id_nro_cta')
    id_nro_cta = Decimal(id_nro_cta_str) if id_nro_cta_str is not None else None
    cuenta = models.CuentaBancaria.objects.filter(id_nro_cta=id_nro_cta).first()
    context={
        'cuenta':cuenta
    }
    return render(request,'balance.html',context)