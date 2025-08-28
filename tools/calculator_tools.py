from crewai.tools import BaseTool

class CalculatorTool(BaseTool):
    def __init__(self):
        super().__init__(
            name="Calculator",
            description="Performs basic math calculations. Input should be a valid mathematical expression."
        )

    def _run(self, input: str) -> str:
        try:
            return str(eval(input))
        except Exception:
            return "Error: Invalid syntax in mathematical expression"