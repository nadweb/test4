import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from Function.Function_def import *
import datetime


# ====================== Custom Styles & Colors ======================
class ColorScheme:
    # Modern color palette
    PRIMARY = "#1E3A5F"  # Dark blue
    SECONDARY = "#4A90E2"  # Bright blue
    SUCCESS = "#52C41A"  # Green
    WARNING = "#FA8C16"  # Orange
    ERROR = "#F5222D"  # Red

    BG_DARK = "#001529"  # Very dark blue
    BG_MAIN = "#F0F2F5"  # Light gray background
    BG_CARD = "#FFFFFF"  # White cards

    TEXT_PRIMARY = "#262626"  # Dark text
    TEXT_SECONDARY = "#8C8C8C"  # Gray text
    TEXT_WHITE = "#FFFFFF"  # White text

    BORDER = "#D9D9D9"  # Light border
    SHADOW = "#00000019"  # Shadow color


def setup_modern_styles():
    style = ttk.Style()
    style.theme_use('clam')

    # Configure modern button styles
    style.configure("Primary.TButton",
                    font=("Segoe UI", 10, "bold"),
                    borderwidth=0,
                    relief="flat",
                    padding=(15, 10))

    style.map("Primary.TButton",
              background=[('active', ColorScheme.SECONDARY),
                          ('!active', ColorScheme.PRIMARY)],
              foreground=[('active', 'white'), ('!active', 'white')])

    style.configure("Success.TButton",
                    font=("Segoe UI", 10),
                    borderwidth=0,
                    relief="flat",
                    padding=(12, 8))

    style.map("Success.TButton",
              background=[('active', '#73D13D'),
                          ('!active', ColorScheme.SUCCESS)],
              foreground=[('active', 'white'), ('!active', 'white')])

    # Configure combobox style
    style.configure("Modern.TCombobox",
                    fieldbackground="white",
                    borderwidth=1,
                    relief="solid")


# ====================== Custom Widgets ======================
class ModernCard(tk.Frame):
    def __init__(self, parent, title="", icon="", **kwargs):
        super().__init__(parent, bg=ColorScheme.BG_CARD, relief="flat", **kwargs)

        # Add subtle border
        self.configure(highlightbackground=ColorScheme.BORDER,
                       highlightthickness=1)

        if title:
            header = tk.Frame(self, bg=ColorScheme.BG_CARD, height=50)
            header.pack(fill="x", padx=20, pady=(15, 10))

            # Icon and title
            title_label = tk.Label(header,
                                   text=f"{icon}  {title}" if icon else title,
                                   font=("Segoe UI", 13, "bold"),
                                   bg=ColorScheme.BG_CARD,
                                   fg=ColorScheme.TEXT_PRIMARY)
            title_label.pack(side="left")


class StatCard(tk.Frame):
    def __init__(self, parent, title, value, subtitle="", color=ColorScheme.PRIMARY, **kwargs):
        super().__init__(parent, bg=ColorScheme.BG_CARD, relief="flat", **kwargs)

        self.configure(highlightbackground=ColorScheme.BORDER,
                       highlightthickness=1)

        # Content
        content = tk.Frame(self, bg=ColorScheme.BG_CARD)
        content.pack(fill="both", expand=True, padx=15, pady=15)

        # Title
        tk.Label(content,
                 text=title,
                 font=("Segoe UI", 9),
                 bg=ColorScheme.BG_CARD,
                 fg=ColorScheme.TEXT_SECONDARY).pack(anchor="w")

        # Value with color accent
        value_frame = tk.Frame(content, bg=ColorScheme.BG_CARD)
        value_frame.pack(anchor="w", pady=(5, 0))

        # Color indicator
        indicator = tk.Frame(value_frame, bg=color, width=4, height=30)
        indicator.pack(side="left", padx=(0, 10))

        tk.Label(value_frame,
                 text=value,
                 font=("Segoe UI", 20, "bold"),
                 bg=ColorScheme.BG_CARD,
                 fg=ColorScheme.TEXT_PRIMARY).pack(side="left")

        if subtitle:
            tk.Label(content,
                     text=subtitle,
                     font=("Segoe UI", 8),
                     bg=ColorScheme.BG_CARD,
                     fg=ColorScheme.TEXT_SECONDARY).pack(anchor="w", pady=(2, 0))


