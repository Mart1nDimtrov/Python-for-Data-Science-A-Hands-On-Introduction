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
	for key, value in i.items():
		if key == "name":
			photo_name_outer = value
			#print(key)
			#print(photo_name_outer)
		if key == 'tags':
			for tag_1 in value:
				tag_outer = tag_1
				print(tag_outer)
				for i_2 in l:
					for key_2, value_2 in i_2.items():
						if key_2 == "name":
							photo_name_inner = value_2
							#print(key)
							#print(photo_name_outer)
						if key_2 == 'tags':
							for tag_2 in value_2:
								if tag_1 == tag_2 and photo_name_inner != photo_name_outer:
									photo_groups[tag_1] = {photo_name_inner, photo_name_outer}
				

print(photo_groups)