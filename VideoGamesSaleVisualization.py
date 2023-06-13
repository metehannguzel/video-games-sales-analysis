import pandas as pd

import plotly.express as px
import plotly.graph_objects as go

total_sales_column = "Total_Sales"

# loading data
vg_sales = pd.read_csv("./dataset.csv")

# 1st released games by year
if "Total_Shipped" in vg_sales.columns:
    vg_sales[total_sales_column] = vg_sales["Total_Shipped"].fillna(0) + vg_sales["Global_Sales"].fillna(0)
else:
    regions = ["NA", "JP", "EU", "Other"]
    region_sales_suffix = "_Sales"

    vg_sales[total_sales_column] = vg_sales["Global_Sales"]

tvg_sales = vg_sales.copy()

# tvg_sales["Year_of_Release"] = vg_sales["Year_of_Release"].fillna(vg_sales["Global_Sales"].mean())
tvg_sales = vg_sales[vg_sales["Year_of_Release"].notna()] # !!!
tvg_sales = tvg_sales.sort_values("Year_of_Release", ascending = True)

figure = px.histogram(
    tvg_sales,
    x = "Platform",
    animation_frame = "Year_of_Release",
    range_y = [0, 550],
)

figure.update_xaxes(type = "category")
figure.update_xaxes(categoryorder = "category ascending")
figure.show()

# 2nd released games by year

top_tvg_sales = tvg_sales.groupby(["Platform", "Year_of_Release"]).agg({total_sales_column: "count"}).reset_index()
top_tvg_sales.columns = ["Platform", "Year_of_Release", "Count"]
top_tvg_sales = top_tvg_sales[top_tvg_sales["Year_of_Release"].isin([2016])]
top_tvg_sales = top_tvg_sales[top_tvg_sales["Count"] > top_tvg_sales["Count"].sum() * 0.01]
top_tvg_sales["Year_of_Release"] = top_tvg_sales["Year_of_Release"].astype(str)

figure = px.bar(
    top_tvg_sales,
    x = "Platform",
    y = "Count",
    color = "Year_of_Release",
    barmode = "group"
)

figure.update_layout(title = "Total released video games by platform")
figure.update_xaxes(type = "category")
figure.update_xaxes(categoryorder = "category ascending")
figure.show()

################################################################################################################################################################

# 1st sales analysis

platform_tvg_sales = tvg_sales.groupby(["Platform", "Year_of_Release"]).agg({total_sales_column: "sum"}).reset_index()
platform_tvg_sales = platform_tvg_sales.sort_values("Year_of_Release", ascending = True)

figure = px.bar(
    platform_tvg_sales,
    x = "Platform",
    y = total_sales_column,
    animation_frame = "Year_of_Release",
    range_y = [0, 150]
)

figure.update_xaxes(type = "category")
figure.update_xaxes(categoryorder = "category ascending")
figure.show()

# 2nd sales analysis

platform_top_tvg_sales = platform_tvg_sales[platform_tvg_sales["Year_of_Release"].isin([2016, 2017, 2018, 2019])]
platform_top_tvg_sales = platform_top_tvg_sales[platform_top_tvg_sales[total_sales_column] > platform_top_tvg_sales[total_sales_column].sum() * 0.005]
platform_top_tvg_sales["Year_of_Release"] = platform_top_tvg_sales["Year_of_Release"].astype(str)

figure = px.bar(
    platform_top_tvg_sales,
    x = "Platform",
    y = total_sales_column,
    color = "Year_of_Release",
    barmode = "group"
)

figure.update_layout(title = "Total sales by platforms (Millions)")
figure.update_xaxes(type = "category")
figure.update_xaxes(categoryorder = "category ascending")
figure.show()

# aggregated sales analysis

platform_sum_tvg_sales = platform_tvg_sales.groupby(["Platform"]).agg({total_sales_column: "sum"}).reset_index()
platform_sum_tvg_sales = platform_sum_tvg_sales[platform_sum_tvg_sales[total_sales_column] > platform_sum_tvg_sales[total_sales_column].sum() * 0.03]

figure = px.bar(
    platform_sum_tvg_sales,
    x = "Platform",
    y = total_sales_column
)

figure.update_layout(title = "Total sales of all time in the most important platforms (Millions)")
figure.update_xaxes(type = "category")
figure.update_xaxes(categoryorder = "category ascending")
figure.show()

# here we can check it: platform_tmp_tvg_sales = tvg_sales.groupby(["Platform", "Year_of_Release"]).agg({total_sales_column: ["sum", "count"]})

################################################################################################################################################################

# sales distribution

if "Total_Shipped" in vg_sales.columns:
    regions = ["NA", "JP", "PAL", "Other"]
else:
    regions = ["NA", "JP", "EU", "Other"]
    
    region_sales_suffix = "_Sales"
    regions_agg = {}
    
for region in regions:
    regions_agg[region + region_sales_suffix] = "sum"
    
regions_agg[total_sales_column] = "sum"
regions_agg

geo_tvg_sales = tvg_sales.groupby(["Year_of_Release"]).agg(regions_agg).reset_index()
geo_tvg_sales = geo_tvg_sales.sort_values("Year_of_Release", ascending = True)

figure = go.Figure()

for region in regions:
    figure.add_trace(go.Scatter(
        x = geo_tvg_sales["Year_of_Release"],
        y = geo_tvg_sales[region + region_sales_suffix],
        mode = "lines",
        name = region
    ))
    
figure.update_layout(title = "Total sales per year by region (Millions)")
figure.update_xaxes(type = "category")
figure.show()

################################################################################################################################################################

# distribution of sales by genre

genre_tvg_sales = tvg_sales.groupby(["Genre"]).agg(regions_agg)
genre_tvg_sales = genre_tvg_sales.sort_values(total_sales_column, ascending = False)

figure = px.imshow(genre_tvg_sales.drop(total_sales_column, 1).T)
figure.update_layout(title = "Sales distribution by genre and region (Millions)")
figure.show()

# 2nd distribution of sales by genre

genre_total_tvg_sales = genre_tvg_sales.reset_index().sort_values(total_sales_column, ascending = False)

figure = go.Figure()

figure.add_trace(go.Scatter(
    x = genre_total_tvg_sales["Genre"],
    y = genre_total_tvg_sales[total_sales_column],
    mode = "lines + markers"
))

figure.update_layout(title = "Total sales by genre (Millions)")
figure.update_xaxes(type = "category")
# figure.update_xaxes(categoryorder = "total descending")
figure.show()
