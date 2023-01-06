class BotService():

    @staticmethod
    async def get_start_answer():
        answer = 'This bot will help you find the most effective teams for your goals.\n\
        WAR menu /war,\n\
        EVENTS menu /events,\n\
        MYTHICAL titan menu - /myth'
        return answer

    @staticmethod
    async def get_war_answer():
        answer = 'Choose which center you want to get an attack command for.\n\
            /mim'
        return answer

    @staticmethod
    async def get_myth_answer():
        return 'Here will be myth'

    @staticmethod
    async def get_event_answer():
        return 'Here will be events'
    
    @staticmethod
    async def get_info_answer():
        answer = 'Info section: you can give feedback or donate to the development of the project'
        return answer

    @staticmethod
    async def get_mim_answer():
        return 'Here will be picture about better command attack to mim'

services = BotService()


# try:
    #     await bot.send_photo(message.chat.id, photo='https://ibb.co/DgdTNLc')
    # except BadRequest:
