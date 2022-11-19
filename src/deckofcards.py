from requests import get

class DeckOfCards:
	def __init__(self) -> None:
		self.api = "http://deckofcardsapi.com/api"
		self.headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
		}
	
	def shuffle_cards(self, deck_count: int = 1) -> dict:
		return get(
			f"{self.api}/deck/new/shuffle/?deck_count={deck_count}",
			headers=self.headers).json()
	
	def draw_card(
			self,
			deck_id: str = "new",
			count: int = 1) -> dict:
		return get(
			f"{self.api}/deck/{deck_id}/draw/?count={count}",
			headers=self.headers).json()
	
	def reshuffle_cards(
			self,
			deck_id: str,
			remaining: bool = False) -> dict:
		url = f"{self.api}/deck/{deck_id}/shuffle"
		if remaining:
			url += f"?remaining={remaining}"
		return get(url, headers=self.headers).json()
	
	def brand_new_deck(
			self,
			jokers_enabled: bool = False) -> dict:
		return get(
			f"{self.api}/deck/new?jokers_enabled={jokers_enabled}",
			headers=self.headers).json()
	
	def partial_deck(
			self,
			cards: str = "AS,2S,KS,AD,2D,KD,AC,2C,KC,AH,2H,KH") -> dict:
		return get(
			f"{self.api}/deck/new/shuffle/?cards={cards}",
			headers=self.headers).json()
	
	def add_to_piles(
			self,
			deck_id: str,
			pile_name: str,
			cards: str = "AS,2S") -> dict:
		return get(
			f"{self.api}/deck/{deck_id}/pile/{pile_name}/add?cards={cards}",
			headers=self.headers).json()
	
	def shuffle_piles(
			self,
			deck_id: str,
			pile_name: str) -> dict:
		return get(
			f"{self.api}/deck/{deck_id}/pile/{pile_name}/shuffle",
			headers=self.headers).json()
	
	def listing_cards_in_piles(
			self,
			deck_id: str,
			pile_name: str) -> dict:
		return get(
			f"{self.api}/deck/{deck_id}/pile/{pile_name}/list",
			headers=self.headers).json()
	
	def draw_from_cards(
			self,
			deck_id: str,
			pile_name: str,
			cards: str = "AS,2S") -> dict:
		return get(
			f"{self.api}/deck/{deck_id}/pile/{pile_name}/draw?cards={cards}",
			headers=self.headers).json()
	
	def draw_from_count(
			self,
			deck_id: str,
			pile_name: str,
			count: int) -> dict:
		return get(
			f"{self.api}/deck/{deck_id}/pile/{pile_name}/draw?count={count}",
			headers=self.headers).json()
			
	def draw_bottom(self, deck_id: str) -> dict:
		return get(
			f"{self.api}/deck/{deck_id}/draw/bottom",
			headers=self.headers).json()
	
	def draw_random(self, deck_id: str) -> dict:
		return get(
			f"{self.api}/deck/{deck_id}/draw/random",
			headers=self.headers).json()
	
	def return_cards(self, deck_id: str) -> dict:
		return get(
			f"{self.api}/deck/{deck_id}/return",
			headers=self.headers).json()
