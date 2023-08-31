import matplotlib.pyplot as plt
from pyrolite.util.classification import TAS
import mplstereonet
import ternary
from matplotlib import rc
from io import BytesIO


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
