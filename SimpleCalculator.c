#include <stdio.h>
#include <stdlib.h>

int main()
{
    //ข้อความที่เป็นภาษา Eng อิงจากข้อมูลในเว็บต่างชาติ juu
    char ch;   //Stores a single character/letter/number
    double a, b;  //Stores fractional numbers, containing one or more decimals. Sufficient for storing 15 decimal digits
    while (1) {
        printf("Enter an operator (+, -, *, /), "
               "Exit write E: ");
        scanf(" %c", &ch);
 
        // กดEออก
        if (ch == 'E')
            exit(0);

        //ใส่จำนวนตัวแรกกับตัวที่สองที่จะคำนวณ Ex. 5 10
        printf("Enter First and Sec operand: ");
        scanf("%lf %lf", &a, &b);    /*For printf, arguments of type float are promoted to double so both %f and %lf are used for double. 
                                      For scanf, you should use %f for float and %lf for double*/
 
        // สำหรับการแบบเลือกใช้เครื่องหมายอันอื่นๆให้มันทำยังไง
        // การทำงานต่างๆอยู่ที่ เครื่องหมาย


        /*%f is the format specifier used for float data type in the functions printf and scanf . 
        By default it will display values upto 6 digits after the decimal point but , 
        writing %.1f or %.2f will reduce the precision to 1 or 2 digits respectively*/
        switch (ch) {
 
        // บวก
        case '+':
            printf("%.1lf + %.1lf = %.1lf\n", a, b, a + b);
            break;
 
        // ลบ
        case '-':
            printf("%.1lf - %.1lf = %.1lf\n", a, b, a - b);
            break;
 
        // คูณ
        case '*':
            printf("%.1lf * %.1lf = %.1lf\n", a, b, a * b);
            break;
 
        // หาร
        case '/':
            printf("%.1lf / %.1lf = %.1lf\n", a, b, a / b);
            break;
 
        // ถ้าตัวแปลไม่อยู่ใน 4ตัวนี้ให้ Error
        default:
            printf(
                "Error please write Correct Operator ( +, -, *, /)\n");
        }
 
        printf("\n");
    }
}