def open_and_add_to_list(file_name):
	with open(file_name) as my_file:
		output_list = my_file.readlines()
		output_list_stripped = []
		for i in output_list:
			output_list_stripped.append(i.strip())
	return output_list_stripped

# open the file of your favorite foods.
# read all of your favorite foods into a list called [your_name]_favs
# read all of your pair's favorite foods into a list called [their_name]_favs
# read all of your pair's favorite foods into a list called [their_name]_favs

def compare_favs(amy_fav_list,erin_fav_list):
	for i in range(len(amy_fav_list)):
		if amy_fav_list[i] == erin_fav_list[i]: 
			print "Our favs are the same!"
		else:
			print "Our favs are not the same :("


# create a function called compare_favs that takes two arguments, the list of your favs and the list of your pair's. 
# This function should print "Our favorite foods are the same!" if your top favorite food is the same as your pairs.
# Otherwise, the function should print "Our favorite foods are different"


def main():
	amy_fav_list = open_and_add_to_list("amy_fav_foods.txt")
	erin_fav_list = open_and_add_to_list("erin_fav_foods.txt")
	compare_favs(amy_fav_list,erin_fav_list)



# Call the compare_favs function with your favs and your pair's favs
# Run compare_favs.py! Make sure it works!


if __name__ == '__main__':
	main()