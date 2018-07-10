def sort_scores(unsorted_scores, highest_possible_score):
	scores_to_count = {}
	sorted_scores = []
	for score in unsorted_scores:
		scores_to_count[score] = scores_to_count.get(score, 0) + 1
	for score in scores_to_count:
		for number in range(scores_to_count[score]):
			sorted_scores.append(score)
	return sorted_scores