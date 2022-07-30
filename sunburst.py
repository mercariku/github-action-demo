from matplotlib import rcParams, cycler
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px 
import datapane as dp
import pandas as pd
import io, os
from dotenv import load_dotenv

dp.login(token='b7fb94113661f74aa4bbf24e223978b509ff7618')

# Import CSV
qtr_jm = pd.read_csv ("csv/FidelityInternational_JP_FinancialStatement_JudiMarlinski.csv")
qtr_cm = pd.read_csv ("csv/FidelityInternational_JP_FinancialStatement_ChuckMcKenzie.csv")
qtr_dy = pd.read_csv ("csv/FidelityInternational_JP_FinancialStatement_DerekYoung.csv")

fig_jm = px.sunburst(
    qtr_jm,
    path=["JudiMarlinski","Qtr","BS_Section1","BS_Section2","BS_Section3","BS_Section4"],
    values="BS_Price_Ref",
    color="Qtr"
)

fig_cm = px.sunburst(
    qtr_cm,
    path=["ChuckMcKenzie","Qtr","BS_Section1","BS_Section2","BS_Section3","BS_Section4"],
    values="BS_Price_Ref",
    color="Qtr"
)

fig_dy = px.sunburst(
    qtr_dy,
    path=["DerekYoung","Qtr","BS_Section1","BS_Section2","BS_Section3","BS_Section4"],
    values="BS_Price_Ref",
    color="Qtr"
)

report = dp.Report(
    dp.Page(
        dp.Plot(fig_jm),
        title = "Judi Marlinski"),
    dp.Page(
        dp.Plot(fig_cm),
        title = "Chuck McKenzie"
    ), 
    dp.Page(
        dp.Plot(fig_dy),
        title = "Derek Young"
   )
)

report.upload(name="Equity Research Associate: Sunburst", publicly_visible = True)