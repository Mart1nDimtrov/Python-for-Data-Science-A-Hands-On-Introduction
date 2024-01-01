# Exercise #1: Improved Photo Tag Analysis

l = [
	 {
	  "name": "photo1.jpg",
	  "tags": {'coffee', 'breakfast', 'drink', 'table', 'tableware', 'cup', 'food'}
	 },
	 {
	  "name": "photo2.jpg",
	  "tags": {'food', 'dish', 'meat', 'meal', 'tableware', 'dinner', 'vegetable'}
	 },
	 {
	  "name": "photo3.jpg",
	  "tags": {'city', 'skyline', 'cityscape', 'skyscraper', 'architecture', 'building', 'travel'}
	 },
	 {
	  "name": "photo4.jpg",
	  "tags": {'drink', 'juice', 'glass', 'meal', 'fruit', 'food', 'grapes'}
	 }
	]

photo_groups = {}

for i in l:
	for 