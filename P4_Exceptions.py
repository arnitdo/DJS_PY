from common_utils import dump_info

dump_info()

# Name Error
try:
	c = a + 5
except NameError as e:
	print(f"A NameError occurred: {e}")

# Type Error
try:
	x = int('abc')
except ValueError as e:
	print(f"A ValueError occurred: {e}")

try:
	y = 'a' + 5
except TypeError as e:
	print(f"A TypeError occurred: {e}")

try:
	5 / 0
except ZeroDivisionError as e:
	print(f"A ZeroDivisionError occurred: {e}")		

try:
	some_arr = []
	print(some_arr[1])
except IndexError as e:
	print(f"A IndexError occurred: {e}")		

class NumberTooLowException(Exception):
	pass

class NumberTooHighException(Exception):
	pass


while True:
	try:
		some_num = int(input("Guess the number: "))
		if (some_num < 10):
			raise NumberTooLowException
		elif (some_num > 10):
			raise NumberTooHighException
		else:
			print("You guessed correctly!")
			break
	except NumberTooLowException:
		print("You guessed too low!")
		continue
	except NumberTooHighException:
		print("You guessed too high")
		continue
	except ValueError:
		print("Invalid input!")
		continue
	except KeyboardInterrupt:
		break
	except:
		print("Other error occurred!")