def number_to_words(number, include_and=False):
	"""returns a string representation for the given number"""
	number=int(number)
	ones=["one","two","three","four","five","six","seven","eight","nine"]
	teens=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
	tens=["twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
	if number<10:
		return ones[number-1]
	elif number<20:
		return teens[number-10]
	elif number<100:
		return tens[number//10-2]+(" "+number_to_words(number%10, include_and) if number%10!=0 else "")
	elif number<1000:
		return number_to_words(number//100)+" hundred"+((" and " if include_and else " ")+number_to_words(number%100, include_and) if number%100!=0 else "")
	elif number<1000000:
		return number_to_words(number//1000, include_and)+" thousand"+(" "+number_to_words(number%1000, include_and) if number%1000!=0 else "")
	elif number<1000000000:
		return number_to_words(number//1000000, include_and)+" million"+(" "+number_to_words(number%1000000, include_and) if number%1000000!=0 else "")