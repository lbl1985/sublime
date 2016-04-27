import sublime, sublime_plugin, os

class FindUnderCursorCommand(sublime_plugin.WindowCommand):
    def run(self):
        view = self.window.active_view()
        view.run_command("expand_selection", {"to": "word"}) 
        view.run_command("slurp_find_string")
        self.window.run_command("show_panel", {"panel": "find", "reverse": False} )

class PathToClipboardCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sublime.set_clipboard(self.view.file_name())

class FilenameToClipboardCommand(sublime_plugin.TextCommand):
    def run(self, edit):
       sublime.set_clipboard(os.path.basename(self.view.file_name()))

class FiledirToClipboardCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        branch, leaf = os.path.split(self.view.file_name())
        sublime.set_clipboard(branch)

class FilenameLineNumToClipboardCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        folder_name, file_name = os.path.split(self.view.file_name())

        region1 = self.view.sel()[0]
        selection_text = self.view.substr(region1)

        line, column = self.view.rowcol(region1.begin())

        # line is 0 based therefore, plus 1
        line = line + 1
        msg = selection_text + " [" + file_name + ":" + str(line) + "]"
        # print msg
        sublime.set_clipboard(msg)