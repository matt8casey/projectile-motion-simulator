class Display:

    @staticmethod
    def show_welcome():
        print("\n===================================")
        print("      Physics Projectile Tool")
        print("===================================")
        print("Calculate ideal projectile motion")
        print("or compare motion with air drag.")

    @staticmethod
    def _print_results(title, results):
        print(f"\n=== {title} ===")
        print(f"Range: {results['range']:.2f} m")
        print(f"Maximum Height: {results['max_height']:.2f} m")
        print(f"Flight Time: {results['flight_time']:.2f} s")

        if "terminal_velocity" in results:
            print(
                f"Terminal Velocity: "
                f"{results['terminal_velocity']:.2f} m/s"
            )

        if "max_speed_reached" in results:
            print(
                f"Maximum Speed Reached: "
                f"{results['max_speed_reached']:.2f} m/s"
            )

    @staticmethod
    def show_ideal_results(projectile):
        Display._print_results(
            "IDEAL PROJECTILE MOTION",
            projectile.get_ideal_results()
        )

    @staticmethod
    def show_drag_results(projectile):
        Display._print_results(
            "PROJECTILE MOTION WITH DRAG",
            projectile.get_drag_results()
        )

    @staticmethod
    def show_comparison_results(projectile):
        results = projectile.get_comparison_results()

        ideal = results["ideal"]
        drag = results["drag"]

        print("\n=== COMPARISON: IDEAL VS DRAG ===")

        Display._print_results(
            "IDEAL MOTION",
            ideal
        )

        Display._print_results(
            "MOTION WITH DRAG",
            drag
        )

        print("\n=== DIFFERENCE ===")
        print(
            f"Range Difference: "
            f"{results['range_difference']:.2f} m"
        )
        print(
            f"Percent Difference: "
            f"{results['percent_difference']:.2f}%"
        )

    @staticmethod
    def show_error(message):
        print("\nError:")
        print(message)