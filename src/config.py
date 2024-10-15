import os

REPORTS_DIR = 'reports'
os.makedirs(REPORTS_DIR, exist_ok=True)

# Define paths for reports
sweetviz_report_path = os.path.join(REPORTS_DIR, 'sweet_report.html')
klib_cat_plot_path = os.path.join(REPORTS_DIR, 'klib_cat_plot.png')
klib_dist_plot_path = os.path.join(REPORTS_DIR, 'klib_dist_plot.png')
klib_missing_val_plot_path = os.path.join(REPORTS_DIR, 'klib_missing_val_plot.png')