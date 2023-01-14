import random

# Funkcja tworząca talię kart
def create_deck():
    suits = ['Kier', 'Karo', 'Trefl', 'Pik']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Walet', 'Dama', 'Król', 'As']
    deck = []
    for suit in suits:
        for rank in ranks:
            card = rank + ' ' + suit
            deck.append(card)
    return deck

# Funkcja pobierająca losową kartę z talii
def get_card(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card

# Funkcja obliczająca punkty karty
def get_points(card):
    rank = card.split()[0]
    if rank in ['Walet', 'Dama', 'Król']:
        return 10
    elif rank == 'As':
        return 11
    else:
        return int(rank)

# Funkcja rozgrywająca rundę
def play_round():
    deck = create_deck()
    player_cards = [get_card(deck), get_card(deck)]
    dealer_cards = [get_card(deck), get_card(deck)]
    player_points = sum(get_points(card) for card in player_cards)
    dealer_points = sum(get_points(card) for card in dealer_cards)
    print(f'Twoje karty: {player_cards}, punkty: {player_points}')
    print(f'Karty dealera: {dealer_cards[0]} i ***')
    while True:
        choice = input('Chcesz dobrać kartę? (t/n) ')
        if choice.lower() == 't':
            player_cards.append(get_card(deck))
            player_points = sum(get_points(card) for card in player_cards)
            print(f'Twoje karty: {player_cards}, punkty: {player_points}')
            if player_points > 21:
                print('Przegrałeś!')
                return False
        else:
            break
    print(f'Karty dealera: {dealer_cards}, punkty: {dealer_points}')
    while dealer_points < 17:
        dealer_cards.append(get_card(deck))
        dealer_points = sum(get_points(card) for card in dealer_cards)
        print(f'Karty dealera: {dealer_cards}, punkty: {dealer_points}')
        if dealer_points > 21:
            print('Wygrałeś!')
            return True
    if player_points > dealer_points:
        print('Wygrałeś!')
        return True
    elif player_points == dealer_points:
      print('Remis!')
      return None
    else:
      print('Przegrałeś!')
      return False
# Pętla gry

while True:
  result = play_round()
  if result is None:
    play_again = input("Remis! Czy chcesz zagrać jeszcze raz? (t/n)")
  else:
    play_again = input("Czy chcesz zagrać jeszcze raz? (t/n)")
  if play_again.lower() != 't':
    break
