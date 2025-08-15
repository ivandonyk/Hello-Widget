# Hello Widget

A React-based Jupyter widget using anywidget.

## Installation

```bash
pip install -e .
cd hello_widget/static && npm install
```

## Usage

```python
from hello_widget import HelloWidget

widget = HelloWidget(name="World")
widget.size = 32  # Font size in pixels
display(widget)
```