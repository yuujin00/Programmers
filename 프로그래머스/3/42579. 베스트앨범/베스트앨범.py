def solution(genres, plays):
    answer = []
    
    play={} #{'classic': 1450, 'pop': 3100}
    genre={} #{'classic': [[500, 0], [150, 2], [800, 3]], 'pop': [[600, 1], [2500, 4]]}
    
    for i in range (len(genres)) :
        if genres[i] in play :
            play[genres[i]] += plays[i]
            genre[genres[i]].append([plays[i],i])
        else :
            play[genres[i]] = plays[i]
            genre[genres[i]] = [[plays[i],i]]
    
    genrelist=sorted(play.items(),key=lambda x : x[1], reverse=True)
    # ['pop', 'classic']
    
    for (g, p) in genrelist :
        # 재생횟수 내림차순
        genre[g] = sorted(genre[g],key=lambda x : x[0], reverse=True)
        answer+=[j for (i,j) in genre[g][:2]]
    
        
    return answer