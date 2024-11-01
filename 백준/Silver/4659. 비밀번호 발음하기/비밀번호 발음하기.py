while True :
    text=input()

    if text=='end':
        break

    vowels='aeiou'

    answer=True

    for v in vowels :
        if v in text :
            break
    else : 
        answer=False

    v_cnt=0
    c_cnt=0

    for t in text :
        if t in vowels :
            v_cnt+=1
            c_cnt=0
        else :
            c_cnt+=1
            v_cnt=0

        if v_cnt==3 or c_cnt==3 :
            answer=False
            break

    for i in range(1,len(text)):
        if text[i]==text[i-1] and text[i] not in {'e','o'}:
            answer=False
            break

    if answer:
        print(f'<{text}> is acceptable.')
    else :
        print(f'<{text}> is not acceptable.')