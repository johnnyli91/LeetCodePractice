class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = 0
        cows = 0
        unmatched_secret_numbers = []
        unmatched_guess_numbers = []
        
        for index, secret_number in enumerate(secret):
            guess_number = guess[index]
            if secret_number == guess_number:
                bulls += 1
            else:
                unmatched_secret_numbers.append(secret_number)
                unmatched_guess_numbers.append(guess_number)
                
        for number in unmatched_guess_numbers:
            if number in unmatched_secret_numbers:
                cows += 1
                unmatched_secret_numbers.remove(number)
        return "%dA%dB" % (bulls, cows)
