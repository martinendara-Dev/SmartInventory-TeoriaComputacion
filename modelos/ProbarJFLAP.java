import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.HashMap;
import automata.Automaton;
import automata.fsa.FSAStepByStateSimulator;
import file.XMLCodec;

/** Ejecuta los .jff con el motor ORIGINAL de JFLAP 7.1, no una imitación. */
class ProbarJFLAP {
    public static void main(String[] args) throws Exception {
        Path carpeta = Path.of(args.length == 0 ? "modelos" : args[0]);
        int cantidad = 0;
        System.out.println("Motor: automata.fsa.FSAStepByStateSimulator de JFLAP 7.1");
        for (String linea : Files.readAllLines(carpeta.resolve("pruebas.tsv"))) {
            String[] campos = linea.split("\t");
            Automaton modelo = (Automaton) new XMLCodec().decode(
                new File(carpeta.resolve(campos[0]+".jff").toString()), new HashMap<>());
            boolean resultado = new FSAStepByStateSimulator(modelo).simulateInput(campos[1]);
            boolean esperado = Boolean.parseBoolean(campos[2]);
            System.out.println(campos[0]+" | "+campos[1]+" | "+(resultado ? "Accept" : "Reject")
                +" | "+(resultado == esperado ? "OK" : "FALLO"));
            if (resultado != esperado) throw new AssertionError(linea);
            cantidad++;
        }
        System.out.println(cantidad+" secuencias correctas.");
        System.exit(0);
    }
}
