def solution(new_id):
    #1 모두 소문자
    new_id = new_id.lower()

    # 2 소문자, 숫자, 빼기, 밑줄, 마침표 제외한 모든 문자 제거

    for i in new_id :
        if i.isalnum() == True :
            continue
        elif i in ['-', '_', '.'] :
            continue
        else :
            new_id = new_id.replace(i, '')        

    # 3 마침표가 2번이상 연속되면 하나로 치환

    while '..' in new_id :
        new_id = new_id.replace('..', '.')

    # 4 마침표가 처음이나 마지막에 있으면 제거

    new_id = list(new_id)
    if new_id[0] == '.' :
        new_id[0] = ''
    if new_id[-1] == '.' :
        new_id[-1] = ''

    new_id = ''.join(map(str, new_id))

    # 5 new_id가 빈 문자열이면 'a' 대입

    if len(new_id) == 0 :
        new_id += 'a'

    # 6 16글자 이상이면 15개 제외 모두 제거

    new_id = list(new_id)
    if len(new_id) >= 16 :
        new_id = new_id[:15]
        if new_id[-1] == '.' :
            del new_id[-1]

    new_id = ''.join(map(str, new_id))

    # 7 new_id가 2자 이하면 new_id 마지막 글자를 길이가 3까지 반복
    while len(new_id) < 3:
        new_id += new_id[-1]
    return new_id

