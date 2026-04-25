import sys
import importlib.util

try:
    import customtkinter as ctk
except ImportError:
    ctk = None

class DependencyAuditor(ctk.CTk if ctk else object):
    """
    A professional utility to verify if the 'bs4' package 
    is correctly installed in the current Python path.
    """
    def __init__(self):
        if ctk:
            super().__init__()
            self.title("Aether | Environment Auditor")
            self.geometry("400x250")
            self._build_ui()
        else:
            self.run_cli_audit()

    def _build_ui(self):
        self.label = ctk.CTkLabel(self, text="BS4 Module Status:", font=("Roboto", 16, "bold"))
        self.label.pack(pady=20)

        status, detail = self.check_bs4()
        
        color = "#4BB543" if status == "INSTALLED" else "#CC0000"
        
        self.status_label = ctk.CTkLabel(self, text=status, text_color=color, font=("Roboto", 24, "bold"))
        self.status_label.pack(pady=10)

        self.detail_label = ctk.CTkLabel(self, text=detail, wraplength=350)
        self.detail_label.pack(pady=20)

    def check_bs4(self):
        """Architectural check for package existence without triggering a crash."""
        package_name = 'bs4'
        spec = importlib.util.find_spec(package_name)
        if spec is not None:
            # It exists
            import bs4
            return "INSTALLED", f"Version: {bs4.__version__}\nLocation: {spec.origin}"
        else:
            return "MISSING", "Run 'pip install beautifulsoup4' to resolve."

    def run_cli_audit(self):
        """Fallback for environments without CustomTkinter."""
        status, detail = self.check_bs4()
        print(f"--- ENVIRONMENT AUDIT ---\nSTATUS: {status}\n{detail}")

if __name__ == "__main__":
    # Resilience: Check if we are in a GUI-capable environment
    app = DependencyAuditor()
    if ctk:
        app.mainloop()