# no imports just built in python functions used.
# 
# Make a script with the target method , test helper and test cases function
# Read all instructions. Twice (comments in this file).
#
# Your question will be different than Icy Hot, with different parameters and requirement.
# IcyHot is a sample.
#
# You can copy the structure of IcyHot
# I will judge on test cases (different test data, testing edge cases, to properly test the requirements)
#
# Its not unittest style, but is single file with solution and data driven unit test cases.
#
# Test cases function calls test helper function repeatedly with different test data and expected value
#
# test helper calls target function and compares actual return with expected
#
# Target function and, unit test cases and test helper
# no imports just built in python functions used. For your problem also do not use 3rd party libraries or any other modules.
# Use simple objects and classes that are built in to Python only.
#
#
class IcyHot:

    def __init__(self):
        self.count = 0
        self.errs = 0

    def main(self):
        self.icy_hot_test_cases()

    # General test helper for data and expected value unit test.
    #
    # Calls the target function with given inputs and verifies that
    # the actual result matches the expected result.
    #
    # Notes:
    # - Parameters before the last one must match the target function's inputs
    #   in both type and order.
    # - The last parameter represents the expected return value.
    # - If the target function signature changes, this helper's signature
    #   must be updated accordingly.
    # - The expected value must be pre-calculated correctly for each test case.
    #
    # Another example of helper unit test method:
    #
    # If the target function is:
    #
    # def round_sum(a, b, c): ...
    #
    # then the helper could be:
    #
    # def test_round_sum(a, b, c, expected): ...
    #
    # Example below assumes target signature:
    #     boolean icyHot(int temp1, int temp2)
    #
    # This function works for this target. But for you, its a sample. The actual number of parameters and parameter types,
    # for your test helper, will depend on the parameters of your target function, their type and return type.
    def test_icy_hot(self, temp1, temp2, expected_return):
        actual_return = False
        self.count += 1

        try:
            actual_return = self.icy_hot(temp1, temp2)
        except Exception as e:
            print("Error", e)

        if actual_return != expected_return:
            print(
                "Actual :" + str(actual_return)
                + ", expected :" + str(expected_return)
                + ", for temp1 :" + str(temp1)
                + ", temp2 :" + str(temp2)
                + ", count :" + str(self.count)
                + "."
            )
            self.errs += 1

    # Different test cases - more the better. To adequately test the target function for all
    # requirements per the question.
    # Number of test cases depends on question and number & type of parameters in target.
    # You need to think of the values. Think of edge cases and make sure question scenarios and other scenarios are covrered.
    # Suggest implement your test helper and test cases functions first and then the target function implemrntation.
    def icy_hot_test_cases(self):
        # besides date here,
        # only use Python built in functions if told too, most problems only need built in functionality

        # copy to your test cases and change text IcyHot ...
        print("IcyHot Test cases")

        test_data = [
            (0, 0, False),
            (0, 101, False),
            (-1, 101, True),
            (500, -101, True),
            (0, 101, False),
            (-100, 1999, True),
        ]

        for temp1, temp2, expected in test_data:
            self.test_icy_hot(temp1, temp2, expected)

        print(
            "IcyHot test cases count "
            + str(self.count)
            + ", Errors (test case expected value wrong or implmentaion wrong or problem understanding wrong):"
            + str(self.errs)
            + "."
        )

    # Target function, this function is the problem function to implement. The signature should be same as
    # in your question.
    #
    #
    # Sample Question:
    # Given two temperatures, return true if one is less than 0 and the other is greater than 100.
    #
    # icyHot(120, -1) -> true
    # icyHot(-1, 120) -> true
    # icyHot(2, 120) -> false
    #
    # For debug can have print here but in reference website need to comment out.
    #
    def icy_hot(self, temp1, temp2):
        if temp1 < 0 and temp2 > 100:
            return True  # sample answer, incomplete, your problem will be different and you should implement compleltely
            # ...here not dont complete so can see sample error message when you run this
        return False


app = IcyHot()
app.main()
