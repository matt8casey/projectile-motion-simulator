from physics.projectile import Projectile
from ui.input_handler import InputHandler
from ui.display import Display
from ui.graphing import Graphing


def create_projectile_with_drag(velocity, angle):
    projectile_type = InputHandler.get_projectile_type()

    if projectile_type == "custom":
        mass, drag_coefficient, diameter = (
            InputHandler.get_custom_projectile_properties()
        )

        return Projectile(
            velocity,
            angle,
            mass=mass,
            drag_coefficient=drag_coefficient,
            diameter=diameter
        )

    return Projectile(
        velocity,
        angle,
        projectile_type=projectile_type
    )


def run_projectile_calculator():
    Display.show_welcome()

    velocity, angle = InputHandler.get_projectile_inputs()
    motion_type = InputHandler.get_motion_type()

    if motion_type == "ideal":
        projectile = Projectile(velocity, angle)
        Display.show_ideal_results(projectile)

    elif motion_type == "drag":
        projectile = create_projectile_with_drag(
            velocity,
            angle
        )

        Display.show_drag_results(projectile)

    elif motion_type == "comparison":
        projectile = create_projectile_with_drag(
            velocity,
            angle
        )

        Display.show_comparison_results(projectile)

    Graphing.show_projectile_graph(
        projectile,
        show_ideal=True,
        show_drag=projectile.has_drag_properties()
    )


def main():
    try:
        run_projectile_calculator()

    except ValueError as error:
        Display.show_error(error)


if __name__ == "__main__":
    main()