def remove_duplicates(input):
    '''This function will remove duplicate words from users input'''
    split_userinput=input.split(' ')
    removing_dupli = list(set(split_userinput))
    final_sentence = ' '.join(removing_dupli)
    return final_sentence

def compare(userssentence, fromdummyList):
    '''This function will return the similar count value comparing user's sentence and computer's sentence '''
    userswords=userssentence.strip().split(' ')
    dummywords=fromdummyList.strip().split(' ')
    similar_count = 0
    for uword in userswords:
        for dword in dummywords:
            if uword.lower() == dword.lower():
                similar_count += 1
    return similar_count

if  __name__  ==  '__main__':
    dumyy_list = ['python is good.', 'No 1 good boy is not bad but it is nice boy', 'No 2 python boy is python boy not snake boy']
    user_sentence = input("Search here:")
    filtered_usersentence = remove_duplicates(user_sentence)
    all_score = [compare(filtered_usersentence, sentence) for sentence in dumyy_list]
    final = [s for s in sorted(zip(all_score, dumyy_list), reverse=True) if s[0] != 0]
    print(f"{len(final)} results found!!!")
    for score, sent in final:
        print(f"{sent}")


