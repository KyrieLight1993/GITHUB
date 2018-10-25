import java.util.*;
import java.text.*;

public class Game
/**
 * Player A and Player B are playing the RPS game.
 * 2 Up-quark one Down-quark made a proton.
 * Positive is Up Negative is Down
 * Its all about 3, 6, 9...
 * If you are single to 30, 
 * you will be able to use the big magic 
 * to turn your cat into a girlfriend...
 * You need to get a cat first.
 */
{
    public static void main(String[] args) {


        final int scissor = 3;

        final int rock = -6;

        final int paper = 9;

        int a = -1;

        int b = -1;

        String winner = new String();

        Scanner inputScan = new Scanner(System.in);

        System.out.println ( "3 for scissor, -6 for rock, 9 for paper Player A please enter your number here_ ");

        a = inputScan.nextInt ();

        System.out.println ( "3 for scissor, -6 for rock, 9 for paper Player B please enter your number here_ ");

        b = inputScan.nextInt ();

        switch(a-b){

            case 0 :

            winner = "none"; 

            System.out.println ("draw");

            break; 

            case -6 :

            case -9 :

            case 15 :

            winner = "player A" ;

            System.out.println ( winner + " win!");

            break; 

            case 9 :

            case -15 :

            case 6 :

            winner = "player B" ;

            System.out.println ( winner + " win!");

            break;

            default : 

            System.out.println ( "invalid input !");

            break;

        }


    }
}