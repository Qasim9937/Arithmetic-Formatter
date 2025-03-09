def arithmetic_arranger(problems, show_answers=False):
     
    if len(problems) <= 5:

        row1, row2, dashes, answer = '','','',''
    
        for problem in problems:

            num1,operator,num2 = problem.split()

            if len(num1) > 4 or len(num2) > 4:
                return 'Error: Numbers cannot be more than four digits.'    

            elif not num1.isdigit() or not num2.isdigit(): 
                print(num1.isdigit())
                return 'Error: Numbers must only contain digits.'

            elif operator != '+' and operator != '-':
                return "Error: Operator must be '+' or '-'."

        
            out1 = num1 + ' ' * 4
            out2 = operator + ' ' + num2 + ' ' * 4 if len(num2) >= len(num1) else operator + ' ' + ' ' *  (len(num1) - len(num2)) + num2 + ' ' * 4
            space = len(out2) if len(out2) >= len(out1) else len(out1)
            ans = str(int(num1) + int(num2)) + ' ' * 4 if operator == '+' else str(int(num1) - int(num2)) + ' ' * 4

            row1 += f'{out1:>{space}}'
            row2 += f'{out2:>{space}}'
            dashes += '-' * len(out2.strip()) + ' ' * 4
            answer += f'{ans:>{space}}'
            
        if not show_answers:   
            return row1.rstrip()+'\n'+row2.rstrip()+'\n'+dashes.rstrip()

        else:
            return row1.rstrip()+'\n'+row2.rstrip()+'\n'+dashes.rstrip()+'\n'+answer.rstrip()
                

    else:
        return 'Error: Too many problems.' 
