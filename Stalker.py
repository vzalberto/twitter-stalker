# Needs https://github.com/bear/python-twitter
# Only works with for small timelines. Consider Twitter's API rate limiting

def GetEntireUserTimeline(user):
	stCount = api.GetUser(screen_name=user).statuses_count
	timeline = api.GetUserTimeline(screen_name=user)
	while len(timeline) < stCount:
		 timeline.extend(api.GetUserTimeline(screen_name=user, max_id=timeline[len(timeline)-1].id))
	return timeline

