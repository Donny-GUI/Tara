from typing import Self
import tokenize
import tkinter as tk
from tkinter import Menu, messagebox, filedialog, simpledialog
import keyword
import re
from tkinter import ttk
import builtins
from typing import Optional, Tuple, Union
import customtkinter as ctk
from pyautogui import size
from io import BytesIO
import importlib
import pkgutil
DimGrayRGB = (51, 51, 51)
DimGrayHTML = '#333333'
DimGrayName = 'dimgray'
keywords0 = ['from', 'import', 'True', 'False', 'as', 'None']
keywords1 = [x for x in keyword.kwlist if x not in keywords0]
html_colors = {'aliceblue': '#F0F8FF', 'antiquewhite': '#FAEBD7', 'aqua': '#00FFFF', 'aquamarine': '#7FFFD4', 'azure': '#F0FFFF', 'beige': '#F5F5DC', 'bisque': '#FFE4C4', 'black': '#000000', 'blanchedalmond': '#FFEBCD', 'blue': '#0000FF', 'blueviolet': '#8A2BE2', 'brown': '#A52A2A', 'burlywood': '#DEB887', 'cadetblue': '#5F9EA0', 'chartreuse': '#7FFF00', 'chocolate': '#D2691E', 'coral': '#FF7F50', 'cornflowerblue': '#6495ED', 'cornsilk': '#FFF8DC', 'crimson': '#DC143C', 'cyan': '#00FFFF', 'darkblue': '#00008B', 'darkcyan': '#008B8B', 'darkgoldenrod': '#B8860B', 'darkgray': '#A9A9A9', 'darkgreen': '#006400', 'darkkhaki': '#BDB76B', 'darkmagenta': '#8B008B', 'darkolivegreen': '#556B2F', 'darkorange': '#FF8C00', 'darkorchid': '#9932CC', 'darkred': '#8B0000', 'darksalmon': '#E9967A', 'darkseagreen': '#8FBC8F', 'darkslateblue': '#483D8B', 'darkslategray': '#2F4F4F', 'darkturquoise': '#00CED1', 'darkviolet': '#9400D3', 'deeppink': '#FF1493', 'deepskyblue': '#00BFFF', 'dimgray': '#696969', 'dodgerblue': '#1E90FF', 'firebrick': '#B22222', 'floralwhite': '#FFFAF0', 'forestgreen': '#228B22', 'fuchsia': '#FF00FF', 'gainsboro': '#DCDCDC', 'ghostwhite': '#F8F8FF', 'gold': '#FFD700', 'goldenrod': '#DAA520', 'gray': '#808080', 'green': '#008000', 'greenyellow': '#ADFF2F', 'honeydew': '#F0FFF0', 'hotpink': '#FF69B4', 'indianred': '#CD5C5C', 'indigo': '#4B0082', 'ivory': '#FFFFF0', 'khaki': '#F0E68C', 'lavender': '#E6E6FA', 'lavenderblush': '#FFF0F5', 'lawngreen': '#7CFC00', 'lemonchiffon': '#FFFACD', 'lightblue': '#ADD8E6', 'lightcoral': '#F08080', 'lightcyan': '#E0FFFF', 'lightgoldenrodyellow': '#FAFAD2', 'lightgray': '#D3D3D3', 'lightgreen': '#90EE90', 'lightpink': '#FFB6C1', 'lightsalmon': '#FFA07A', 'lightseagreen': '#20B2AA', 'lightskyblue': '#87CEFA', 'lightslategray': '#778899', 'lightsteelblue': '#B0C4DE', 'lightyellow': '#FFFFE0', 'lime': '#00FF00', 'limegreen': '#32CD32', 'linen': '#FAF0E6', 'magenta': '#FF00FF', 'maroon': '#800000', 'mediumaquamarine': '#66CDAA', 'mediumblue': '#0000CD', 'mediumorchid': '#BA55D3', 'mediumpurple': '#9370DB', 'mediumseagreen': '#3CB371', 'mediumslateblue': '#7B68EE', 'mediumspringgreen': '#00FA9A', 'mediumturquoise': '#48D1CC', 'mediumvioletred': '#C71585', 'midnightblue': '#191970', 'mintcream': '#F5FFFA', 'mistyrose': '#FFE4E1', 'moccasin': '#FFE4B5', 'navajowhite': '#FFDEAD', 'navy': '#000080', 'oldlace': '#FDF5E6', 'olive': '#808000', 'olivedrab': '#6B8E23', 'orange': '#FFA500', 'orangered': '#FF4500', 'orchid': '#DA70D6', 'palegoldenrod': '#EEE8AA', 'palegreen': '#98FB98', 'paleturquoise': '#AFEEEE', 'palevioletred': '#DB7093', 'papayawhip': '#FFEFD5', 'peachpuff': '#FFDAB9', 'peru': '#CD853F', 'pink': '#FFC0CB', 'plum': '#DDA0DD', 'powderblue': '#B0E0E6', 'purple': '#800080', 'rebeccapurple': '#663399', 'red': '#FF0000', 'rosybrown': '#BC8F8F', 'royalblue': '#4169E1', 'saddlebrown': '#8B4513', 'salmon': '#FA8072', 'sandybrown': '#F4A460', 'seagreen': '#2E8B57', 'seashell': '#FFF5EE', 'sienna': '#A0522D', 'silver': '#C0C0C0', 'skyblue': '#87CEEB', 'slateblue': '#6A5ACD', 'slategray': '#708090', 'snow': '#FFFAFA', 'springgreen': '#00FF7F', 'steelblue': '#4682B4', 'tan': '#D2B48C', 'teal': '#008080', 'thistle': '#D8BFD8', 'tomato': '#FF6347', 'turquoise': '#40E0D0', 'violet': '#EE82EE', 'wheat': '#F5DEB3', 'white': '#FFFFFF', 'whitesmoke': '#F5F5F5', 'yellow': '#FFFF00', 'yellowgreen': '#9ACD32'}

