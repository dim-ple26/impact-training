def can_win(cards):
  n=len(cards)
  for i in range(n):
    if cards[i]==1:
      cards[i]=-1 
      if i>0 and cards[i-1]!=-1:
        cards[i-1]^=1
      if i<n-1 and cards[i+1]!=1:
        cards[i+1]^=1 
  return all(card== -1 for card in cards)



initial_cards=[1,0,1,0,1]
print(can_win(initial_cards))

initial_cards=[1,0,0]
print(can_win(initial_cards))


cards_state={
  1:"down",
  2:"up",
  3:"down"
}
keys_to_modify = [key for key, value in cards_state.items() if value == "up"]

for key in keys_to_modify:

      if key-1 in cards_state:
         cards_state[key-1]="up"
       
      if key+1 in cards_state:
         cards_state[key+1]="up"
      
      cards_state.pop(key)
    
print(cards_state)

  