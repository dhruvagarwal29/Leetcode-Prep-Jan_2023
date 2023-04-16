# generate all the combinations of balanced paranthesis

def generate_paranthesis(num):
    result = []
    result.append('(') # insert the 1st open bracket 
    open_bracket_count = 0
    close_bracket_count = 0
    while close_bracket_count < num:
        current_size = len(result)
        for i in range(current_size):
            current_bracket = result.pop(0)
            open_bracket_count = current_bracket.count('(')
            close_bracket_count = current_bracket.count(')')

            if open_bracket_count < num:
                result.append(current_bracket + "(")
                if close_bracket_count < open_bracket_count:
                    result.append(current_bracket + ")")
                    close_bracket_count += 1
                open_bracket_count+=1
            
            else:
                result.append(current_bracket + ")")
                close_bracket_count += 1

        # breaking condition for the loop

        
        # close_bracket_count = result[0].count(')')

        # if close_bracket_count == num:
        #     break

    return result


if __name__=="__main__":
    print(generate_paranthesis(3))