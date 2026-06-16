import math
import matplotlib.pyplot as plt


class Graphing:
    @staticmethod
    def plot_ideal_trajectory(projectile, points=100):
        results = projectile.get_ideal_results()

        flight_time = results["flight_time"]
        dt = flight_time / points

        x_values = []
        y_values = []

        for i in range(points + 1):
            t = i * dt

            x = projectile.velocity * math.cos(projectile.angle_radians) * t
            y = (
                projectile.velocity
                * math.sin(projectile.angle_radians)
                * t
                - 0.5 * projectile.GRAVITY * t**2
            )

            if y >= 0:
                x_values.append(x)
                y_values.append(y)

        plt.plot(x_values, y_values, label="Ideal Motion")

    @staticmethod
    def plot_drag_trajectory(projectile):
        drag_results = projectile.get_drag_results(dt=0.001)
        trajectory = drag_results["trajectory"]

        x_values = [point[0] for point in trajectory]
        y_values = [point[1] for point in trajectory]

        plt.plot(x_values, y_values, label="Motion With Drag")

    @staticmethod
    def show_projectile_graph(projectile, show_ideal=True, show_drag=False):
        plt.figure()

        if show_ideal:
            Graphing.plot_ideal_trajectory(projectile)

        if show_drag:
            if projectile.has_drag_properties():
                Graphing.plot_drag_trajectory(projectile)
            else:
                print("Cannot graph drag motion without drag properties.")

        plt.title("Projectile Motion")
        plt.xlabel("Horizontal Distance (m)")
        plt.ylabel("Vertical Distance (m)")
        plt.grid(True)
        plt.legend()
        plt.axis("equal")
        plt.show()