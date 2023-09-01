import matplotlib.pyplot as plt
from pyrolite.util.classification import TAS
import mplstereonet
import ternary
from matplotlib import rc
from io import BytesIO
import numpy as np

from matplotlib import pyplot as plt
import matplotlib as mpl
from matplotlib import rc
import pandas as pd


def Create_TAS_Plot(uploaded_df):
    uploaded_df["Na2O + K2O"] = uploaded_df["Na2O"] + uploaded_df["K2O"]
    cm = TAS()
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 5))

    cm.add_to_axes(
        ax,
        fill=False,
        which_labels="ID",
        alpha=0.5,
        linewidth=0.5,
        zorder=-1,
        add_labels=True,
    )

    uploaded_df[["SiO2", "Na2O + K2O"]].pyroplot.scatter(
        ax=ax,
        c=uploaded_df["hexcolor"],
        alpha=0.3,
        label=uploaded_df["label"],
        # marker=example_df["marker"],
    )

    # ax.set_title("Example TAS diagram")
    ax.set_ylabel("Na$_2$O + K$_2$O")
    ax.set_xlabel("SiO$_2$")
    ax.legend()

    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    plt.close()

    return buffer


def Create_Stereonet_Plot(uploaded_df):
    strike = uploaded_df["strike"]
    dip = uploaded_df["dip"]
    label = uploaded_df["label"]

    fig, ax = mplstereonet.subplots()

    for str, di, lab in zip(strike, dip, label):
        ax.pole(str, di, c="b", label=f"{lab} {str}/{di}")
    ax.legend()
    ax.grid()

    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    plt.close()

    return buffer


def Create_Plagioclase_Plot(uploaded_df):
    # Extract specific columns
    df_selected = uploaded_df[["An", "Or", "Ab", "marker", "label", "hexcolor", "size"]]

    # Extract individual columns
    marker = df_selected["marker"].values
    label = df_selected["label"].values
    color = df_selected["hexcolor"].values
    size = df_selected["size"].values

    # Set up the figure
    fig, tax = ternary.figure(scale=100)
    fig.set_size_inches(10, 9)

    tax.scatter(
        points=df_selected[["An", "Or", "Ab"]].values,
        marker="s",
        label=label,
        alpha=1,
        s=size,
        color=color,
        zorder=10,
    )

    # Corner labels
    fontsize = 20
    offset = 0.2
    tax.top_corner_label("Or", fontsize=fontsize, offset=offset)
    tax.left_corner_label("Ab", fontsize=fontsize, offset=offset)
    tax.right_corner_label("An", fontsize=fontsize, offset=offset)

    # Decorations
    # tax.legend(loc="center", prop={"size": 12})
    tax.boundary(linewidth=1)
    tax.gridlines(multiple=10, color="gray")
    tax.ticks(axis="lbr", linewidth=1, multiple=10)
    tax.get_axes().axis("off")
    plt.rcParams["font.family"] = "Arial"
    plt.rcParams["axes.axisbelow"] = True
    # plt.rcParams.update({'font.size': 16})

    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    plt.close()

    return buffer


def Create_Pyroxene_Plot(uploaded_df):
    # Extract specific columns
    df_selected = uploaded_df[["Fs", "Wo", "En", "marker", "label", "hexcolor", "size"]]

    # Extract individual columns
    marker = df_selected["marker"].values
    label = df_selected["label"].values
    color = df_selected["hexcolor"].values
    size = df_selected["size"].values

    # Set up the figure
    fig, tax = ternary.figure(scale=100)
    fig.set_size_inches(10, 9)

    tax.scatter(
        points=df_selected[["Fs", "Wo", "En"]].values,
        marker="s",
        label=label,
        alpha=1,
        s=size,
        color=color,
        zorder=10,
    )

    # Draw some lines.
    p1, p2 = (50, 50, 0), (0, 50, 50)
    tax.line(p1, p2, linewidth=1, color="k", alpha=1, linestyle="-")

    p1, p2 = (95, 5, 0), (0, 5, 95)
    tax.line(p1, p2, linewidth=1, color="k", alpha=1, linestyle="-")

    p1, p2 = (55, 45, 0), (0, 45, 55)
    tax.line(p1, p2, linewidth=1, color="k", alpha=1, linestyle="-")

    p1, p2 = (47.5, 5, 47.5), (50, 0, 50)
    tax.line(p1, p2, linewidth=1, color="k", alpha=1, linestyle="-")

    p1, p2 = (25, 50, 25), (27.5, 45, 27.5)
    tax.line(p1, p2, linewidth=1, color="k", alpha=1, linestyle="-")

    p1, p2 = (80, 20, 0), (0, 20, 80)
    tax.line(p1, p2, linewidth=1, color="k", alpha=1, linestyle="-")

    tax.get_axes().text(42.5, 10, "pigeonite", color="k")
    tax.get_axes().text(45, 25, "augite", color="k")

    tax.get_axes().text(10, 1, "enstatite", color="k")
    tax.get_axes().text(80, 1, "ferrosilite", color="k")

    tax.get_axes().text(30, 40, "diopside", color="k", zorder=-1)
    tax.get_axes().text(55, 40, "hedenbergite", color="k")

    # Corner labels.
    fontsize = 20
    offset = 0.2
    tax.top_corner_label("Wo", fontsize=fontsize, offset=offset)
    tax.left_corner_label("En", fontsize=fontsize, offset=offset)
    tax.right_corner_label("Fs", fontsize=fontsize, offset=offset)

    # Decorations.
    # tax.legend(loc="best", prop={"size": 12})
    tax.boundary(linewidth=1)
    tax.gridlines(multiple=10, color="gray")
    tax.ticks(axis="lbr", linewidth=1, multiple=10)
    tax.get_axes().axis("off")
    plt.rcParams["font.family"] = "Arial"
    plt.rcParams["axes.axisbelow"] = True
    plt.rcParams.update({"font.size": 16})

    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    plt.close()

    return buffer


