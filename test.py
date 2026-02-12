from rich.console import Console
console = Console()


def wrap(text: str, styles: list) -> str:
    styles = " ".join(styles)
    message = f"[{styles}]{text}[/{styles}]"
    return message


text_1 = "Добро пожаловать в казино"
text_2 = "У нас выйгрывает каждый пятый"

style_1 = ["green", "underline"]
style_2 = ["blue", "italic"]

message = wrap(text=text_1, styles=style_1) + " " + wrap(text=text_2, styles=style_2) 


console.print(message)