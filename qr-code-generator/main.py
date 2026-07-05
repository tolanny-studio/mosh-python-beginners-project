import qrcode


def validate_color(color):
    """Validate that the input is a hexadecimal color code (#RRGGBB)."""
    # Ensure the color has the correct format.
    if len(color) != 7 or not color.startswith("#"):
        return False

    # Verify that each character after '#' is a valid hexadecimal digit.
    for char in color[1:]:
        if not ("0" <= char <= "9" or "A" <= char <= "F"):
            return False

    return True


def generate_color():
    """Prompt the user for custom QR code colors or use the default colors."""
    while True:
        generate = input(
            "Do you want a customized foreground and background color "
            "(Black and White are the default colors) [y/n]: "
        ).lower()

        # Continue prompting until a valid response is entered.
        if generate not in ("y", "n"):
            print("Invalid input")
            continue

        # Collect and validate custom colors.
        if generate == "y":
            while True:
                foreground_color = (
                    input("Enter foreground color (format #RRGGBB): ")
                    .upper()
                    .strip()
                )

                if not validate_color(foreground_color):
                    print("Invalid foreground color🎨")
                    continue

                background_color = (
                    input("Enter background color (format #RRGGBB): ")
                    .upper()
                    .strip()
                )

                if not validate_color(background_color):
                    print("Invalid background color🎨")
                    continue

                return foreground_color, background_color

        # Use the default black-and-white color scheme.
        return "#000000", "#FFFFFF"


def get_qr_input():
    """Prompt the user for the text or URL to encode."""
    while True:
        text_input = input("Enter text or URL: ").strip()

        # Require a minimum amount of input.
        if len(text_input) < 5:
            print("Input must be at least 5 characters long🔤")
            continue

        return text_input


def generate_file():
    """Prompt the user for the output file name."""
    while True:
        file_name = input("Enter file output name: ").strip()

        # Prevent empty file names.
        if not file_name:
            print("File name cannot be empty📪")
            continue

        return file_name


def generate_qr_code():
    """Generate and save a customized QR code image."""

    # Collect the information required to generate the QR code.
    qr_input = get_qr_input()
    file_name = generate_file()
    export_file = f"{file_name}.png"

    # Configure the QR code generator.
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    # Encode the user's data into the QR code.
    qr.add_data(qr_input)
    qr.make(fit=True)

    # Generate the image using the selected colors.
    foreground_color, background_color = generate_color()
    img = qr.make_image(
        fill_color=foreground_color,
        back_color=background_color,
    )

    # Save the generated QR code image.
    try:
        img.save(export_file)
        print(f"Successfully generated {export_file} 🗃️")
    except Exception as e:
        print(f"Failed to save QR code⛔: {e}")


# Run the program only when this file is executed directly.
if __name__ == "__main__":
    generate_qr_code()