def Spidergram_Normalization(uploaded_df, normalization_reference):
    src_file = r"data\Normalization_values.xlsx"
    normalization_values = pd.read_excel(src_file, sheet_name=normalization_reference)
    normalization_elements = normalization_values.columns

    data = []
    Normalized_uploaded_df = pd.DataFrame(data)

    for col in normalization_elements:
        Normalized_uploaded_df["sample"] = uploaded_df["sample"]
        Normalized_uploaded_df["linestyle"] = uploaded_df["linestyle"]
        Normalized_uploaded_df["hexcolor"] = uploaded_df["hexcolor"]
        Normalized_uploaded_df["linewidth"] = uploaded_df["linewidth"]
        Normalized_uploaded_df[col] = (
            uploaded_df[col] / normalization_values[col].values
        )

    return Normalized_uploaded_df


def Create_Spidergram(Normalized_uploaded_df, normalization_reference):
    fig, ax = plt.subplots(figsize=(16, 8))

    # Iterate through rows of the DataFrame
    for index, row in Normalized_uploaded_df.iterrows():
        sample = row["sample"]
        linestyle = row["linestyle"]
        hexcolor = row["hexcolor"]
        linewidth = row["linewidth"]

        # Extract the data series for this row (use column names for x labels)
        data_series = row[4:]  # Assuming the actual data starts from the 5th column

        ax.tick_params(axis="y", which="both", labelsize=16, width=1, length=5)
        ax.tick_params(axis="x", labelsize=16, width=1, length=5)
        ax.set_yscale("log")
        ax.yaxis.set_major_formatter(mpl.ticker.ScalarFormatter())
        ax.ticklabel_format(style="plain", axis="y", useOffset=False, useMathText=True)

        # Plot the data on the spidergram, using column names as x labels
        plt.plot(
            data_series,
            "-o",
            linestyle=linestyle,
            linewidth=linewidth,
            color=hexcolor,
            label=sample,
        )

    # rc ("font", weight="bold")
    # plt.yticks(weight="bold")
    # plt.xticks(weight="bold", rotation=0)  # Rotate x-axis labels as needed
    plt.ylabel(
        f"Concentration / {normalization_reference}",
        size=16,
        # fontweight="bold",
    )
    plt.grid(False)
    plt.legend()

    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    plt.close()

    return buffer


"""  
   fig, ax = plt.subplots(figsize=(16, 8))
    ax.tick_params(axis="y", which="both", labelsize=16, width=1, length=5)
    ax.tick_params(axis="x", labelsize=16, width=1, length=5)
    ax.set_yscale("log")
    ax.yaxis.set_major_formatter(mpl.ticker.ScalarFormatter())
    # ax.yaxis.set_minor_formatter(mpl.ticker.ScalarFormatter())
    ax.ticklabel_format(style="plain", axis="y", useOffset=False, useMathText=True)

    for samp, ls, color, lab in zip(
        Normalized_uploaded_df["sample"],
        Normalized_uploaded_df["linestyle"],
        Normalized_uploaded_df["hexcolor"],
        Normalized_uploaded_df.columns,
    ):
        x = Normalized_uploaded_df.loc[Normalized_uploaded_df["sample"] == samp]
        x = x.where(pd.notnull(x), None)
        x = x.to_numpy()
        x = np.delete(x, 0)
        plt.plot(lab, x, "-o", linestyle=ls, color=color)

    rc("font", weight="bold")
    plt.yticks(weight="bold")
    plt.xticks(weight="bold")
    plt.xticks(rotation=0)
    plt.ylabel("Concentration/Primitive mantle", size=16, fontweight="bold")
    # plt.legend(fontsize=16)
    plt.grid(False)

    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    plt.close()

    return buffer
 """
