namespace _9_Palindrome_Number;

internal class Program
{
    static void Main(string[] args)
    {
        var var1 = Palindrome.IsPalindrome(1221);
        Console.WriteLine(var1);
    }
}
public class Palindrome
{
    public static bool IsPalindrome(int num)
    {
        int rest = (num > 0) ? num : 0;
        int digit = 0, inverse = 0;

        while (rest > 0)
        {
            digit = rest % 10;
            rest = rest / 10;
            inverse = inverse * 10 + digit;
        }
        return num == inverse;
    }
}
