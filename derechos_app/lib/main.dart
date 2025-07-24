import 'package:flutter/material.dart';

//Aqui importamos las subpantallas donde se podran visualizar los pdfs
import 'screens/screen_constitucion.dart';
import 'screens/screen_codigotrabajo.dart';

void main() {
  runApp(const DerechosApp());
}

//Aqui definimos cosas concretas de la app como son el nombre,
//el color base de la app, y definimos como "PantallaInicio"
//a la primera pantalla que se mostrara a los usuarios
class DerechosApp extends StatelessWidget {
  const DerechosApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Derechos Laborales y Sociales',
      theme: ThemeData(primarySwatch: Colors.indigo),
      home: const PantallaInicio(),
      debugShowCheckedModeBanner: false,
    );
  }
}

//En esta clase "PantallaInicio" esta todo el contenido que se muestra en
//la pantalla principal, como un titulo principal en la parte superior,
//tambien tenemos en el apartado de body un texto introductorio.
class PantallaInicio extends StatelessWidget {
  const PantallaInicio({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Derechos Laborales y Sociales'),
        centerTitle: true,
      ),

      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text(
              'En Ecuador, los derechos laborales y sociales están protegidos por la Constitución y el Código del Trabajo, garantizando un trato digno, remuneración justa, seguridad social y condiciones de trabajo seguras para todos los trabajadores.',
              style: TextStyle(fontSize: 16),
              textAlign: TextAlign.justify,
            ),
            const SizedBox(height: 30),

            Center(
              child: Column(
                children: [
                  //Aqui tenemos definido un boton llamado
                  //"Constitución del Ecuador" el cual nos ayudara
                  //haciendo click a navegar hacia la subpantalla definida como
                  //"PantallaPDFConstitucion"
                  ElevatedButton.icon(
                    icon: const Icon(Icons.picture_as_pdf),
                    label: const Text('Constitución del Ecuador'),
                    onPressed: () {
                      Navigator.push(
                        context,
                        MaterialPageRoute(
                          builder: (context) => const PantallaPDFConstitucion(),
                        ),
                      );
                    },
                    style: ElevatedButton.styleFrom(
                      minimumSize: const Size(double.infinity, 50),
                    ),
                  ),
                  const SizedBox(height: 16),

                  //Aqui tenemos definido un segundo boton llamado
                  //"Código del Trabajo" el cual nos ayudara
                  //haciendo click a navegar hacia la subpantalla definida como
                  //"PantallaPDFCodigoTrabajo"
                  ElevatedButton.icon(
                    icon: const Icon(Icons.work),
                    label: const Text('Código del Trabajo'),
                    onPressed: () {
                      Navigator.push(
                        context,
                        MaterialPageRoute(
                          builder: (context) =>
                              const PantallaPDFCodigoTrabajo(),
                        ),
                      );
                    },
                    style: ElevatedButton.styleFrom(
                      minimumSize: const Size(double.infinity, 50),
                    ),
                  ),
                  const SizedBox(height: 16),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
