import discord
from discord import app_commands
from discord.ext import commands
from discord import utils
import random

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

TOKEN = "MTA0OTk2ODExNDcxNDAzODM2Mw.GNSRkI.lZA7m02W26Cw1u54-yHWMQXrjN4R83ObBFDvew"

bot = commands.Bot(command_prefix="!", intents=intents)



@bot.event
async def on_ready():
    print("discord bot in started working!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)


@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"hello")


@bot.tree.command(name='rps', description="rock paper scissors")
async def rps(interaction: discord.Interaction, choice: str):
    options = ['камень', 'бумага', 'ножницы']
    computer_choice = random.choice(options)
    
    if choice not in options:
        return await interaction.response.send_message("Неверный ввод. Выберите «камень», «бумага» или «ножницы».")
    
    result = None
    if choice == computer_choice:
        result = 'ничья🤝🏻'
    elif choice == 'камень' and computer_choice == 'ножницы':
        result = 'ты выиграл😎'
    elif choice == 'бумага' and computer_choice == 'камень':
        result = 'ты выиграл😎'
    elif choice == 'ножницы' and computer_choice == 'бумага':
        result = 'ты выиграл😎'
    else:
        result = 'ты проиграл😥'
    
    await interaction.response.send_message(f'Вы выбрали **{choice}**. Компьютер выбрал **{computer_choice}**. **{result}**!')


board = [' ' for x in range(9)]

def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    return "\n".join([row1, row2, row3])

def is_winner(char):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]  # diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == char:
            return True
    return False

@bot.tree.command(name='ttt', description="playing a tic tac toe")
async def tic_tac_toe(interaction: discord.Interaction, cell: int):
    global board
    player = "X" if board.count("X") == board.count("O") else "O"
    board[cell - 1] = player
    
    if is_winner(player):
        await interaction.response.send_message(f'{player} wins!\n\n{print_board()}')
        board = [' ' for x in range(9)]
    elif not any([space == ' ' for space in board]):
        await interaction.response.send_message(f'Tie!\n\n{print_board()}')
        board = [' ' for x in range(9)]
    else:
        await interaction.response.send_message(f'{player}\'s turn.\n\n{print_board()}')


@bot.tree.command(name="random")
async def random_int(interaction: discord.Interaction, first: int, last: int):
    result = random.randint(first, last)
    print(f"рандомное число от {first} до {last}: **{result}**")
    await interaction.response.send_message(f"рандомное число от {first} до {last}: **{result}**")


# @bot.tree.command(name="coin")
# async def coin(interaction: discord.Interaction, choice: str):
#     options = ["орёл","решка"]
#     rand = random.choice(options)
#     print(rand)

#     if rand == choice:
#         await interaction.response.send_message(f"выпал {rand}, ты выиграл😎")
#     elif rand != choice:
#         await interaction.response.send_message(f"выпал {rand}, ты проиграл😥")


@bot.tree.command(name="coin", description="")
async def coin(interaction: discord.Interaction, choice: str):
    optionse = ["орёл", "орел"]
    optionst = ["решка"]
    options = [optionse, optionst]
    digit = random.randint(0, 1)
    rand = (options[digit])

    if choice in rand:
        await interaction.response.send_message(f"выпал {rand[0]}, ты выиграл😎")
    else:
        await interaction.response.send_message(f"выпал {rand[0]}, ты проиграл😥")


@bot.tree.command(name="say")
async def say(interaction: discord.Interaction, say: str):
    await interaction.response.send_message(f"{say}")

bot.run(TOKEN)
