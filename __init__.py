import anywidget
import traitlets
import pathlib

class HelloWidget(anywidget.AnyWidget):
    _esm = pathlib.Path(__file__).parent / "static" / "index.js"
    _css = pathlib.Path(__file__).parent / "static" / "style.css"
    name = traitlets.Unicode("World").tag(sync=True)