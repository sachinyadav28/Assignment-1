package pdftask;

import com.lowagie.text.Document;

import com.lowagie.text.DocumentException;

import com.lowagie.text.pdf.PdfWriter;

import com.lowagie.text.rtf.parser.RtfParser;

import java.io.FileInputStream;

import java.io.FileNotFoundException;

import java.io.FileOutputStream;

import java.io.IOException;

public class App {

    public static void main(String[] args) {
    
     String inputFile = "sample_rtf_file.rtf";
    
     String outputFile = "sample_pdf_file.pdf";
    
     // create a new document
    
     Document document = new Document();
    
     try {
    
         // create a PDF writer to save the new document to disk
         PdfWriter writer = PdfWriter.getInstance(document, new FileOutputStream(outputFile));

     // open the document for modifications

     document.open();
     // create a new parser to load the RTF file

     RtfParser parser = new RtfParser(null);

     // read the rtf file into a compatible document

     parser.convertRtfDocument(new FileInputStream(inputFile), document);

     // save the pdf to disk

     document.close();

     System.out.println("Finished");

 } catch (DocumentException e) {

     e.printStackTrace();

 } catch (FileNotFoundException e) {

     e.printStackTrace();

 } catch (IOException e) {

     e.printStackTrace();

 }

}

}