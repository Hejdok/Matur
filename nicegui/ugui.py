from nicegui import ui

def example():
    ui.notify("Button works!")


def example2():
    ui.notify("Button2")

buttons = {
    "Button 1": example,
    "Button 2": example2
}

with ui.element("div").classes("flex items-center justify-center flex-col h-screen w-full gap-5"):
    ui.label("Hello").classes("text-teal-300 text-4xl")
    ui.label("Bye").style("color: red")

    with ui.grid(columns=3):
        for name, func in buttons.items():
            ui.button(name, on_click=func)

ui.run(native=True)