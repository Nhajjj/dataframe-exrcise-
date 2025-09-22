{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Nhajjj/dataframe-exrcise-/blob/main/exercises/dataframe_exercise.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "\n",
        "# Sample sales dataset (20 rows)\n",
        "data = {\n",
        "    \"OrderID\": range(1001, 1021),\n",
        "    \"Product\": [\n",
        "        \"Laptop\", \"Mouse\", \"Keyboard\", \"Monitor\", \"Laptop\", \"Headphones\", \"Mouse\", \"Chair\", \"Desk\", \"Laptop\",\n",
        "        \"Printer\", \"Keyboard\", \"Monitor\", \"Mouse\", \"Laptop\", \"Headphones\", \"Desk\", \"Monitor\", \"Printer\", \"Chair\"\n",
        "    ],\n",
        "    \"Category\": [\n",
        "        \"Electronics\", \"Accessories\", \"Accessories\", \"Electronics\", \"Electronics\", \"Accessories\", \"Accessories\",\n",
        "        \"Furniture\", \"Furniture\", \"Electronics\", \"Electronics\", \"Accessories\", \"Electronics\", \"Accessories\",\n",
        "        \"Electronics\", \"Accessories\", \"Furniture\", \"Electronics\", \"Electronics\", \"Furniture\"\n",
        "    ],\n",
        "    \"Quantity\": [2, 5, 3, 4, 1, 6, 10, 2, 1, 3, 2, 4, 2, 7, 5, 3, 2, 4, 1, 6],\n",
        "    \"Price\": [800, 20, 50, 200, 850, 40, 25, 150, 300, 900, 120, 55, 250, 20, 750, 35, 280, 220, 110, 180],\n",
        "    \"Customer\": [\n",
        "        \"Alice\", \"Bob\", \"Charlie\", \"Diana\", \"Ethan\", \"Fiona\", \"George\", \"Hannah\", \"Ian\", \"Jane\",\n",
        "        \"Kyle\", \"Laura\", \"Mike\", \"Nina\", \"Oscar\", \"Paul\", \"Queen\", \"Robert\", \"Sarah\", \"Tom\"\n",
        "    ],\n",
        "    \"Region\": [\n",
        "        \"North\", \"South\", \"East\", \"West\", \"North\", \"South\", \"East\", \"West\", \"North\", \"South\",\n",
        "        \"East\", \"West\", \"North\", \"South\", \"East\", \"West\", \"North\", \"South\", \"East\", \"West\"\n",
        "    ]\n",
        "}\n",
        "\n",
        "df = pd.DataFrame(data)\n",
        "df[\"Total\"] = df[\"Quantity\"] * df[\"Price\"]\n",
        "\n",
        "# Outputs\n",
        "print(df.head())\n",
        "print(\"Shape:\", df.shape)\n",
        "print(\"Columns:\", df.columns.tolist())\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dpLcRsnLKFbf",
        "outputId": "93dff058-45de-4603-9496-1a3b31d188f8"
      },
      "execution_count": 49,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "   OrderID   Product     Category  Quantity  Price Customer Region  Total\n",
            "0     1001    Laptop  Electronics         2    800    Alice  North   1600\n",
            "1     1002     Mouse  Accessories         5     20      Bob  South    100\n",
            "2     1003  Keyboard  Accessories         3     50  Charlie   East    150\n",
            "3     1004   Monitor  Electronics         4    200    Diana   West    800\n",
            "4     1005    Laptop  Electronics         1    850    Ethan  North    850\n",
            "Shape: (20, 8)\n",
            "Columns: ['OrderID', 'Product', 'Category', 'Quantity', 'Price', 'Customer', 'Region', 'Total']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df[\"Discount\"] = df[\"Quantity\"].apply(lambda x: 0.10 if x >= 5 else 0)\n",
        "df[\"FinalTotal\"] = df[\"Total\"] - (df[\"Total\"] * df[\"Discount\"])\n",
        "print(df[[\"OrderID\", \"Product\", \"Total\", \"Discount\", \"FinalTotal\"]].head())\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rc1v5pHTKGvl",
        "outputId": "48ddf67f-3cb1-432b-c09d-4a2ef6850210"
      },
      "execution_count": 50,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "   OrderID   Product  Total  Discount  FinalTotal\n",
            "0     1001    Laptop   1600       0.0      1600.0\n",
            "1     1002     Mouse    100       0.1        90.0\n",
            "2     1003  Keyboard    150       0.0       150.0\n",
            "3     1004   Monitor    800       0.0       800.0\n",
            "4     1005    Laptop    850       0.0       850.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "new_row = {\n",
        "    \"OrderID\": 1021, \"Product\": \"Tablet\", \"Category\": \"Electronics\",\n",
        "    \"Quantity\": 2, \"Price\": 450, \"Customer\": \"Victor\", \"Region\": \"East\"\n",
        "}\n",
        "df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)\n",
        "df[\"Total\"] = df[\"Quantity\"] * df[\"Price\"]\n",
        "print(df.tail(3))\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XmgR_6JBKJQd",
        "outputId": "df8e303c-a0f1-47de-8f5b-efca40dd82a8"
      },
      "execution_count": 51,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "    OrderID  Product     Category  Quantity  Price Customer Region  Total  \\\n",
            "18     1019  Printer  Electronics         1    110    Sarah   East    110   \n",
            "19     1020    Chair    Furniture         6    180      Tom   West   1080   \n",
            "20     1021   Tablet  Electronics         2    450   Victor   East    900   \n",
            "\n",
            "    Discount  FinalTotal  \n",
            "18       0.0       110.0  \n",
            "19       0.1       972.0  \n",
            "20       NaN         NaN  \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.loc[df[\"Product\"] == \"Mouse\", \"Price\"] = 30\n",
        "df[\"Total\"] = df[\"Quantity\"] * df[\"Price\"]\n",
        "print(df[df[\"Product\"] == \"Mouse\"])\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dtxCPxoRKRFV",
        "outputId": "88a372dc-440f-4d09-ef0c-eac5bbe069e0"
      },
      "execution_count": 52,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "    OrderID Product     Category  Quantity  Price Customer Region  Total  \\\n",
            "1      1002   Mouse  Accessories         5     30      Bob  South    150   \n",
            "6      1007   Mouse  Accessories        10     30   George   East    300   \n",
            "13     1014   Mouse  Accessories         7     30     Nina  South    210   \n",
            "\n",
            "    Discount  FinalTotal  \n",
            "1        0.1        90.0  \n",
            "6        0.1       225.0  \n",
            "13       0.1       126.0  \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df = df.drop(columns=[\"Discount\", \"FinalTotal\"])\n",
        "print(df.head())\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VubYThg-KTIJ",
        "outputId": "ed170ee0-1e5d-452d-c274-29b6df0e755d"
      },
      "execution_count": 53,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "   OrderID   Product     Category  Quantity  Price Customer Region  Total\n",
            "0     1001    Laptop  Electronics         2    800    Alice  North   1600\n",
            "1     1002     Mouse  Accessories         5     30      Bob  South    150\n",
            "2     1003  Keyboard  Accessories         3     50  Charlie   East    150\n",
            "3     1004   Monitor  Electronics         4    200    Diana   West    800\n",
            "4     1005    Laptop  Electronics         1    850    Ethan  North    850\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df = df.drop(df[df[\"OrderID\"] == 1010].index)\n",
        "df = df.drop(index=0)\n",
        "print(\"New shape:\", df.shape)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0N_Kh5jHNjx5",
        "outputId": "a7103c50-1ac1-4bff-e969-b2f6d2c4a3b5"
      },
      "execution_count": 54,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "New shape: (19, 8)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "result1 = df[(df[\"Category\"] == \"Electronics\") & (df[\"Quantity\"] >= 3)]\n",
        "print(result1)\n",
        "\n",
        "result2 = df[df[\"Price\"] > 500]\n",
        "print(result2)\n",
        "\n",
        "count_north = df[df[\"Region\"] == \"North\"].shape[0]\n",
        "print(\"North orders:\", count_north)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6EK7jME8N-uI",
        "outputId": "0f61beb3-f9a3-4c74-a572-1ef645139d55"
      },
      "execution_count": 55,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "    OrderID  Product     Category  Quantity  Price Customer Region  Total\n",
            "3      1004  Monitor  Electronics         4    200    Diana   West    800\n",
            "14     1015   Laptop  Electronics         5    750    Oscar   East   3750\n",
            "17     1018  Monitor  Electronics         4    220   Robert  South    880\n",
            "    OrderID Product     Category  Quantity  Price Customer Region  Total\n",
            "4      1005  Laptop  Electronics         1    850    Ethan  North    850\n",
            "14     1015  Laptop  Electronics         5    750    Oscar   East   3750\n",
            "North orders: 4\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "west_sales = df[df[\"Region\"] == \"West\"]\n",
        "print(west_sales)\n",
        "\n",
        "alice_sales = df[df[\"Customer\"] == \"Alice\"]\n",
        "print(alice_sales)\n",
        "\n",
        "subset_sales = df[df[\"Product\"].isin([\"Laptop\", \"Printer\"])]\n",
        "print(subset_sales)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wpPAynKkOQmZ",
        "outputId": "6b5e0571-b51b-4726-9821-a5767b7902c7"
      },
      "execution_count": 56,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "    OrderID     Product     Category  Quantity  Price Customer Region  Total\n",
            "3      1004     Monitor  Electronics         4    200    Diana   West    800\n",
            "7      1008       Chair    Furniture         2    150   Hannah   West    300\n",
            "11     1012    Keyboard  Accessories         4     55    Laura   West    220\n",
            "15     1016  Headphones  Accessories         3     35     Paul   West    105\n",
            "19     1020       Chair    Furniture         6    180      Tom   West   1080\n",
            "Empty DataFrame\n",
            "Columns: [OrderID, Product, Category, Quantity, Price, Customer, Region, Total]\n",
            "Index: []\n",
            "    OrderID  Product     Category  Quantity  Price Customer Region  Total\n",
            "4      1005   Laptop  Electronics         1    850    Ethan  North    850\n",
            "10     1011  Printer  Electronics         2    120     Kyle   East    240\n",
            "14     1015   Laptop  Electronics         5    750    Oscar   East   3750\n",
            "18     1019  Printer  Electronics         1    110    Sarah   East    110\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df[\"Price\"] = df[\"Price\"].astype(float)\n",
        "df.loc[df[\"Category\"] == \"Furniture\", \"Price\"] *= 1.10\n",
        "df[\"Total\"] = df[\"Quantity\"] * df[\"Price\"]\n",
        "print(df[df[\"Category\"] == \"Furniture\"])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SushB133OijV",
        "outputId": "32d70024-2f10-4072-c620-373d7d163cad"
      },
      "execution_count": 58,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "    OrderID Product   Category  Quantity  Price Customer Region   Total\n",
            "7      1008   Chair  Furniture         2  181.5   Hannah   West   363.0\n",
            "8      1009    Desk  Furniture         1  363.0      Ian  North   363.0\n",
            "16     1017    Desk  Furniture         2  338.8    Queen  North   677.6\n",
            "19     1020   Chair  Furniture         6  217.8      Tom   West  1306.8\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sorted_df = df.sort_values(by=\"Total\", ascending=False)\n",
        "print(sorted_df.head())\n",
        "\n",
        "multi_sort = df.sort_values(by=[\"Region\", \"Customer\"])\n",
        "print(multi_sort.head())\n"
      ],
      "metadata": {
        "id": "9Ypak8NEO8cw",
        "outputId": "a72acd38-ea7e-47f2-8d83-787d498519b1",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 59,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "    OrderID  Product     Category  Quantity  Price Customer Region   Total\n",
            "14     1015   Laptop  Electronics         5  750.0    Oscar   East  3750.0\n",
            "19     1020    Chair    Furniture         6  217.8      Tom   West  1306.8\n",
            "20     1021   Tablet  Electronics         2  450.0   Victor   East   900.0\n",
            "17     1018  Monitor  Electronics         4  220.0   Robert  South   880.0\n",
            "4      1005   Laptop  Electronics         1  850.0    Ethan  North   850.0\n",
            "    OrderID   Product     Category  Quantity  Price Customer Region   Total\n",
            "2      1003  Keyboard  Accessories         3   50.0  Charlie   East   150.0\n",
            "6      1007     Mouse  Accessories        10   30.0   George   East   300.0\n",
            "10     1011   Printer  Electronics         2  120.0     Kyle   East   240.0\n",
            "14     1015    Laptop  Electronics         5  750.0    Oscar   East  3750.0\n",
            "18     1019   Printer  Electronics         1  110.0    Sarah   East   110.0\n"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "colab": {
      "name": "Welcome To Colab",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}