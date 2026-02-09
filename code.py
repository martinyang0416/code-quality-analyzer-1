n, k = map(int, input().split())
teams = [tuple(map(int, input().split())) for _ in range(n)]
sorted_teams = sorted(teams, key=lambda x: (-x[0], x[1]))

groups = []
current_group = []
for team in sorted_teams:
    if not current_group:
        current_group.append(team)
    else:
        last_p, last_t = current_group[0]
        if team[0] == last_p and team[1] == last_t:
            current_group.append(team)
        else:
            groups.append(current_group)
            current_group = [te