def list_importable_modules() -> list:
    importable_modules = []
    for module_info in pkgutil.iter_modules():
        if module_info.module_finder and module_info.name not in importable_modules:
            importable_modules.append(module_info.name)
    return importable_modules

def python_builtin_regex() -> None:
    python_builtins = dir(builtins)
    builtins_patterns = [f'\\b{re.escape(builtin)}\\b' for builtin in python_builtins]
    builtins_regex = '|'.join(builtins_patterns)
    return re.compile(builtins_regex)

def python_keyword_regex() -> None:
    python_keywords = keywords1
    keyword_patterns = [f'\\b{re.escape(keyword)}\\b' for keyword in python_keywords]
    keywords_regex = '|'.join(keyword_patterns)
    return re.compile(keywords_regex)

def special_keyword_regex() -> None:
    python_keywords = keywords0
    keyword_patterns = [f'\\b{re.escape(keyword)}\\b' for keyword in python_keywords]
    keywords_regex = '|'.join(keyword_patterns)
    return re.compile(keywords_regex)

def roundpara_regex() -> None:
    pattern = '\\(|\\)'
    return re.compile(pattern)

def squigpara_regex() -> None:
    pattern = '\\{|\\}'
    return re.compile(pattern)

def quote_regex() -> None:
    pattern = '"[^"]*"|\\\'[^\\\']*\\\''
    return re.compile(pattern)

def functions_def_regex() -> None:
    pattern = 'def\\s(\\w+)\\('
    return re.compile(pattern)

def assignment_regex() -> None:
    pattern = '(.+?)\\s='
    return re.compile(pattern)

def class_name_regex() -> None:
    pattern = '(\\w+)\\.\\w+\\(\\)'
    return re.compile(pattern)

def exact(integer: int) -> None:
    return tokenize.EXACT_TOKEN_TYPES[integer]

