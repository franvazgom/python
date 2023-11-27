# Carrito de compras
## Configuración de ambiente
1. Descomprimir el archivo 01_webrestaurante.zip
2. Crear un entorno virtual
3. Instalar las librerías del archivo requirements.txt
4. Verificar el funcionamiento de la aplicación
```python
usuario     = admin
password    = hola1234 
```

## Análisis y diagrama de secuencia
## FrontEnd
1. Colocar la imágen del carrito de compras
```html
<li class="nav-item px-lg-4">
    <a class="nav-link text-secondary" href="#" onclick='#'> 
        <i class="fas fa-shopping-cart"> <span id='cart-badge' class="badge badge-danger">0</span> </i>
    </a>
</li>
```
2. Estructura de almacenamiento del carrito <br>
    |product_id|Quantity|
    |----------|--------|
    | 1 | 4 |
    | 2 | 2 |
    | 3 | 1 |
```javascript
    cart = {1:4, 2:2, 3:1}; 
```
3. El carrito es un diccionario en javaScript que se almacena en el localstorage <br> 
```javascript
// Verificar si el carrito se encuentra en el localstorage. 
if (localStorage.getItem('cart') == null) {
    localStorage.clear();
    var cart = {};
} else {   // En caso de que se encuetre en el localstorage se convierte a json, para su manipulación
    cart = JSON.parse(localStorage.getItem('cart'));
    show_badge_cart();
}
```
4. Crear función para mostrar el total de elementos que se encuentran en el carrito <br>
```javascript
function show_badge_cart() {
    var totalItems = 0;
    if (localStorage.getItem('cart') != null) {
        cart = JSON.parse(localStorage.getItem('cart'));
        for (var x in cart) {
            totalItems += parseInt(cart[x]);
        }
    }
    $('#cart-badge').text(totalItems.toString());
}
```
Verificar las funciones de js, desde la consola, ejecutar: 
```javascript
    cart = {1:4, 2:2, 3:1}
    localStorage.setItem('cart', JSON.stringify(cart))
    show_badge_cart(); 
```

5. Crear función para agregar un producto al carrito <br>
```javascript
function addCart(idProduct) {
    if (cart[idProduct] != undefined) {
        cart[idProduct] += 1;
    } else {
        cart[idProduct] = 1;
    }
    localStorage.setItem('cart', JSON.stringify(cart));
    show_badge_cart();
}
```
Verificar la función de js, desde la consola, ejecutar: 
```javascript
    addCart(1)
    addCart(1)
    addCart(2)
    show_badge_cart(); 
```
6. En el archivo service_list, colocar el botón para agregar al carrito de compras
```html
<a class="btn btn-primary" 
    onclick='addCart({{service.id}})' >Agrega al carrito
</a>
```
Verificar su funcionamiento <br>

7. Crear el archivo detail_order.html <br>
```html
<div class="container">
    <div class="row mt-2">
        <div class="col-md-9 mx-auto mb-1">
            <table class="table table-bordered">
                <thead class="text-white">
                    <tr>
                        <th>Id</th>
                        <th>Títutlo</th>
                        <th>Sub título</th>
                        <th>Cantidad</th>
                        <th style='text-align: right'>Costo unitario</th>
                        <th style='text-align: right'>Subtotal</th>
                    </tr>
                </thead>
                <tbody class="text-white">
                    <tr>
                        <td>1</td>
                        <td>Producto 1</td>
                        <td>Subtitulo 1</td>
                        <td>4</td>
                        <td style='text-align: right'>$350.00</td>
                        <td style='text-align: right'>$1,400.00</td>
                    </tr>
                    <tr>
                        <td>3</td>
                        <td>Producto 3</td>
                        <td>Subtitulo 3</td>
                        <td>1</td>
                        <td style='text-align: right'>$195.00</td>
                        <td style='text-align: right'>$195.00</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    <div class="row mt-1">
        <div class="col-md-9 mx-auto mb-2">
            <div style='text-align:right;'>
                <span class="text-white">
                    Total = $1,595.00
                </span>
            </div>
        </div>
    </div>
    <div class="row mt-1">
        <div class="col-md-9 mx-auto mb-2">
            <div id='button_submit' style='text-align:right;'>
                <a href="#" class="btn text-white form-btn mx-1">
                    <span class="spinner-border spinner-border-sm d-none"></span>
                    <i class="fas fa-paper-plane fa-fw"></i> Confirmar pedido
                </a>
            </div>
        </div>
    </div>
</div>
```
## BackEnd
8. Dentro del archivo views.py crear el método detail_order
```python
def detail_order(request):
    return render(request, 'services/detail_order.html')

# Agregar el path en el archivo urls.py
path('detail_order/', views.detail_order, name='detail_order'),
``` 
 Verificar su funcionamiento:  /services/detail_order


Crear formulario y función para mostrar el pedido <br>
```html
<form id='cartForm' action="{% url 'services:detail_order' %}" method='post'>
    {% csrf_token %}
    <input type="hidden" name='order_data' id='order_data'>
</form>
```

```javascript
function showOrder() {
    if (localStorage.getItem('cart') != null) {
        $('#order_data').val(localStorage.getItem('cart'));
        $('#cartForm').submit();
    }
}
```

## BackEnd
1. view.py 

```python
def detail_order(request):
    order = list()
    if request.method == 'POST':
        str_order_data = request.POST['order_data']
        order_data = json.loads(str_order_data)
        total = 0
        cost = 1650
        for product in order_data.keys():
            qty = order_data[product]
            if qty > 0:
                key = int(product)
                service = Service.objects.get(pk=key)
                dict_product = {}
                dict_product['id'] = service.id
                dict_product['title'] = service.title
                dict_product['sub_title'] = service.sub_title
                dict_product['quantity'] = qty
                dict_product['cost'] = cost
                dict_product['subtotal'] = cost * qty
                total += qty * 100
                order.append(dict_product)
        #Se colocan las variables en session
        request.session['total_float'] = float(total) 
        request.session['detail_order'] = order
    return render(request, 'services/detail_order.html', {'order':order, 'total':total})

```
Template 
```html
    <tbody class="text-white">
        {% for product in order  %}
        <tr>
            <td>{{product.id}}</td>
            <td>{{product.title}}</td>
            <td>{{product.sub_title}}</td>
            <td>{{product.quantity}}</td>
            <td style='text-align: right'>${{product.cost|floatformat:2|intcomma  }}</td>
            <td style='text-align: right'>${{product.subtotal|floatformat:2|intcomma }}</td>
        </tr>    
        {% endfor %}
    </tbody>

    <div class="row mt-1">
        <div class="col-md-9 mx-auto mb-2">
            <div style='text-align:right;'>
                <span class="text-white">
                    Total = ${{total|floatformat:2|intcomma}}
                </span>
            </div>
        </div>
    </div>
```
### Librería django humanize 
`pip install django-humanize`  <br>
settings.config <br> 
'django.contrib.humanize',


2. Modelo para el pedido
``` python
class Order(models.Model):
    email           = models.EmailField(verbose_name='Email')
    name            = models.CharField(max_length=100, verbose_name='Nombre')
    address         = models.CharField(max_length=200, verbose_name='Dirección')
    neighborhood    = models.CharField(max_length=200, verbose_name='Colonia o fraccionamiento')
    total           = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Total') 
    date            = models.DateTimeField(auto_now_add=True, verbose_name='Fecha del pedido')

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['-date']

    def __str__(self):
        return str(self.id)
```
