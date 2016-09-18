from my_custom_prompt import MyCustomPrompt

c = get_config()

c.TerminalInteractiveShell.prompts_class = MyCustomPrompt
c.TerminalIPythonApp.display_banner = False
c.TerminalInteractiveShell.confirm_exit = False
c.TerminalInteractiveShell.term_title = True
c.TerminalInteractiveShell.separate_in = ''

