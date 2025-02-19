public class Moyenne {

    // Méthode pour vérifier la validité des notes
    private static boolean estValide(int note) {
        return note >= 0 && note <= 20;
    }

    // Méthode pour calculer la moyenne et afficher la mention
    public static void calculerMoyenne(int n1, int n2, int n3) {
        // Vérifier la validité des notes
        if (!estValide(n1) || !estValide(n2) || !estValide(n3)) {
            System.out.println("Erreur : Les notes doivent être comprises entre 0 et 20.");
            return; // Arrêter l'exécution si une note est invalide
        }

        // Calculer la moyenne
        double moyenne = (n1 + n2 + n3) / 3.0;

        // Afficher la moyenne
        System.out.println("La moyenne est : " + moyenne);

        // Déterminer et afficher la mention
        if (moyenne < 10) {
            System.out.println("Mention : Insuffisant");
        } else if (moyenne >= 10 && moyenne < 15) {
            System.out.println("Mention : Correct");
        } else {
            System.out.println("Mention : Excellent");
        }
    }

    // Méthode principale pour tester la classe
    public static void main(String[] args) {
        // Exemples de test
        calculerMoyenne(12, 14, 16); // Cas valide
        calculerMoyenne(8, 21, 15);  // Cas invalide (note 21)
        calculerMoyenne(5, 10, 18);  // Cas valide
    }
}
