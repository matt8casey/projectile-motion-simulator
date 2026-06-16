import math


class Projectile:
    GRAVITY = 9.81
    AIR_DENSITY = 1.225

    PRESETS = {
        "baseball": {
            "mass": 0.145,
            "drag_coefficient": 0.47,
            "diameter": 0.073
        },
        "golf_ball": {
            "mass": 0.0459,
            "drag_coefficient": 0.24,
            "diameter": 0.0427
        },
        "soccer_ball": {
            "mass": 0.43,
            "drag_coefficient": 0.25,
            "diameter": 0.22
        },
        "tennis_ball": {
            "mass": 0.057,
            "drag_coefficient": 0.55,
            "diameter": 0.067
        }
    }

    def __init__(
        self,
        velocity,
        angle,
        projectile_type=None,
        mass=None,
        drag_coefficient=None,
        diameter=None
    ):
        self.velocity = velocity
        self.angle_degrees = angle
        self.angle_radians = math.radians(angle)

        self.projectile_type = projectile_type

        self.mass = mass
        self.drag_coefficient = drag_coefficient
        self.diameter = diameter

        if projectile_type in self.PRESETS:
            self._load_preset(projectile_type)

        self.area = self._calculate_cross_sectional_area()

    def _load_preset(self, projectile_type):
        preset = self.PRESETS[projectile_type]

        self.mass = preset["mass"]
        self.drag_coefficient = preset["drag_coefficient"]
        self.diameter = preset["diameter"]

    def _calculate_cross_sectional_area(self):
        if self.diameter is None:
            return None

        radius = self.diameter / 2
        return math.pi * radius**2

    def has_drag_properties(self):
        return (
            self.mass is not None
            and self.drag_coefficient is not None
            and self.area is not None
        )

    def calculate_range(self):
        return (
            self.velocity**2
            * math.sin(2 * self.angle_radians)
        ) / self.GRAVITY

    def calculate_max_height(self):
        return (
            self.velocity**2
            * math.sin(self.angle_radians)**2
        ) / (2 * self.GRAVITY)

    def calculate_flight_time(self):
        return (
            2
            * self.velocity
            * math.sin(self.angle_radians)
        ) / self.GRAVITY

    def get_ideal_results(self):
        return {
            "range": self.calculate_range(),
            "max_height": self.calculate_max_height(),
            "flight_time": self.calculate_flight_time()
        }

    def get_drag_results(self, dt=0.01):
        if not self.has_drag_properties():
            raise ValueError(
                "Drag calculations require mass, drag coefficient, and diameter."
            )

        x = 0.0
        y = 0.0
        time = 0.0

        vx = self.velocity * math.cos(self.angle_radians)
        vy = self.velocity * math.sin(self.angle_radians)

        max_height = y
        trajectory = [(x, y)]
        max_speed = math.sqrt(vx**2 + vy**2)

        while y >= 0:
            speed = math.sqrt(vx**2 + vy**2)

            if speed > max_speed:
                max_speed = speed

            elif speed == 0:
                drag_ax = 0
                drag_ay = 0
            else:
                drag_force = (
                    0.5
                    * self.AIR_DENSITY
                    * self.drag_coefficient
                    * self.area
                    * speed**2
                )

                drag_acceleration = drag_force / self.mass

                drag_ax = -drag_acceleration * (vx / speed)
                drag_ay = -drag_acceleration * (vy / speed)

            ax = drag_ax
            ay = -self.GRAVITY + drag_ay

            vx += ax * dt
            vy += ay * dt

            x += vx * dt
            y += vy * dt

            time += dt

            if y > max_height:
                max_height = y

            if y >= 0:
                trajectory.append((x, y))

        return {
            "range": x,
            "max_height": max_height,
            "flight_time": time,
            "terminal_velocity": self.calculate_terminal_velocity(),
            "max_speed_reached": max_speed,
            "trajectory": trajectory
        }

    def get_comparison_results(self):
        ideal = self.get_ideal_results()
        drag = self.get_drag_results()

        range_difference = ideal["range"] - drag["range"]

        if ideal["range"] != 0:
            percent_difference = (
                range_difference / ideal["range"]
            ) * 100
        else:
            percent_difference = 0

        return {
            "ideal": ideal,
            "drag": drag,
            "terminal_velocity": self.calculate_terminal_velocity(),
            "range_difference": range_difference,
            "percent_difference": percent_difference
        }
    
    def calculate_terminal_velocity(self):
        if not self.has_drag_properties():
            return None

        return math.sqrt(
            (
                2
                * self.mass
                * self.GRAVITY
            )
            /
            (
                self.AIR_DENSITY
                * self.drag_coefficient
                * self.area
            )
        )