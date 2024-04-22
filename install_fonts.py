import os
import win32com.client

def install_fonts(fonts_dir):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    font_dir = os.path.join(current_dir, fonts_dir)

    font_viewer = win32com.client.Dispatch("Shell.Application")

    if not os.path.exists(font_dir):
        print(f"Directory '{font_dir}' does not exist.")
        return

    font_files = [f for f in os.listdir(font_dir) if f.endswith('.ttf')]

    if not font_files:
        print(f"No font files found in '{font_dir}'.")
        return

    installed_fonts = [font.Name for font in font_viewer.Namespace(0x14).Items()]

    for font_file in font_files:
        font_path = os.path.join(font_dir, font_file)

        if font_file not in installed_fonts:
            font_viewer.Namespace(0x14).CopyHere(font_path)

            # Wait until font installation is complete
            while font_file not in installed_fonts:
                installed_fonts = [font.Name for font in font_viewer.Namespace(0x14).Items()]

            print(f"Installed font: {font_file}")
        else:
            print(f"Font '{font_file}' is already installed.")

# Change the directory to the path where your fonts are located
fonts_directory = "fonts"

install_fonts(fonts_directory)
