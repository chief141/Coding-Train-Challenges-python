''' Search if a number is present in the first
	1 million digits of pi and if it does search
	the position of that number in the first 1 million digits of pi

	Done by https://chief141.github.io
'''


print("			Enter the number you want to search")
print("			in the first 1 million digits of pi")
print("			It should be of more than one digit")
print()

#LOADING FILE
pi_file = "one-million-digits-pi.txt"
try: 
	with open(pi_file, 'r') as f:
		d = f.read()    # READING DATA
		d = d.split('.')  # REMOVING FIRST 3 AND . FROM THE NUMBER
		data = d[1]   # STORING THE DATA
		data = [current_input_char for current_input_char in data]

except Exception as e:
	print(f"Cannot open {pi_file}")
	print(f"Error :  {e}")
	data = False

if data:
	while True:
		inp = input("Enter the number you want to search : ")
		if inp == "" or len(inp) < 2:
			print("Enter atleast two digits")	
			
		else:
			try : 
				int(inp)
				not_int = True
			except:
				not_int = False

			if not_int:
				try:
					first_char = inp[0]

					list_of_index = [current_input_char for current_input_char, value in enumerate(data) if value == first_char]
					if len(list_of_index) > 0:
						m = 0
						
						adding_index  =  1
						index_of_current_input_char  =   1
						current_input_char  =  inp[index_of_current_input_char]

						while index_of_current_input_char < len(inp) and m < len(list_of_index):

							current_input_char = inp[index_of_current_input_char]
							index = list_of_index[m]

							if current_input_char == data[index + adding_index]:
								adding_index += 1
								index_of_current_input_char += 1
								present = True

							else :
								present = False
								adding_index = 0
								index_of_current_input_char = 0
								m += 1

						if present:
							print(f"Found {inp} at {list_of_index[m] + 1} position in the first 1 Million digits of pi ")
						else:
							print(f"{inp} in not present in the first 1 Million digits of pi")

				except Exception as e:
					print("An unexpected error occured ")
					print(f"Error :  {e}")
			else:
				print("type a number...")

		print()
		print()
