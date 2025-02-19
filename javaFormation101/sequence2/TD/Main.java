public class Main {
    public static void main(String[] args) {
        try {
            // Valid codePays
            Prix p1 = new Prix(100.0, 250);
            System.out.println("TVA Taux Normal: " + p1.getTVATauxNormal());
            System.out.println("Montant TTC: " + p1.calculerMontantTTC());

            // Another valid codePays
            Prix p2 = new Prix(200.0, 56);
            System.out.println("TVA Taux Normal: " + p2.getTVATauxNormal());
            System.out.println("Montant TTC: " + p2.calculerMontantTTC());

            // Invalid codePays (will throw an exception)
            Prix p3 = new Prix(300.0, 33); // This will throw an IllegalArgumentException
        } catch(IllegalArgumentException e) {
            System.out.println("Ne pas autorese: " + e.getMessage());


        }
}
}
