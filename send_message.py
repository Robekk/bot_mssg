import asyncio
from telegram import Bot

# Replace 'YOUR_TOKEN_HERE' with your bot's token
bot_token = 'YOUR_TOKEN_HERE'
bot = Bot(token=bot_token)
message = message = f"""          
                Your prefer bot name here

           your detail here
           you can use more detail like:
           1. {total_accounts}
           2. {total_balance_all_accounts:,.0f}
           

            == xyzuan dump ==
            """


# Replace 'YOUR_GROUP_ID' with your group ID. It should be a negative number for groups.
group_id = -234242736472634287  # Example group ID

async def send_message():
    # Send a message
    await bot.send_message(chat_id=group_id, text=message)

# Run the async function
if __name__ == "__main__":
    asyncio.run(send_message())