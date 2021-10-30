{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled6.ipynb",
      "provenance": [],
      "mount_file_id": "1FBt4SJeyrpIMlXa8EHh2e-T7LMdyteL2",
      "authorship_tag": "ABX9TyN1dCM/B7LWvOTzUw294xpK",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Skaronite/ml/blob/main/linear-regression.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "sQnP-420JcYL"
      },
      "source": [
        "import pandas as pd \n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "from sklearn import linear_model"
      ],
      "execution_count": 41,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "izOE2glsSvOU",
        "outputId": "a5253aad-e8ce-4025-dff3-4d9b2cc477e8"
      },
      "source": [
        "df = pd.read_csv(\"https://raw.githubusercontent.com/codebasics/py/master/ML/1_linear_reg/Exercise/canada_per_capita_income.csv\")\n",
        "df"
      ],
      "execution_count": 42,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>year</th>\n",
              "      <th>per capita income (US$)</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1970</td>\n",
              "      <td>3399.299037</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1971</td>\n",
              "      <td>3768.297935</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1972</td>\n",
              "      <td>4251.175484</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1973</td>\n",
              "      <td>4804.463248</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>1974</td>\n",
              "      <td>5576.514583</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>1975</td>\n",
              "      <td>5998.144346</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>1976</td>\n",
              "      <td>7062.131392</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>1977</td>\n",
              "      <td>7100.126170</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>1978</td>\n",
              "      <td>7247.967035</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>1979</td>\n",
              "      <td>7602.912681</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>10</th>\n",
              "      <td>1980</td>\n",
              "      <td>8355.968120</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>11</th>\n",
              "      <td>1981</td>\n",
              "      <td>9434.390652</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>12</th>\n",
              "      <td>1982</td>\n",
              "      <td>9619.438377</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>13</th>\n",
              "      <td>1983</td>\n",
              "      <td>10416.536590</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>14</th>\n",
              "      <td>1984</td>\n",
              "      <td>10790.328720</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>15</th>\n",
              "      <td>1985</td>\n",
              "      <td>11018.955850</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>16</th>\n",
              "      <td>1986</td>\n",
              "      <td>11482.891530</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>17</th>\n",
              "      <td>1987</td>\n",
              "      <td>12974.806620</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>18</th>\n",
              "      <td>1988</td>\n",
              "      <td>15080.283450</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>19</th>\n",
              "      <td>1989</td>\n",
              "      <td>16426.725480</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>20</th>\n",
              "      <td>1990</td>\n",
              "      <td>16838.673200</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>21</th>\n",
              "      <td>1991</td>\n",
              "      <td>17266.097690</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>22</th>\n",
              "      <td>1992</td>\n",
              "      <td>16412.083090</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>23</th>\n",
              "      <td>1993</td>\n",
              "      <td>15875.586730</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>24</th>\n",
              "      <td>1994</td>\n",
              "      <td>15755.820270</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25</th>\n",
              "      <td>1995</td>\n",
              "      <td>16369.317250</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>26</th>\n",
              "      <td>1996</td>\n",
              "      <td>16699.826680</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>27</th>\n",
              "      <td>1997</td>\n",
              "      <td>17310.757750</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>28</th>\n",
              "      <td>1998</td>\n",
              "      <td>16622.671870</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>29</th>\n",
              "      <td>1999</td>\n",
              "      <td>17581.024140</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>30</th>\n",
              "      <td>2000</td>\n",
              "      <td>18987.382410</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>31</th>\n",
              "      <td>2001</td>\n",
              "      <td>18601.397240</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>32</th>\n",
              "      <td>2002</td>\n",
              "      <td>19232.175560</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>33</th>\n",
              "      <td>2003</td>\n",
              "      <td>22739.426280</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>34</th>\n",
              "      <td>2004</td>\n",
              "      <td>25719.147150</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>35</th>\n",
              "      <td>2005</td>\n",
              "      <td>29198.055690</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>36</th>\n",
              "      <td>2006</td>\n",
              "      <td>32738.262900</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>37</th>\n",
              "      <td>2007</td>\n",
              "      <td>36144.481220</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>38</th>\n",
              "      <td>2008</td>\n",
              "      <td>37446.486090</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>39</th>\n",
              "      <td>2009</td>\n",
              "      <td>32755.176820</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>40</th>\n",
              "      <td>2010</td>\n",
              "      <td>38420.522890</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>41</th>\n",
              "      <td>2011</td>\n",
              "      <td>42334.711210</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>42</th>\n",
              "      <td>2012</td>\n",
              "      <td>42665.255970</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>43</th>\n",
              "      <td>2013</td>\n",
              "      <td>42676.468370</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>44</th>\n",
              "      <td>2014</td>\n",
              "      <td>41039.893600</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>45</th>\n",
              "      <td>2015</td>\n",
              "      <td>35175.188980</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>46</th>\n",
              "      <td>2016</td>\n",
              "      <td>34229.193630</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "    year  per capita income (US$)\n",
              "0   1970              3399.299037\n",
              "1   1971              3768.297935\n",
              "2   1972              4251.175484\n",
              "3   1973              4804.463248\n",
              "4   1974              5576.514583\n",
              "5   1975              5998.144346\n",
              "6   1976              7062.131392\n",
              "7   1977              7100.126170\n",
              "8   1978              7247.967035\n",
              "9   1979              7602.912681\n",
              "10  1980              8355.968120\n",
              "11  1981              9434.390652\n",
              "12  1982              9619.438377\n",
              "13  1983             10416.536590\n",
              "14  1984             10790.328720\n",
              "15  1985             11018.955850\n",
              "16  1986             11482.891530\n",
              "17  1987             12974.806620\n",
              "18  1988             15080.283450\n",
              "19  1989             16426.725480\n",
              "20  1990             16838.673200\n",
              "21  1991             17266.097690\n",
              "22  1992             16412.083090\n",
              "23  1993             15875.586730\n",
              "24  1994             15755.820270\n",
              "25  1995             16369.317250\n",
              "26  1996             16699.826680\n",
              "27  1997             17310.757750\n",
              "28  1998             16622.671870\n",
              "29  1999             17581.024140\n",
              "30  2000             18987.382410\n",
              "31  2001             18601.397240\n",
              "32  2002             19232.175560\n",
              "33  2003             22739.426280\n",
              "34  2004             25719.147150\n",
              "35  2005             29198.055690\n",
              "36  2006             32738.262900\n",
              "37  2007             36144.481220\n",
              "38  2008             37446.486090\n",
              "39  2009             32755.176820\n",
              "40  2010             38420.522890\n",
              "41  2011             42334.711210\n",
              "42  2012             42665.255970\n",
              "43  2013             42676.468370\n",
              "44  2014             41039.893600\n",
              "45  2015             35175.188980\n",
              "46  2016             34229.193630"
            ]
          },
          "metadata": {},
          "execution_count": 42
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 296
        },
        "id": "wCZXu_qPUC6I",
        "outputId": "bfc4b245-0bb6-415a-93c0-fb514f355ad0"
      },
      "source": [
        "%matplotlib inline\n",
        "plt.xlabel(\"year\")\n",
        "plt.ylabel(\"per capita income (US$)\")\n",
        "plt.scatter(df.year,df['per capita income (US$)'], color='red',marker='+')"
      ],
      "execution_count": 43,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.collections.PathCollection at 0x7f83b8aa0f10>"
            ]
          },
          "metadata": {},
          "execution_count": 43
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XjX7pglmfILL",
        "outputId": "683d2e1f-b86e-4b78-9337-19b546b8c573"
      },
      "source": [
        "reg = linear_model.LinearRegression()\n",
        "reg.fit(df[['year']],df[['per capita income (US$)']])"
      ],
      "execution_count": 45,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)"
            ]
          },
          "metadata": {},
          "execution_count": 45
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ffwegFYuftPW",
        "outputId": "6f31ee62-16ac-4e38-978a-8eeedb7303ee"
      },
      "source": [
        "reg.predict([[2020]])"
      ],
      "execution_count": 46,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[41288.69409442]])"
            ]
          },
          "metadata": {},
          "execution_count": 46
        }
      ]
    }
  ]
}