def solution(participant, completion):
    participant.sort()
    completion.sort()
    # print(participant)
    # print(completion)
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            if participant[i+1] == completion[i]:
                return participant[i]
            return participant[i+1]       
    return participant[i+1]