# ====================== Main Application ======================
class ModernDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("📊 Hệ Thống Phân Tích & Trực Quan Hóa Dữ Liệu")
        self.root.geometry("1400x900")
        self.root.configure(bg=ColorScheme.BG_MAIN)

        # Setup styles
        setup_modern_styles()

        # Create main layout
        self.create_layout()

    def create_layout(self):
        # Top Navigation Bar
        self.create_navbar()

        # Main Container
        main_container = tk.Frame(self.root, bg=ColorScheme.BG_MAIN)
        main_container.pack(fill="both", expand=True)

        # Left Sidebar
        self.create_sidebar(main_container)

        # Main Content Area
        content_area = tk.Frame(main_container, bg=ColorScheme.BG_MAIN)
        content_area.pack(side="left", fill="both", expand=True, padx=(0, 20), pady=20)

        # Dashboard Header with Stats
        self.create_dashboard_header(content_area)

        # Main Work Area
        work_area = tk.Frame(content_area, bg=ColorScheme.BG_MAIN)
        work_area.pack(fill="both", expand=True, pady=(20, 0))

        # Create tabbed interface
        self.create_tabbed_interface(work_area)

    def create_navbar(self):
        """Create top navigation bar"""
        navbar = tk.Frame(self.root, bg=ColorScheme.PRIMARY, height=60)
        navbar.pack(fill="x")
        navbar.pack_propagate(False)

        # App title
        title_frame = tk.Frame(navbar, bg=ColorScheme.PRIMARY)
        title_frame.pack(side="left", padx=20, fill="y")

        tk.Label(title_frame,
                 text="📊 PHÂN TÍCH DỮ LIỆU",
                 font=("Segoe UI", 16, "bold"),
                 bg=ColorScheme.PRIMARY,
                 fg=ColorScheme.TEXT_WHITE).pack(expand=True)

        # Right side info
        info_frame = tk.Frame(navbar, bg=ColorScheme.PRIMARY)
        info_frame.pack(side="right", padx=20, fill="y")

        # Date/Time
        current_date = datetime.datetime.now().strftime("%d/%m/%Y - %H:%M")
        tk.Label(info_frame,
                 text=f"🕐 {current_date}",
                 font=("Segoe UI", 10),
                 bg=ColorScheme.PRIMARY,
                 fg=ColorScheme.TEXT_WHITE).pack(side="right", expand=True)

    def create_sidebar(self, parent):
        """Create left sidebar with navigation"""
        sidebar = tk.Frame(parent, bg=ColorScheme.BG_DARK, width=250)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        # Menu items
        menu_items = [
            ("🏠", "Tổng quan", True),
            ("📁", "Quản lý Dữ liệu", False),
            ("📊", "Biểu đồ", False),
            ("🔍", "Truy vấn SQL", False),
            ("🤖", "Dự báo AI", False),
            ("📈", "Báo cáo", False),
            ("⚙️", "Cài đặt", False),
        ]

        for icon, text, active in menu_items:
            self.create_menu_item(sidebar, icon, text, active)

    def create_menu_item(self, parent, icon, text, active=False):
        """Create a sidebar menu item"""
        bg = ColorScheme.PRIMARY if active else ColorScheme.BG_DARK
        fg = ColorScheme.TEXT_WHITE

        item = tk.Frame(parent, bg=bg, height=45)
        item.pack(fill="x", pady=1)
        item.pack_propagate(False)

        # Add hover effect
        def on_enter(e):
            if not active:
                item.configure(bg="#1A2B3D")

        def on_leave(e):
            if not active:
                item.configure(bg=ColorScheme.BG_DARK)

        item.bind("<Enter>", on_enter)
        item.bind("<Leave>", on_leave)

        # Content
        content = tk.Frame(item, bg=bg)
        content.pack(expand=True)

        label = tk.Label(content,
                         text=f"{icon}  {text}",
                         font=("Segoe UI", 11),
                         bg=bg,
                         fg=fg)
        label.pack(side="left", padx=20)

        # Active indicator
        if active:
            indicator = tk.Frame(item, bg=ColorScheme.SUCCESS, width=4)
            indicator.place(x=0, y=0, relheight=1)

    def create_dashboard_header(self, parent):
        """Create dashboard header with statistics cards"""
        header_frame = tk.Frame(parent, bg=ColorScheme.BG_MAIN)
        header_frame.pack(fill="x")

        # Title
        tk.Label(header_frame,
                 text="Bảng Điều Khiển",
                 font=("Segoe UI", 18, "bold"),
                 bg=ColorScheme.BG_MAIN,
                 fg=ColorScheme.TEXT_PRIMARY).pack(anchor="w", pady=(0, 15))

        # Stats cards
        stats_frame = tk.Frame(header_frame, bg=ColorScheme.BG_MAIN)
        stats_frame.pack(fill="x")

        # Create stat cards
        stats = [
            ("Tổng Dữ Liệu", "15,234", "Bản ghi", ColorScheme.PRIMARY),
            ("Đã Xử Lý", "12,890", "↑ 12.5%", ColorScheme.SUCCESS),
            ("Đang Chờ", "2,344", "Cần xử lý", ColorScheme.WARNING),
            ("Báo Cáo", "48", "Tháng này", ColorScheme.SECONDARY),
        ]

        for title, value, subtitle, color in stats:
            card = StatCard(stats_frame, title, value, subtitle, color)
            card.pack(side="left", fill="both", expand=True, padx=(0, 15))

    def create_tabbed_interface(self, parent):
        """Create main tabbed interface"""
        # Create notebook for tabs
        notebook = ttk.Notebook(parent)
        notebook.pack(fill="both", expand=True)

        # Tab 1: Data Import
        self.create_data_import_tab(notebook)

        # Tab 2: Visualization
        self.create_visualization_tab(notebook)

        # Tab 3: SQL Query
        self.create_sql_tab(notebook)

        # Tab 4: AI Prediction
        self.create_prediction_tab(notebook)

    def create_data_import_tab(self, notebook):
        """Create data import tab"""
        tab = tk.Frame(notebook, bg=ColorScheme.BG_MAIN)
        notebook.add(tab, text="   📥 Nhập Dữ Liệu   ")

        # Database section
        db_card = ModernCard(tab, "Cấu Hình Cơ Sở Dữ Liệu", "🗄️")
        db_card.pack(fill="x", padx=20, pady=(20, 10))

        db_content = tk.Frame(db_card, bg=ColorScheme.BG_CARD)
        db_content.pack(fill="x", padx=20, pady=(0, 20))

        # Database path
        db_row1 = tk.Frame(db_content, bg=ColorScheme.BG_CARD)
        db_row1.pack(fill="x", pady=5)

        tk.Label(db_row1,
                 text="Đường dẫn CSDL:",
                 font=("Segoe UI", 10),
                 bg=ColorScheme.BG_CARD,
                 fg=ColorScheme.TEXT_PRIMARY,
                 width=15,
                 anchor="w").pack(side="left")

        self.entry_database = tk.Entry(db_row1,
                                       font=("Segoe UI", 10),
                                       relief="solid",
                                       bd=1)
        self.entry_database.pack(side="left", fill="x", expand=True, padx=(0, 10))

        ttk.Button(db_row1,
                   text="📂 Chọn",
                   command=lambda: Choose_database(self.entry_database)).pack(side="left", padx=2)

        ttk.Button(db_row1,
                   text="➕ Tạo mới",
                   style="Success.TButton",
                   command=lambda: Create_database(self.entry_database)).pack(side="left", padx=2)

        # Table name
        db_row2 = tk.Frame(db_content, bg=ColorScheme.BG_CARD)
        db_row2.pack(fill="x", pady=5)

        tk.Label(db_row2,
                 text="Tên bảng:",
                 font=("Segoe UI", 10),
                 bg=ColorScheme.BG_CARD,
                 fg=ColorScheme.TEXT_PRIMARY,
                 width=15,
                 anchor="w").pack(side="left")

        self.entry_table = tk.Entry(db_row2,
                                    font=("Segoe UI", 10),
                                    relief="solid",
                                    bd=1,
                                    width=30)
        self.entry_table.pack(side="left")

        # File import section
        file_card = ModernCard(tab, "Nhập Liệu Từ File", "📁")
        file_card.pack(fill="x", padx=20, pady=10)

        file_content = tk.Frame(file_card, bg=ColorScheme.BG_CARD)
        file_content.pack(fill="x", padx=20, pady=(0, 20))

        file_row = tk.Frame(file_content, bg=ColorScheme.BG_CARD)
        file_row.pack(fill="x")

        tk.Label(file_row,
                 text="File dữ liệu:",
                 font=("Segoe UI", 10),
                 bg=ColorScheme.BG_CARD,
                 fg=ColorScheme.TEXT_PRIMARY,
                 width=15,
                 anchor="nw").pack(side="left")

        # Text widget for files
        text_frame = tk.Frame(file_row, relief="solid", bd=1, bg="white")
        text_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))

        self.text_widget = tk.Text(text_frame,
                                   font=("Consolas", 10),
                                   height=4,
                                   wrap="none",
                                   relief="flat",
                                   bg="white")
        self.text_widget.pack(side="left", fill="both", expand=True)

        self.scroll = tk.Scrollbar(text_frame, orient="vertical", command=self.text_widget.yview)
        self.text_widget.config(yscrollcommand=self.scroll.set)

        btn_frame = tk.Frame(file_row, bg=ColorScheme.BG_CARD)
        btn_frame.pack(side="left")

        ttk.Button(btn_frame,
                   text="📂 Chọn file",
                   command=lambda: Choose_data(self.text_widget, self.scroll)).pack(pady=2)

        ttk.Button(btn_frame,
                   text="⬆️ Tải lên",
                   style="Primary.TButton",
                   command=lambda: Load_data(
                       self.entry_database, self.entry_table, self.text_widget,
                       self.tree, self.combo_x, self.combo_y
                   )).pack(pady=2)

        # Data preview
        preview_card = ModernCard(tab, "Xem Trước Dữ Liệu", "👁️")
        preview_card.pack(fill="both", expand=True, padx=20, pady=10)

        tree_frame = tk.Frame(preview_card, bg=ColorScheme.BG_CARD)
        tree_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        # Create Treeview
        self.tree = ttk.Treeview(tree_frame)
        self.tree.pack(side="left", fill="both", expand=True)

        tree_scroll = tk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        tree_scroll.pack(side="right", fill="y")
        self.tree.config(yscrollcommand=tree_scroll.set)

    def create_visualization_tab(self, notebook):
        """Create visualization tab"""
        tab = tk.Frame(notebook, bg=ColorScheme.BG_MAIN)
        notebook.add(tab, text="   📊 Trực Quan Hóa   ")

        # Chart configuration
        config_card = ModernCard(tab, "Cấu Hình Biểu Đồ", "⚙️")
        config_card.pack(fill="x", padx=20, pady=(20, 10))

        config_content = tk.Frame(config_card, bg=ColorScheme.BG_CARD)
        config_content.pack(fill="x", padx=20, pady=(0, 20))

        # Chart type row
        row1 = tk.Frame(config_content, bg=ColorScheme.BG_CARD)
        row1.pack(fill="x", pady=5)

        tk.Label(row1,
                 text="Loại biểu đồ:",
                 font=("Segoe UI", 10),
                 bg=ColorScheme.BG_CARD,
                 width=12,
                 anchor="w").pack(side="left", padx=(0, 10))

        self.combo_chart = ttk.Combobox(row1,
                                        values=["Cột", "Tròn", "Đường", "Phân tán", "Khu vực"],
                                        font=("Segoe UI", 10),
                                        state="readonly",
                                        width=15)
        self.combo_chart.pack(side="left", padx=5)
        self.combo_chart.set("Cột")

        tk.Label(row1,
                 text="Trục X:",
                 font=("Segoe UI", 10),
                 bg=ColorScheme.BG_CARD,
                 width=8,
                 anchor="e").pack(side="left", padx=(20, 5))

        self.combo_x = ttk.Combobox(row1,
                                    values=[],
                                    font=("Segoe UI", 10),
                                    state="readonly",
                                    width=15)
        self.combo_x.pack(side="left", padx=5)

        tk.Label(row1,
                 text="Trục Y:",
                 font=("Segoe UI", 10),
                 bg=ColorScheme.BG_CARD,
                 width=8,
                 anchor="e").pack(side="left", padx=(20, 5))

        self.combo_y = ttk.Combobox(row1,
                                    values=[],
                                    font=("Segoe UI", 10),
                                    state="readonly",
                                    width=15)
        self.combo_y.pack(side="left", padx=5)

        # Buttons
        ttk.Button(row1,
                   text="📊 Vẽ biểu đồ",
                   style="Primary.TButton",
                   command=lambda: Draw_chart(
                       self.combo_chart, self.combo_x, self.combo_y, self.frame_chart
                   )).pack(side="left", padx=(20, 5))

        ttk.Button(row1,
                   text="💾 Lưu",
                   style="Success.TButton",
                   command=Save_chart).pack(side="left", padx=5)

        # Chart display
        chart_card = ModernCard(tab, "Biểu Đồ", "📈")
        chart_card.pack(fill="both", expand=True, padx=20, pady=10)

        self.frame_chart = tk.Frame(chart_card, bg=ColorScheme.BG_CARD)
        self.frame_chart.pack(fill="both", expand=True, padx=20, pady=(0, 20))

    def create_sql_tab(self, notebook):
        """Create SQL query tab"""
        tab = tk.Frame(notebook, bg=ColorScheme.BG_MAIN)
        notebook.add(tab, text="   🔍 Truy Vấn SQL   ")

        # SQL Editor
        editor_card = ModernCard(tab, "Trình Soạn Thảo SQL", "✏️")
        editor_card.pack(fill="x", padx=20, pady=(20, 10))

        editor_content = tk.Frame(editor_card, bg=ColorScheme.BG_CARD)
        editor_content.pack(fill="x", padx=20, pady=(0, 20))

        # SQL text area
        sql_frame = tk.Frame(editor_content, relief="solid", bd=1, bg="#2B2B2B")
        sql_frame.pack(fill="x")

        self.sql_text = tk.Text(sql_frame,
                                font=("Consolas", 11),
                                height=8,
                                bg="#2B2B2B",
                                fg="#F0F0F0",
                                insertbackground="white",
                                relief="flat")
        self.sql_text.pack(side="left", fill="both", expand=True)

        sql_scroll = tk.Scrollbar(sql_frame, orient="vertical", command=self.sql_text.yview)
        sql_scroll.pack(side="right", fill="y")
        self.sql_text.config(yscrollcommand=sql_scroll.set)

        # Sample query
        self.sql_text.insert("1.0",
                             "-- Ví dụ truy vấn\nSELECT * FROM ten_bang\nWHERE dieu_kien = 'gia_tri'\nORDER BY cot DESC\nLIMIT 100;")

        # Execute button
        ttk.Button(editor_content,
                   text="▶️ Thực thi",
                   style="Primary.TButton",
                   command=lambda: Excute_sql(
                       self.entry_database, self.sql_text, self.tree,
                       self.combo_x, self.combo_y
                   )).pack(anchor="e", pady=(10, 0))

        # Results
        results_card = ModernCard(tab, "Kết Quả Truy Vấn", "📋")
        results_card.pack(fill="both", expand=True, padx=20, pady=10)

    def create_prediction_tab(self, notebook):
        """Create AI prediction tab"""
        tab = tk.Frame(notebook, bg=ColorScheme.BG_MAIN)
        notebook.add(tab, text="   🤖 Dự Báo AI   ")

        # Model configuration
        model_card = ModernCard(tab, "Cấu Hình Mô Hình Dự Báo", "🎯")
        model_card.pack(fill="x", padx=20, pady=(20, 10))

        model_content = tk.Frame(model_card, bg=ColorScheme.BG_CARD)
        model_content.pack(fill="x", padx=20, pady=(0, 20))

        # Model selection row
        model_row = tk.Frame(model_content, bg=ColorScheme.BG_CARD)
        model_row.pack(fill="x", pady=10)

        tk.Label(model_row,
                 text="Mô hình:",
                 font=("Segoe UI", 11),
                 bg=ColorScheme.BG_CARD,
                 fg=ColorScheme.TEXT_PRIMARY).pack(side="left", padx=(0, 10))

        self.combo_model = ttk.Combobox(model_row,
                                        values=["Hồi quy tuyến tính", "Random Forest",
                                                "XGBoost", "Mạng Neural", "ARIMA", "Prophet"],
                                        font=("Segoe UI", 10),
                                        state="readonly",
                                        width=25)
        self.combo_model.pack(side="left", padx=5)
        self.combo_model.set("Hồi quy tuyến tính")

        tk.Label(model_row,
                 text="Năm dự báo:",
                 font=("Segoe UI", 11),
                 bg=ColorScheme.BG_CARD,
                 fg=ColorScheme.TEXT_PRIMARY).pack(side="left", padx=(30, 10))

        self.entry_year = tk.Entry(model_row,
                                   font=("Segoe UI", 10),
                                   width=10,
                                   relief="solid",
                                   bd=1)
        self.entry_year.pack(side="left", padx=5)
        self.entry_year.insert(0, "2025")

        ttk.Button(model_row,
                   text="🎯 Dự báo",
                   style="Primary.TButton",
                   command=clone).pack(side="left", padx=(30, 0))

        # Additional parameters
        params_frame = tk.Frame(model_content, bg=ColorScheme.BG_CARD)
        params_frame.pack(fill="x", pady=10)

        tk.Label(params_frame,
                 text="Tham số bổ sung:",
                 font=("Segoe UI", 10),
                 bg=ColorScheme.BG_CARD,
                 fg=ColorScheme.TEXT_SECONDARY).pack(anchor="w")

        params_row = tk.Frame(params_frame, bg=ColorScheme.BG_CARD)
        params_row.pack(fill="x", pady=5)

        # Confidence interval
        tk.Label(params_row,
                 text="Độ tin cậy:",
                 font=("Segoe UI", 10),
                 bg=ColorScheme.BG_CARD).pack(side="left", padx=(20, 5))

        confidence = ttk.Combobox(params_row,
                                  values=["90%", "95%", "99%"],
                                  font=("Segoe UI", 10),
                                  state="readonly",
                                  width=10)
        confidence.pack(side="left", padx=5)
        confidence.set("95%")

        # Test size
        tk.Label(params_row,
                 text="Tỷ lệ kiểm thử:",
                 font=("Segoe UI", 10),
                 bg=ColorScheme.BG_CARD).pack(side="left", padx=(20, 5))

        test_size = ttk.Combobox(params_row,
                                 values=["20%", "25%", "30%"],
                                 font=("Segoe UI", 10),
                                 state="readonly",
                                 width=10)
        test_size.pack(side="left", padx=5)
        test_size.set("20%")

        # Results visualization
        results_card = ModernCard(tab, "Kết Quả Dự Báo", "📊")
        results_card.pack(fill="both", expand=True, padx=20, pady=10)

        # Info panel
        info_panel = tk.Frame(results_card, bg="#E6F7FF", relief="solid", bd=1)
        info_panel.pack(fill="x", padx=20, pady=(0, 20))

        tk.Label(info_panel,
                 text="ℹ️ Chọn mô hình phù hợp với dữ liệu của bạn và nhập năm cần dự báo.",
                 font=("Segoe UI", 10),
                 bg="#E6F7FF",
                 fg=ColorScheme.PRIMARY,
                 wraplength=800).pack(padx=15, pady=10)


# ====================== Main Execution ======================
if __name__ == "__main__":
    root = tk.Tk()
    app = ModernDashboard(root)
    root.mainloop()