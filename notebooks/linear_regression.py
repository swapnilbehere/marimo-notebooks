import marimo

__generated_with = "0.16.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import panadas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    return np, plt


@app.cell
def _(np):
    diff = np.array([0,1,2,3])
    return (diff,)


@app.cell
def _(diff):
    print(diff)
    return


@app.cell
def _():
    return


@app.cell
def _(np, plt):
    # Generate some data
    x = np.linspace(0, 10, 100) # 100 evenly spaced points between 0 and 10
    y = np.sin(x) # The sine of each x value

    # Create the plot
    plt.plot(x, y)

    # Add labels and a title for clarity (optional but recommended)
    plt.xlabel("X-axis Label")
    plt.ylabel("Y-axis Label")
    plt.title("Simple Sine Wave Plot")

    # Display the plot
    plt.show()
    return


if __name__ == "__main__":
    app.run()
