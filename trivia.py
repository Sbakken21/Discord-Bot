from discord.ext import commands
import aiohttp
import random
import html

class Trivia():
    """Trivia related commands"""

    def __init__(self, bot):
        self.bot = bot

    async def fetch_token(self, session, url):
        # Get token from Open Trivia API
        async with session.get(url) as response:
            data = await response.json()
            question_url = f'https://opentdb.com/api.php?amount=1{self.selected_category}&token={data["token"]}'

            async with aiohttp.ClientSession() as session:
                return await self.fetch_data(session, question_url)

    async def fetch_data(self, session, url):
        # Obtain question data from API
        async with session.get(url) as response:
            data = await response.json()
            question_data = data["results"][0]
            return question_data

    def replace_chars(self, str):
        # Replace special characters from question data
        new_str = html.unescape(str)
        return new_str

    @commands.command()
    async def trivia(self, *, user_category = ''):
        """Get a random trivia question from a variety of topics"""

        # If user selects category, apply category to API else return no category
        if user_category.lower() == 'anime':
            self.selected_category = f'&category=31'
        elif user_category.lower() == 'general':
            self.selected_category = f'&category=9'
        elif user_category.lower().replace(" ","") == 'videogames':
            self.selected_category = f'&category=15'
        else:
            self.selected_category = ''

        async with aiohttp.ClientSession() as session:
            # Request token from Open Trivia API
            trivia_data = await self.fetch_token(session, 'https://opentdb.com/api_token.php?command=request')
            question = self.replace_chars(trivia_data["question"])
            category = trivia_data["category"]
            difficulty = trivia_data["difficulty"]
            self.correct_answer = self.replace_chars(trivia_data["correct_answer"])
            # Combine correct and incorrect answer choices
            choices_array = [trivia_data["correct_answer"]] + trivia_data["incorrect_answers"]
            # Shuffle answer choices
            random_choices = random.sample(choices_array, len(choices_array))

            # After choices are shuffled, apply corresponding answer choice
            choice_num = 1
            self.num_choices = []
            for choice in random_choices:
                choice = f'{str(choice_num)}. {choice}'
                self.num_choices.append(choice)
                choice_num += 1

            choices = self.replace_chars('\n'.join(self.num_choices))
            await self.bot.say(f'Question: {question} \nCategory: {category}\nDifficulty: {difficulty}\nChoices: \n{choices}')

    @commands.command()
    async def answer(self, answer : int):
        """answer a question by using /answer 1-4"""

        # Check if answer corresponds to answer choice
        user_answer = self.num_choices[answer-1]
        user_answer = self.replace_chars(user_answer)
        # Remove answer choice (3. ) from the comparison
        if user_answer[3:] == self.correct_answer:
            await self.bot.say('CORRECT')
        else:
            await self.bot.say(f'INCORRECT\nThe correct answer is: {self.correct_answer}')

    @commands.command()
    async def categories(self):
        """List of trivia categories"""
        await self.bot.say(f'The following is the list of available categories: \nGeneral\nVideo games\nAnime')

def setup(bot):
    bot.add_cog(Trivia(bot))