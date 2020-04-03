package pdfbox;

import java.io.File;
import org.jodconverter.core.office.OfficeException;
import org.jodconverter.core.office.OfficeUtils;
import org.jodconverter.local.JodConverter;
import org.jodconverter.local.office.LocalOfficeManager;

public class App {

    public static void main(String[] args) throws OfficeException {
    
        File inputFile = new File("sample_rtf_file.rtf");
        File outputFile = new File("sample_pdf_file.pdf");
    
     final LocalOfficeManager officeManager = LocalOfficeManager.install(); 
try {

    // Start an office process and connect to the started instance (on port 2002).
    officeManager.start();

    // Convert
    JodConverter
             .convert(inputFile)
             .to(outputFile)
             .execute();
} 
finally {
    // Stop the office process
    OfficeUtils.stopQuietly(officeManager);
}
}
}

