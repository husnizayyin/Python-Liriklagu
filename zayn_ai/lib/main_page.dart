import 'dart:io';

import 'package:flutter/material.dart';
import 'package:google_generative_ai/google_generative_ai.dart';
import 'package:image_picker/image_picker.dart';
import 'package:zayn_ai/general_variable.dart';

class MainPage extends StatefulWidget {
  const MainPage({super.key});

  @override
  State<MainPage> createState() => _MainPageState();
}

class _MainPageState extends State<MainPage> {
  TextEditingController textEditingController = TextEditingController();
  String answer = '';
  XFile? image;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          backgroundColor: Colors.amber.shade100,
          title: const Text('Zayn AI'),
        ),
        body: Padding(
          padding: const EdgeInsets.all(20),
          child: ListView(
            children: [
              TextField(
                  controller: textEditingController,
                  decoration: const InputDecoration(
                    hintText: 'Enter your request here',
                    border: OutlineInputBorder(),
                  )),
              const SizedBox(height: 20),
              Container(
                width: double.infinity,
                height: 100,
                decoration: BoxDecoration(
                    color: image == null ? Colors.grey.shade200 : null,
                    image: image != null
                        ? DecorationImage(image: FileImage(File(image!.path)))
                        : null),
              ),
              const SizedBox(height: 20),
              ElevatedButton(
                onPressed: () {
                  ImagePicker().pickImage(source: ImageSource.gallery).then(
                    (value) {
                      setState(() {
                        image = value;
                      });
                    },
                  );
                },
                child: const Text('Pick Image'),
              ),
              ElevatedButton(
                onPressed: () {
                  GenerativeModel model = GenerativeModel(model: 'gemini-1.5-flash-latest',apiKey: apiKey);
                  model.generateContent([
                    Content.multi([
                      TextPart(textEditingController.text),
                      if (image != null)
                       DataPart('image/jpeg', File(image!.path).readAsBytesSync())
                    ])
                  ]).then((value) {
                    setState(() {
                      answer = value.text.toString();
                    });
                  });
                
                },
                child: const Text('Send'),
              ),
              const SizedBox(height: 20),
              Text(answer),
            ],
          ),
        ));
  }
}
