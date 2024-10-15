from ydata_profiling import ProfileReport
from src import config
import sweetviz as sv
import matplotlib.pyplot as plt
import klib

def generate_profile_report(data):
    return ProfileReport(data, explorative=True).to_html()

def generate_sweetviz_report(data):
    sv.analyze(data).show_html(config.sweetviz_report_path, open_browser=False)

def generate_klib_report(data):
    save_klib_plot(klib.cat_plot(data),config.klib_cat_plot_path)
    save_klib_plot(klib.dist_plot(data),config.klib_dist_plot_path)
    save_klib_plot(klib.missingval_plot(data),config.klib_missing_val_plot_path)

def save_klib_plot(plot, path):
    plot
    plt.savefig(path)
    plt.close()
