class InputHandler:

    @staticmethod
    def get_float(prompt, min_value=None, max_value=None):
        while True:
            try:
                value = float(input(prompt))

                if min_value is not None and value < min_value:
                    print(f"Value must be at least {min_value}.")
                    continue

                if max_value is not None and value > max_value:
                    print(f"Value must be no greater than {max_value}.")
                    continue

                return value

            except ValueError:
                print("Invalid input. Please enter a number.")

    @staticmethod
    def get_menu_choice(prompt, valid_choices):
        while True:
            choice = input(prompt).strip()

            if choice in valid_choices:
                return valid_choices[choice]

            print("Invalid choice. Please try again.")

    @staticmethod
    def get_projectile_inputs():
        velocity = InputHandler.get_float(
            "Enter velocity (m/s): ",
            min_value=0
        )

        angle = InputHandler.get_float(
            "Enter launch angle (degrees): ",
            min_value=0,
            max_value=90
        )

        return velocity, angle

    @staticmethod
    def get_motion_type():
        print("\nMotion Type")
        print("1. Ideal Motion")
        print("2. Motion With Drag")

        return InputHandler.get_menu_choice(
            "Choose motion type: ",
            {
                "1": "ideal",
                "2": "drag"
            }
        )

    @staticmethod
    def get_projectile_type():
        print("\nProjectile Type")
        print("1. Baseball")
        print("2. Golf Ball")
        print("3. Soccer Ball")
        print("4. Tennis Ball")
        print("5. Custom")

        return InputHandler.get_menu_choice(
            "Choose projectile type: ",
            {
                "1": "baseball",
                "2": "golf_ball",
                "3": "soccer_ball",
                "4": "tennis_ball",
                "5": "custom"
            }
        )
    
    @staticmethod
    def get_custom_projectile_properties():
        mass = InputHandler.get_float(
            "Enter mass (kg): ",
            min_value=0.001
        )

        drag_coefficient = InputHandler.get_float(
            "Enter drag coefficient: ",
            min_value=0
        )

        diameter = InputHandler.get_float(
            "Enter diameter (m): ",
            min_value=0.001
        )

        return mass, drag_coefficient, diameter