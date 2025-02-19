

/**
 * Classe Prix
 * 
 * Classe permettant de stocker les informations relatives à un prix
 * 
 * Un objet Prix est caractérisé par:
 * - un montant HT
 * - un code de pays fr 250 et be 52
 * 
 * Un objet Prix permet de:
 * - obtenir le taux de TVA normal en fonction du code pays
 * 
 * Exemple d'utilisation:
 * Prix p = new Prix(100.0, 250);
 * System.out.println(p.getTVATauxNormal());
 * 
 * Sortie:
 * 0.20
 */

public class Prix {
    private double montantHT;
    private int codePays;

     public Prix (double montantHT , int codePays){
            
           if (codePays != 250 && codePays != 56) {
                throw new IllegalArgumentException("codePays must be either 250 or 56");
            }
            
            this.montantHT = montantHT; // montantHT est un attribut de l'objet courant
            this.codePays = codePays; // codePays est un attribut de l'objet courant
     }

     public double getTVATauxNormal(){
        if (codePays == 250) return 0.20;
        else return 0.21;

     }
   public double calculerMontantTTC() {
      double tauxTVA = getTVATauxNormal();
      return montantHT * (1 + tauxTVA);
   }

}