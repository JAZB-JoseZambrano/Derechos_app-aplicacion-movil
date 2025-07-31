import 'package:flutter/material.dart';
import 'package:syncfusion_flutter_pdfviewer/pdfviewer.dart';
import 'package:http/http.dart' as http;

class PantallaPDFConstitucion extends StatelessWidget {
  const PantallaPDFConstitucion({super.key});

  //En este apartado colocamos la direccion url donde este alojado
  //el pdf que deseamos mostrar al usuario, previamente subido
  //a nuestro servidor, el cual debe esta ativo para que se
  //visualize el pdf en el app.
  final String urlPDF =
      'http://app.capacitacioncontinua.info/uploads/pdfs/constitucion.pdf';

  //En este apartado se encarga de verificar la peticion,
  //si el servidor responde con el codigo "200" significa
  //que el pdf si existe y que podemos visualizarlo,
  //si ocurre un error sin conexion o mal escrito el url
  //retorna false
  Future<bool> verificarPDF() async {
    try {
      final response = await http.head(Uri.parse(urlPDF));
      return response.statusCode == 200;
    } catch (_) {
      return false;
    }
  }

  //Aqui teenemos un AppBar que nos mostrara un titulo en la parte superior.
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Constitución del Ecuador')),

      //En este apartado tenemos un FutureBuilder es un widget que esta
      //a la espera de la verificacion del pdf (future: verificarPDF)
      //si la verificacion dio una respuesta positiva mostrara el pdf, y si
      //hubo un error o el pdf no esta disponible mostrara
      //un mensaje de error.
      body: FutureBuilder<bool>(
        future: verificarPDF(),
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return const Center(child: CircularProgressIndicator());
          } else if (snapshot.hasError || !snapshot.data!) {
            return const Center(
              child: Text('Error al cargar el PDF. Inténtalo más tarde.'),
            );
          } else {
            return SfPdfViewer.network(urlPDF);
          }
        },
      ),
    );
  }
}
