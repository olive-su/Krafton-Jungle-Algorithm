def bm_match(txt, pat):
    skip = [len(pat)] * 27 # 알파벳 수대로 건너뛰기 표 생성

    for pt in range(len(pat)):
        # 패턴 길이 - 패턴 인덱스 - 1
        skip[ord(pat[pt]) - ord('A')] = len(pat) - pt - 1 # n - k -1
    
    print(pt)
    '''
    @pt : text_pointer
    @pp : pattern_pointer
    '''
    while pt < len(txt):
        pp = len(pat) - 1
        while txt[pt] == pat[pp]:
            if pp == 0:
                return pt
            pt -= 1
            pp -= 1
        # 같은 문자열 처리를 위함 (Ex. pattern="ABCA" -> "A"의 처리)
        # 더 많이 건너 뛰기 위함
        if skip[ord(txt[pt]) - ord('A')] > len(pat) - pp:
            pt += skip[ord(txt[pt]) - ord('A')] # skip 이 더 큰 경우 : 일반적인 경우
        else:
            pt += len(pat) - pp 
    
    return -1


# print(bm_match("ABCXDEZAACACABAC", "BAAC"))
# print(bm_match("ABCXDEZCACACABAC", "ABAC"))