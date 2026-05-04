from typing import Literal
import requests
from pydantic import BaseModel, Field
from subprocess import call
from os import name

# Requirements:
#     * requests
#     * pydantic


# Schema
class Responce(BaseModel):
    count: int
    name: str
    gender: Literal["male", "female"]
    probability: float = Field(ge=0, le=1)


# Core Logic with 3rd-Party sasti RestAPI
class Genderize:
    BASE_URL = f"https://api.genderize.io"

    @staticmethod
    def get_gender(name: str) -> Responce:
        res = requests.get(f"{Genderize.BASE_URL}?name={name}")
        return Responce.model_validate(res.json())


class User:
    # Pata nahi Kyu
    def clear_console():
        call("cls" if name == "nt" else "clear")

    # hey GPT Make it For me
    def confirm_exit() -> bool:
        prompt = f"""
    \033[1;31m╔══════════════════════════════════════════════════════╗\033[0m
    \033[1;31m║        🚪💀 WAIT… YOU'RE LEAVING ALREADY? 💀🚪       ║\033[0m
    \033[1;31m╠══════════════════════════════════════════════════════╣\033[0m

    \033[1;33m😒 Wow. That was quick.\033[0m  
    \033[1;37mWas it something I said? Or are you just done here?\033[0m  

    \033[1;36m👉 Type \033[1;32m[Y]\033[0m to dramatically exit  
    \033[1;36m👉 Type \033[1;32m[N]\033[0m to pretend this never happened  

    \033[1;31m╚══════════════════════════════════════════════════════╝\033[0m
    \033[1;32m>>>\033[0m """

        choice = input(prompt).strip().lower()
        return choice in ("y", "yes")

    # hey GPT Make it For me
    def display(data: Responce) -> None:
        print(f"""
    \033[1;35m╔══════════════════════════════════════════════════════╗\033[0m
    \033[1;35m║        🎭✨ OH WOW, A LIFE-CHANGING RESULT ✨🎭      ║\033[0m
    \033[1;35m╠══════════════════════════════════════════════════════╣\033[0m

    \033[1;33m🙄 Name:\033[0m            \033[1;37m{data.name}\033[0m  
    \033[1;36m🔢 Count:\033[0m           \033[1;37m{data.count}\033[0m  

    \033[1;32m⚧ Gender Guess:\033[0m    \033[1;37m{data.gender.upper()}\033[0m  
    \033[1;31m🎯 Probability:\033[0m    \033[1;37m{data.probability:.2%}\033[0m  

    \033[1;34m💡 Insight:\033[0m  
    \033[1;37mBecause clearly, numbers never lie… right? 🤖\033[0m  
    \033[1;37mWe are {data.probability:.2%} confident — which is basically\033[0m  
    \033[1;37m"trust me bro" but with math. 📊\033[0m  

    \033[1;35m╠══════════════════════════════════════════════════════╣\033[0m
    \033[1;35m║   🧠 Generated with supreme artificial confidence™   ║\033[0m
    \033[1;35m╚══════════════════════════════════════════════════════╝\033[0m
    """)

    # hey GPT Make it For me
    def get_name() -> str:
        template = f"""
    \033[1;35m╔══════════════════════════════════════════════════════╗\033[0m
    \033[1;35m║        🎭✨ WELCOME TO THE NAME GUESS-O-MATIC ✨🎭   ║\033[0m
    \033[1;35m╠══════════════════════════════════════════════════════╣\033[0m

    \033[1;33m🤔 Oh brilliant human, what shall we call you?\033[0m  
    \033[1;37m(Yes, your *actual* name… not "Batman")\033[0m  

    \033[1;36m👉 Enter your name here:\033[0m  \033[1;32m>>>\033[0m """
        print(template, end="")
        name = input()
        print("""
    \033[1;35m╠══════════════════════════════════════════════════════╣\033[0m
    \033[1;35m║   💬 Bold choice. Let’s see what we can do with that ║\033[0m
    \033[1;35m╚══════════════════════════════════════════════════════╝\033[0m
    """)
        return name.strip()

    def goodbye_message() -> None:
        User.clear_console()
        print(f"""
    \033[1;35m╔══════════════════════════════════════════════════════╗\033[0m
    \033[1;35m║          👋✨ THANKS FOR PLAYING! ✨👋               ║\033[0m
    \033[1;35m╠══════════════════════════════════════════════════════╣\033[0m

    \033[1;32m🎉 Well played ! You survived the madness.\033[0m  
    \033[1;36m😄 Hope you had fun and maybe learned... something?\033[0m  

    \033[1;33m🚪 Exiting the Name Guess-O-Matic...\033[0m  
    \033[1;31m💔 Don’t worry, we’ll miss you (a little).\033[0m  

    \033[1;35m╠══════════════════════════════════════════════════════╣\033[0m
    \033[1;35m║         🌟 Come back soon for more fun! 🌟           ║\033[0m
    \033[1;35m╚══════════════════════════════════════════════════════╝\033[0m
""")


class UserHandler:
    def run():
        try:
            User.clear_console()
            while user_input := User.get_name():
                data = Genderize.get_gender(user_input)
                User.display(data)
                exit(0) if User.confirm_exit() else User.clear_console()
        except KeyboardInterrupt:
            User.goodbye_message()


# main logic aise hi
def main() -> None:
    UserHandler.run()


# Ye to rousson se pucho
if __name__ == "__main__":
    main()