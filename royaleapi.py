import requests
auth_header = { "auth":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NjIzLCJpZGVuIjoiMTcyOTY0MDcxNzM2MzQ0NTc2IiwibWQiOnt9LCJ0cyI6MTUyNzQ4MTU1NzYzM30.U7qzLMMsc3HRZIBnHYlt55uWxh92orMPAqGdyxZKUT8" }
base_link = "https://api.royaleapi.com/"
biochem_warfare = "Y900LQ8L"
savage_bros = "R2OV8L"
def get_json_from_link(url):
	response = 	requests.get(url, headers=auth_header)
	return response.json()
def get_player(tag):
	url = base_link + "player/" + tag
	return get_json_from_link(url)
def get_clan(tag):
	url = base_link + "clan/" + tag
	return get_json_from_link(url)
def get_clan_war_log(tag):
	url = base_link + "clan/" + tag + "/warlog"
	return get_json_from_link(url)
def print_previous_war_stats(player_tag, war_log):
	wins = battles = 0
	for war in war_log:
		war_participants = war["participants"]
		for participant in war_participants:
			if participant["tag"] == player_tag:
				wins = wins + participant["wins"]
				battles = battles + participant["battlesPlayed"]
				print("Cards earned:", participant["cardsEarned"])
				print("Battles played:", participant["battlesPlayed"])
				print("Wins:", participant["wins"])
				print("-------------------------")
				break
	if battles == 0:
		win_rate = -1
	else:
		win_rate = wins / battles * 100
	print("Win rate:", win_rate)
def print_previous_war_winrate(player_tag, war_log):
	wins = battles = 0
	for war in war_log:
		war_participants = war["participants"]
		for participant in war_participants:
			if participant["tag"] == player_tag:
				wins = wins + participant["wins"]
				battles = battles + participant["battlesPlayed"]
				break
	if battles == 0:
		win_rate = -1
	else:
		win_rate = wins / battles * 100
	print("Player Tag:", player_tag)
	print("Win rate:", win_rate)
def get_player_stats_from_war(player_tag, clan_tag):
	war_log = get_clan_war_log(clan_tag)
	print_previous_war_stats(player_tag, war_log)
def get_clan_war_win_rates(clan_tag):
	clan = get_clan(clan_tag)
	members = clan["members"]
	war_log = get_clan_war_log(clan_tag)
	for mem in members:
		print("Name:", mem["name"])
		print_previous_war_winrate(mem["tag"], war_log)
		print("---------------------")
# if __name__ == "__main__":
	# data = get_player(biochem_warfare)
	# print(data["games"])
	# get_player_stats_from_war("2LGJVJQJ", savage_bros)