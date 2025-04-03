import os
import subprocess
import time
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo
from plotly.subplots import make_subplots
import plotly.io as pio

project_dir = "/Users/xingwenbo/Desktop/CS383_FinalProject"

def run_and_monitor(command, cwd):
    proc = subprocess.Popen(command, cwd=cwd,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    start_wall = time.time()
    pid, status, rusage = os.wait4(proc.pid, 0)
    end_wall = time.time()
    exec_time = end_wall - start_wall
    cpu_time = rusage.ru_utime + rusage.ru_stime
    stdout_data = proc.stdout.read() or ""
    stderr_data = proc.stderr.read() or ""
    if os.WIFEXITED(status):
        proc.returncode = os.WEXITSTATUS(status)
    elif os.WIFSIGNALED(status):
        proc.returncode = -os.WTERMSIG(status)
    else:
        proc.returncode = status
    return exec_time, cpu_time, stdout_data.strip(), stderr_data.strip()

def run_all_tests():
    data = []
    programs = [
        ("C",      ["./TestC"]),
        ("Java",   ["java", "-cp", ".", "TestJava"]),
        ("Python", ["python3", "TestPython.py"])
    ]
    tasks = ["dijkstra", "fibonacci", "io"]
    for task in tasks:
        for lang, base_cmd in programs:
            print(f"Running {lang} ({task})...")
            cmd = base_cmd + [task]
            exec_time, cpu_time, out, err = run_and_monitor(cmd, cwd=project_dir)
            cpu_percent = (cpu_time / exec_time) * 100 if exec_time > 0 else 0.0
            data.append({
                "Language": lang,
                "Task": task.capitalize() if task != "io" else "IO",
                "Execution Time (s)": round(exec_time, 3),
                "CPU Time (s)": round(cpu_time, 3),
                "Estimated CPU Usage (%)": round(cpu_percent, 2)
            })
    return pd.DataFrame(data)

def plot_results_interactive(df):
    tasks = ["Dijkstra", "Fibonacci", "IO"]

    # Creat 3 chart,
    fig = make_subplots(
        rows=1, cols=3,
        subplot_titles=tasks,
        specs=[[{"secondary_y": True}, {"secondary_y": True}, {"secondary_y": True}]],
        horizontal_spacing=0.1
    )

    for i, task in enumerate(tasks):
        subset = df[df["Task"] == task].sort_values("Language")
        languages = subset["Language"].tolist()

        # left Y, run time 
        fig.add_trace(
            go.Bar(
                x=languages,
                y=subset["Execution Time (s)"],
                name="Execution Time (s)",
                marker_color="skyblue",
                offsetgroup='grp',  #group name 
                hovertemplate="<b>%{x}</b><br>Time: %{y}s"
            ),
            row=1, col=i+1, secondary_y=False
        )

        # right Y：CPU Usage (%)
        fig.add_trace(
            go.Bar(
                x=languages,
                y=subset["Estimated CPU Usage (%)"],
                name="CPU Usage (%)",
                marker_color="orange",
                offsetgroup='grp2',  
                hovertemplate="<b>%{x}</b><br>CPU Usage: %{y}%"
            ),
            row=1, col=i+1, secondary_y=True
        )

        # Title of row
        fig.update_yaxes(title_text="Time (s)", row=1, col=i+1, secondary_y=False)
        fig.update_yaxes(title_text="CPU Usage (%)", row=1, col=i+1, secondary_y=True)

    fig.update_layout(
        title="Performance Comparison by Task",
        barmode="group",  
        height=650,
        width=1450,
        legend=dict(x=0.3, y=-0.15, orientation="h"),
        margin=dict(t=60, b=80)
    )

    # save to static
    pyo.plot(fig, filename="static/chart.html", auto_open=False)
    fig.write_image("static/chart.png")

   

from plotly.subplots import make_subplots

if __name__ == "__main__":
    df = run_all_tests()
    print("\n=== Test Summary ===")
    print(df.to_string(index=False))
    df.to_csv("performance_data.csv", index=False)
    plot_results_interactive(df)
