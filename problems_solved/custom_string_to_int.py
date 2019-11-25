"""
In all common character encodings, the values are sequential: '0' has a value one less than '1', which in turn is followed by '2', '3', and so on.
 (Of course, if you didn’t know this, you’d have to ask the interviewer.) 
 Therefore, the value of a digit character is equal to the digit plus the value of '0'. ( The value of '0' is the nonzero code number representing the character '0'.)
This means you subtract the value of '0' from a digit character to find the numeric value of the digit.
 You don’t even need to know what the value of '0' is; just write -'0', which the compiler interprets as “subtract the value of '0'.”


#convert string to int ; digit_character = digit + '0' => digit = digit_character - '0'

#include<stdio.h>
#include<string.h>
void main(int argc,char** argv){
int num=0,len,i=0,neg=0;
len = strlen(argv[1]);
char neg_num = "-";
if (argv[1][0] == neg_num )
{
        neg = 1;
        i++;
}
while( i < len )
{
num *= 10;
num += ( argv[1][i++] - '0' );
}
if (neg == 1) num = -num;

printf("%d \n",num);

}

#convert int to string;  digit_character = digit + '0'

#include<stdio.h>
#include<string.h>

int main(int argc,char** argv) {
int num=123,i=0,j=0;
char str[20],str1[20];

while ( num != 0 ) {
str[i++] = (char) (num % 10 + '0');
num = num/10;

}
for(i=strlen(str)-1; i>=0;i--)
{
        str1[j++] = str[i];
}

str1[j] = '\0';
printf("%s\n",str1);


return 0;
}

"""

print "hi"