import colorama
import webbrowser

print()
print("┌──────────────────────────────────────────┐");
print("│                                          │");
print(f"│   {colorama.Fore.MAGENTA}{colorama.Style.BRIGHT} Served! {colorama.Style.RESET_ALL}                              │");
print("│                                          │");
print(f"│   {colorama.Style.DIM}{colorama.Fore.MAGENTA}➜{colorama.Style.RESET_ALL}  {colorama.Style.BRIGHT}Local: {colorama.Style.RESET_ALL}https://localhost:3249       │");
print(f"│   {colorama.Style.DIM}{colorama.Fore.MAGENTA}➜{colorama.Style.RESET_ALL}  {colorama.Style.BRIGHT}Network: {colorama.Style.RESET_ALL}https://127.0.0.1:3249     │");
print("│                                          │");

webbrowser.open_new_tab('https://localhost:3249')