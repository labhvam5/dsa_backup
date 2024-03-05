def find_num(word):
    help_dict = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'zero': '0'
    }

    nums = ['one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine',
        'zero'
    ]
    for num in nums:
        if num in word:
            return help_dict[num]

    return -1

s = "shnds9"
result = ""
i=0
j=0
while(i< len(s)):
    if not s[i].isdigit():
        j=i
        while((j < len(s)) and (not s[j].isdigit())):
            j += 1
        digit = find_num(s[i:j])
        if digit != -1:
            result += digit
        i = j-1
    else:
        result += s[i]
    res = ""
    i +=1

sum = int(result[0]) + int(result[len(result)-1])
print(sum) 

# 139439