class CodeEditorApp:

    def __init__(self: Self, root: str):
        self.modules = list_importable_modules()
        self.kwregex = python_keyword_regex()
        self.builtinregex = python_builtin_regex()
        self.specialregex = special_keyword_regex()
        self.highlights = ['builtin', 'keyword', 'special', 'bracket1', 'bracket2', 'quote', 'function', 'assignment']
        self.allpatterns = [self.builtinregex, self.kwregex, self.specialregex, roundpara_regex(), squigpara_regex(), quote_regex(), functions_def_regex(), assignment_regex()]
        self.keywords_literal = keyword.kwlist
        self.builtins_literal = dir(builtins)
        self.comment_tag = '#'
        self.multilines = ('"""', "'''")
        self.brackets = '[{]}()'
        self.digits = '123467890'
        self.funcs = []
        self.classes = []
        self.aliases = []
        self.label_style = ttk.Style()
        self.label_style.configure('Dark.Label', foreground='#FFE4E1', background=DimGrayHTML)
        self.size = size()
        self.half_width = self.size.width // 2
        self.root: tk.Tk = root
        self.root.configure(bg='#333333')
        self.root.title('Code Editor')
        self.root.geometry(f'{self.size.width}x{self.size.height}')
        self.textframe_width = int(self.size.width * 0.08)
        self.textframe_height = int(self.size.height * 0.08)
        self.text_widget = tk.Text(self.root, background=DimGrayHTML, width=self.textframe_width, height=self.textframe_height, foreground='#FFE4E1', font='consolas 12')
        self.text_widget.grid(column=0, row=0, sticky='nsew', padx=0, rowspan=30)
        self.scrollbar = ttk.Scrollbar(self.root, command=self.text_widget.yview)
        self.scrollbar.grid(column=1, row=0, sticky='nsew', rowspan=30)
        self.text_widget.config(yscrollcommand=self.scrollbar.set)
        self.variable_label = tk.Label(self.root, foreground='white', font='consolas 12', background=DimGrayHTML, text='Variables', width=60, height=1)
        self.variable_label.grid(column=2, row=0, padx=0, sticky='nsew', rowspan=1)
        self.listbox_vars = []
        self.variables_listbox = tk.Listbox(self.root, listvariable=self.listbox_vars, foreground='white', background=DimGrayHTML, width=75)
        self.variables_listbox.grid(column=2, row=1, rowspan=4, sticky='nsew')
        self.text_widget.tag_configure('comment', foreground='#009933')
        self.text_widget.tag_configure('function', foreground='#FDED2A')
        self.text_widget.tag_configure('keyword', foreground='#a852ff')
        self.text_widget.tag_configure('special', foreground='#527dff')
        self.text_widget.tag_configure('bracket1', foreground='#FEF590')
        self.text_widget.tag_configure('bracket2', foreground='#C0B002')
        self.text_widget.tag_configure('quote', foreground='#FE877C')
        self.text_widget.tag_configure('assignment', foreground='#CCDAFF')
        self.text_widget.bind('<KeyRelease>', self.syntaxhighlight)
        self.menu_bar = Menu(self.root)
        self.root.config(menu=self.menu_bar)
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='File', menu=self.file_menu)
        self.file_menu.add_command(label='New', command=self.new_file)
        self.file_menu.add_command(label='Open', command=self.open_file)
        self.file_menu.add_command(label='Save', command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit', command=self.exit_app)
        self.edit_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='Edit', menu=self.edit_menu)
        self.edit_menu.add_command(label='Cut', command=self.cut_text)
        self.edit_menu.add_command(label='Copy', command=self.copy_text)
        self.edit_menu.add_command(label='Paste', command=self.paste_text)

    def syntaxhighlight(self: Self, *args):
        self.code = self.text_widget.get('1.0', tk.END)
        self.lines = self.code.split('\n')
        self.index = 0
        for line in self.lines:
            self.index += 1
            if line.strip().startswith('#'):
                self.text_widget.tag_add('comment', f'{self.index}.0', f'{self.index}.{len(line)}')
                continue
            for idx, pat in enumerate(self.allpatterns):
                matches = re.finditer(pat, line)
                for match in matches:
                    self.text_widget.tag_add(self.highlights[idx], f'{self.index}.{match.start()}', f'{self.index}.{match.end()}')
            if self.index < 50:
                if line.startswith('from '):
                    values = line.split(' ')
                    mapping = True if 'as' in values else False
                    if mapping:
                        self.classes.append(values[3])
                        self.aliases.append(values[-1])
                    else:
                        for index, value in enumerate(values):
                            if value == 'import':
                                for v in values[index + 1:]:
                                    self.funcs.append(v.strip().strip(','))
                                break
                elif line.startswith('import '):
                    values = line.split(' ')
                    mapping = True if 'as' in values else False
                    if mapping:
                        asindex = values.index('as')
                        name = values[1:asindex]
                        alias = values[asindex + 1:]
                        self.classes.append(name)
                        self.aliases.append(alias)
                    else:
                        for index, value in enumerate(line.split(' ')):
                            self.classes.append(value.strip())
        self.find_variable_definitions()

    def find_variable_definitions(self: Self):
        vars = []
        for line in self.lines:
            if line.strip().startswith('def '):
                continue
            lmatch = re.findall('\\b\\w+\\b\\s=\\s', line)
            for m in lmatch:
                vars.append(str(m[:-2]).strip())
        self.listbox_vars = list(set(vars))
        for index, v in enumerate(self.listbox_vars):
            self.variables_listbox.insert(index, v)

    def new_file(self: Self):
        self.text_widget.delete('1.0', tk.END)

    def open_file(self: Self):
        file_path = filedialog.askopenfilename(filetypes=[('Text files', '*.txt')])
        if file_path:
            with open(file_path, 'r') as file:
                file_content = file.read()
                self.text_widget.delete('1.0', tk.END)
                self.text_widget.insert('1.0', file_content)

    def save_file(self: Self):
        file_path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text files', '*.txt')])
        if file_path:
            with open(file_path, 'w') as file:
                file_content = self.text_widget.get('1.0', tk.END)
                file.write(file_content)

    def exit_app(self: Self):
        self.root.quit()

    def cut_text(self: Self):
        self.text_widget.event_generate('<<Cut>>')

    def copy_text(self: Self):
        self.text_widget.event_generate('<<Copy>>')

    def paste_text(self: Self):
        self.text_widget.event_generate('<<Paste>>')

    def add_import(self: Self, name: str) -> int:
        """ add a new import to highlight syntax for by name """

        def functions(name: str) -> int:
            try:
                mod = importlib.import_module(name)
                module_attrs = dir(mod)
                class_names = [attr for attr in module_attrs if isinstance(getattr(mod, attr), type)]
                functs = [attr for attr in module_attrs if callable(getattr(mod, attr))]
            except:
                return None
            return (class_names, functs)
        cnames, fnames = functions(name)
        for cname in cnames:
            self.classes.append(cname)
        for fname in fnames:
            self.funcs.append(fname)
if __name__ == '__main__':
    root = tk.Tk()
    app = CodeEditorApp(root)
    root.mainloop()