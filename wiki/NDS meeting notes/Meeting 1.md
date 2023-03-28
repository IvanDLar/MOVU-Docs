# Meeting 1

## Go’s

- [x]  Compra de autos en cualquier estado
- [x]  Validación de identidad del usuario
- [x]  Buscar autos por reconocimiento de lenguaje natural
    - Proceso guiado de filtrado
- [x]  Las agencias deben poder configurar los documentos necesarios para el proceso de compra de un auto
- [x]  Ofrecer auto como enganche
    - Subir fotos
- [x]  Servicio para comunicarte en tiempo real con el vendedor
- [x]  Cada grupo automotriz deben poder configurar sus planes de financiamiento
    - Planes de arrendamiento
- [x]  Deben poder subir sus seguros
- [x]  Integración de pagos
    - Stripe
    - OpenPay
- [x]  Mecanismos de negociación
- [x]  Toda actividad debe poder ser trackeada con fines de auditoria.
- [x]  Que cada agencia pueda configurar la información de sus cuentas bancarias para que ahí se les depositen los pagos por stripe.
    - Como agencia debes poder ver el historial de pagos
- [x]  Buscar y visualizar autos sin requerir inicio de sesión
    - Para comprar sí se requiere cuenta
- [x]  Almacenar información de los usuarios
    - Info confidencial cifrada
    - Cumplir con estándares de seguridad internacionales
        - ~~GDPR compliance~~
    - Mantener info con vigencia
- [x]  MFA support
- [x]  Mandar notificaciones a inactivos
- [x]  Garantizar principio de menor privilegio
    - Cada quien debe de ver solo lo que le corresponde
- [x]  Utilizar plataformas y tech stack seguros

## No go’s

- Proceso de validación para la agencia
- Intervenir en los coches/información listada
- Validar documentos del usuario
- Venta de particulares a particulares
- Proceso de entrega
- Proceso de pruebas de manejo

## Roles

- [x]  Superadmin
    - Revisar solicitudes de las empresas
    - Aprobar o rechazar agencias
- [x]  Administrador de un grupo automotriz
    - Validar documentos en automatico
        - Acta constitutiva…algo
        - Registro en el SAT…algo
        - Comprobante de domicilio
        - Telefono, correo
        - Notificar una vez que el proceso sea finalizado
    - Dar de alta agencias y gerentes
- [x]  Gerentes de agencias
    - Puede hacerse cargo de varias agencias
    - Dar de alta vendedores
- [x]  Vendedores
    - Solo pueden pertenecer a una agencia
    - Gestionar catalogo de vehículos
    - Solicitudes de pruebas de manejo
- [x]  Pensar en el usuario

### Thoughts

- Tech stack a nuestro criterio
- Value added para la agencia es una plataforma de estadísticas de las ventas
- Entender bien el proceso de adquisición de un cliente
    - Necesitamos poder mostrar esta información
- Pueden subir sus propios datos
    - Como podríamos ayudar a integrarlos a nuestro sistema?
- Propuesta del modelo de datos.
- No es necesario registrarse?
- Guía autométrica
- Quieren mostrar los precios reales
- Backups?

### Pending Questions

- ~~Se busca ofrecer un servicio de seguros~~
- Hay restricciones de donde pueden estar los datos?
- ~~Es nuestra responsabilidad validar la identidad de un usuario?~~
- ~~Es nuestra responsabilidad llevar el proceso de la entrega del auto?~~

## Stretch feats

- [x]  Comparación entre autos
- [ ]  ~~Pagos de las mensualidades desde la plataforma~~
- [x]  Plan de recomendación de autos
- [x]  Generación de estadísticas
    - Descarga de reportes
    - Usuarios que han visto tus vehículos
        - Desglose de los leads
- [x]  Ver estadísticas diferentes según el tipo de usuario
- [x]  Rating y reviews de agencias
    - Machine learning

## Values

- Transparencia
    - Mostrar total de pago desglosado
    - Enganche
    - Mensualidades
    - Seguro
- Funcionalidad > Diseño
- User First

### Monetización

- [x]  Comisión por cada vehículo publicado
- [x]  Pagar por prioridad de búsqueda

---

Inicio a fin de momento digital sin moverse de su casa

Coches: nuevos y seminuevos

## Proceso

Pruebas de manejo a donde quieran

Si dos grupos dan el mismo coche, el usuario elige

## Financiamiento

Enganche, financiamiento, contado

Tiene que tener integracion con pasasrela de pago.

Pueda poner datos de cualquier metodo de pago, incluyendo trasferencia.

Si es de contado: depende del banco el limite

Por medio de la agencia

Cada agencia debe de poder subir sus planes de financiamiento y seguros

## Otros

Todo el proceso se debe de documentar

Analizar cuanto cuesta por mes operar, cuanto de comision

## Documentos

Para prueba de manejo:

INE 

Licencia

Cada agencia puede poner poner lo que quiera, puede subir  diferentes formatos.

Para persona fisica:

- 3 estados de cuenta, 6 nominas. Depende de cual sea tu regimen fiscal.
- Empresarial: 3 estados de cuenta
- Asalariada: 6 recibos de nomina
- Comprobante de domicillio: luz, agua, telefono,gas
- Ine
- Formato

# Modelo de negocios

Cobrar comision por coche a las agencias

Debe permitir comision por auto, por prueba de manejo, por numero de agencias

Por cada vehiculo comision, solo por subir

Para los clientes es GRATIS

# Legal

Ellos se encargan de terminos de uso, proteccion,etc…

# Agencia

Puede subir autos para comercializar, sin importar donde este el coche

Cada empresa puede poner cuanto por llevarlo a la casa (puede estar incluido en el precio)

Pasan por processo de autorizacion

Se debe poder negociar, descuentos

Tambien pueden subir planes de arrendamiento

Subir

Acta constitutiva

Cedua fiscal

Documentos legales 

Comporbante de domicillio

Info de cuentas bancarias donde quieren recibir los pagos

NO SE HACE AUTOMATICO

Ver historial de pagos

# Roles

Super admin:

Personas encargadas de processo de valdiacion de empresas

Aprovar/Rechazar solicitudes

Porque se rechaza, que se accepto

Admin de un grupo:

Dar de alta al grupo

Registro, documentos

Gestionar jerarquia dentro de organizacion

Toda la info de todas las agencias

Administrar agencias

Dar de alta gerente de cada

Ver a nivel de grupo cada proesso

Gentes:

Puede tener muchas agencias de el grupo

Ver info de todos los vehiculos de los vendedores

Ver todo que son gerentes

Dar de alta vendedores y dar permisos

Vendedor:

Solo una agencia

Gestionar autos, subir, actualizar.

Llegan solictidudes de adq y pruebas de manejo, responsable de dar seguimiento.

# Info

Manejar autos en la plataforma

Meter autos de afuera

Estandarizar info