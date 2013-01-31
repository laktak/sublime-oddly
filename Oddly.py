import sublime, sublime_plugin

class OddlyCommand(sublime_plugin.WindowCommand):

  def run(self):
    self.window.show_input_panel("Oddly: select every n lines:", "2", self.on_done, None, None)
    pass

  def on_done(self, text):
    try:
      every = int(text)
      if self.window.active_view():
        self.window.active_view().run_command("oddlyn", {"every": every} )
    except ValueError:
      sublime.error_message("Please enter an integer!")
      pass

class OddlynCommand(sublime_plugin.TextCommand):

  def run(self, edit, every):
    every=int(every)
    sel = self.view.sel()
    if len(sel) > 0:
      all = self.view.split_by_newlines(sel[0])
      sel.clear()
      idx = 0
      for item in all:
        if idx % every == 0:
          sel.add(item)
        idx+=1

