class Dog:
    def __init__(self, arm_length: float, leg_length: float, num_eyes: int, has_tail: bool, is_furry: bool):
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.num_eyes = num_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry

    def describe(self):
        print("Description of my favorite animal:")
        print(f"Length of the arms: {self.arm_length} feet")
        print(f"Length of the legs: {self.leg_length} feet")
        print(f"Number of eyes: {self.num_eyes}")
        print(f"Does it have a tail?: {'Yes' if self.has_tail else 'No'}")
        print(f"Is it furry: {'Yes' if self.is_furry else 'No'}")

def main():
    my_dog = Dog(arm_length=1.0, leg_length=1.5, num_eyes=2, has_tail=True, is_furry=True)
    my_dog.describe()

if __name__ == "__main__":
    main()