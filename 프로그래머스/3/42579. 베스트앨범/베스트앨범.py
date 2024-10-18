def solution(genres, plays):
    answer = []
    
    play={}
    genre={}
    
    for i in range(len(genres)):
        if genres[i] in play :
            play[genres[i]] += plays[i]
        else :
            play[genres[i]]=plays[i]
        if genres[i] in genre:
            genre[genres[i]].append([plays[i],i])
        else :
            genre[genres[i]]=[[plays[i],i]]
            
    #print(play,genre)
     
    genre_list=sorted(play.items(), key=lambda x : x[1], reverse=True)
    
    #print(genre_list)
    
    for g,p in genre_list:
        genre[g]=sorted(genre[g],key=lambda x : x[0], reverse =True)
        #print(genre[g])
        
        for i,j in genre[g][:2]:
            answer.append(j)
    
    return answer